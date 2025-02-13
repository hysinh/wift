from django.http import HttpResponse
from .models import MembershipPurchase

import stripe


class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandle Webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        """
        Handles the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        print(intent) # delete this line after webhook tested and is working
        # should see purchase_form and member_form and metadata dictionaries in the payment intent printed to console
        pid = intent.id
        basket = intent.metadata.basket
        # save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        purchase_details = stripe_charge.purchase_details # updated
        member_details = intent.member_details
        total = round(stripe_charge.amount / 100, 2) # updated

        # Clean data in the shipping details
        for field, value in member_details.address.items():
            if value == "":
                member_details.address[field] = None

        try:
            purchase_exists = False
            purchase = MembershipPurchase.objects.get(
                purchase_number__iexact=member_details.purchase_number,
                member__iexact=member_details.member,
                membership_purchased__iexact=member_details.membership_purchased,
                purchase_date__iexact=member_details.purchase_date,
                purchase_total__iexact=member_details.purchase_total,
                stripe_pid__iexact=member_details.stripe_pid,
            )

            purchase_exists = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)

            return HttpResponse(
                content=f'Webhook received: {event["type"]}',
                status=200)
        except MembershipPurchase.DoesNotExist:
            try:
                purchase = MembershipPurchase.objects.create(
                    purchase_number=member_details.purchase_number,
                    member=member_details.member,
                    membership_purchased=member_details.membership_purchased,
                    purchase_date=member_details.purchase_date,
                    purchase_totat=member_details.purchase_total,
                    stripe_pid=member_details.stripe_pid,
                )
            except Exception as e:
                if purchase:
                    purchase.delete()
                return HttpResponse(f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        
    
    def handle_payment_intent_payment_failed(self, event):
        """
        Handles the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
