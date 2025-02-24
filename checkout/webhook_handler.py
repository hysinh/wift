from django.http import HttpResponse
from .models import MembershipPurchase
from profiles.models import MembershipCategory, Member_Data_Private

import stripe
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

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
        basket = intent.metadata.basket
        print(basket)
        for key in basket:
            membership_id = key
        membership_selected = MembershipCategory.objects.filter(pk=membership_id)
        print('membership_selected')
        print(membership_selected)
        
        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        print(stripe_charge)

        # member = stripe_charge.metadata.username
        # billing_details = stripe_charge.billing_details
        member_private_data = intent.shipping
        country = member_private_data.address.country
        print(country)
        grand_total = round(stripe_charge.amount / 100, 2)
        print(grand_total)

        for field, value in member_private_data.address.items():
            if value == "":
                member_private_data.address[field] = None

        purchase_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                purchase = MembershipCategory.objects.get(
                    member = stripe_charge.metadata.username,
                    membership_purchased = membership_selected,
                    purchase_total = grand_total,
                    stripe_pid = pid,
                )
                purchase_exists = True
                break
                
            except MembershipPurchase.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if purchase_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            purchase = None
            try:
                purchase = MembershipPurchase.objects.create(
                    stripe_pid = pid,
                    member = intent.metadata.username,
                    membership_purchased_id = membership_selected.id,
                    purchase_total = grand_total,
                )
            except Exception as e:
                if purchase:
                    purchase.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
      
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
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)