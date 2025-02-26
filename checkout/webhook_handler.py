from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import MembershipPurchase
from profiles.models import MembershipCategory, Member_Data_Private

import stripe
import time
import json


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, purchase):
        """Send the user a confirmation email"""
        print('inside the send confirmation method')
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
        print('inside the handle_payment_intent_succeeded_webhook')
        intent = event.data.object
        print('intent from inside webhook handler')
        print(intent)
        pid = intent.id
        intent_basket = json.loads(intent.metadata.basket)
        # print('the intent basket')
        # print(intent_basket)
        basket = list(intent_basket.keys())
        # print('the basket')
        # print(basket)
        # print(basket[0])

        membership_selected = get_object_or_404(MembershipCategory, pk=basket[0])
        # print(membership_selected)
        # print(membership_selected.id)
        
        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        # print(stripe_charge)

        member = stripe_charge.metadata.username
        # print('member from stripe_charge')
        # print(member)
        member_private_data = intent.shipping
        country = member_private_data.address.country
        print(country)
        grand_total = round(stripe_charge.amount / 100, 2)
        # print(grand_total)

        username = intent.metadata.username
        # print('username')
        # print(username)
        member_id = User.objects.filter(pk=username)
        # print('member_id')
        # print(member_id)

        for field, value in member_private_data.address.items():
            if value == "":
                member_private_data.address[field] = None

        purchase_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                print(f"member: {username}, membership_purchased: {membership_selected.id}, purchase_total: {grand_total}, stripe_pid: {intent.id}")
                member = User.objects.get(id=username)
                membership = MembershipCategory.objects.get(id=membership_selected.id)
                purchase = MembershipPurchase.objects.get(
                    member = member,
                    membership_purchased = membership,
                    purchase_total = grand_total,
                    stripe_pid = intent.id,
                )
                # Breaks after this
                purchase_exists = True
                break
                
            except MembershipPurchase.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if purchase_exists:
            print(f"purchase exists event: {event}")
            self._send_confirmation_email(purchase)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            print("purchase does not exist")
            purchase = None
            try:
                print(f"stripe_pid: {intent.id}, member: {username}, membership_purchased: {membership_selected.id}, purchase_total: {grand_total}")
                member = User.objects.get(id=username)
                membership = MembershipCategory.objects.get(id=membership_selected.id)
                purchase = MembershipPurchase(
                    stripe_pid = intent.id,
                    member = member,
                    membership_purchased = membership,
                    purchase_total = grand_total,
                )
                purchase.save()
                member = Member_Data_Private(
                    member = member,
                    membership_level = membership,
                    default_firstname =  member_private_data.name,
                    default_street_address1 = member_private_data.address.line1,
                    default_street_address2 = member_private_data.address.line2,
                    default_town_or_city = member_private_data.address.city,
                    default_county = member_private_data.address.state,
                    default_postcode = member_private_data.address.postal_code,
                    default_country = member_private_data.address.country,
                )
                member.save()
                print(f'member was created: {member}')
            except Exception as e:
                print(f"unable to create DB record due to: {e}")
                if purchase:
                    purchase.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        print('send email here')
        self._send_confirmation_email(purchase)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)                                     

        # member_data = Member_Data_Private.objects.get(
        #     default_street_address1__iexact = member_private_data.address.line1,
        #     default_street_address2__iexact = member_private_data.address.line2,
        #     default_town_or_city__iexact = member_private_data.address.city,
        #     default_county__iexact = member_private_data.address.state,
        #     default_country__iexact = member_private_data.address.country,
        # )

        
    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        print(f"event: {event}")
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)