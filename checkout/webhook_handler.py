from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stripe webhoooks """

    def __init__(self, request):
        self.request = request

        class handle_event(self, event):
            """
            Handles a generic/unknown/unexpected webhook event 
            """
            return HttpResponse(
                content=f'Webhook received: {event["type"]}',
                status=200
            )