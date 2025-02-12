from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stripe webhoooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles a generic/unknown/unexpected webhook event 
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
    
    def handle_payment_intent_succeeded(self, event):
        """
        Handles the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        print(intent) # delete this line after webhook tested and is working
        # should see purchase_form and member_form and metadata dictionaries in the payment intent printed to console
        pid = intent.id
        basket = intent.metadata.bag
        save_info = intent.metadata.save_info

        # billing

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )
    
    def handle_payment_intent_payment_failed(self, event):
        """
        Handles the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )