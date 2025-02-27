from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import MembershipPurchase
from profiles.models import MembershipCategory

import stripe
import time
import json


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, purchase):
        """Send the user a confirmation email"""
        cust_email = purchase.member.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'purchase': purchase})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'purchase': purchase, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )     

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        intent_basket = json.loads(intent.metadata.basket)
        basket = list(intent_basket.keys())
        membership_selected = get_object_or_404(MembershipCategory, pk=basket[0])
        
        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        member = stripe_charge.metadata.username
        member_private_data = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)
        username = intent.metadata.username

        for field, value in member_private_data.address.items():
            if value == "":
                member_private_data.address[field] = None

        # Check to see if Purchase exists in database
        purchase_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                member = User.objects.get(id=username)
                membership = MembershipCategory.objects.get(id=membership_selected.id)
                purchase = MembershipPurchase.objects.get(
                    member = member,
                    membership_purchased = membership,
                    purchase_total = grand_total,
                    stripe_pid = intent.id,
                )
                purchase_exists = True
                break
                
            except MembershipPurchase.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if purchase_exists:
            self._send_confirmation_email(purchase)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            # Create a Purchase if one does not exist in the database
            purchase = None
            try:
                member = User.objects.get(id=username)
                membership = MembershipCategory.objects.get(id=membership_selected.id)
                purchase = MembershipPurchase(
                    stripe_pid = intent.id,
                    member = member,
                    membership_purchased = membership,
                    purchase_total = grand_total,
                )
                purchase.save()
            except Exception as e:
                if purchase:
                    purchase.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)


        self._send_confirmation_email(purchase)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)                                     

        
    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)