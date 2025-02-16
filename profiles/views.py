from django.shortcuts import render
from .models import Member_Data_Private, Member_Data_Public
from checkout.models import MembershipPurchase

# Create your views here.
def dashboard(request):
    """ Display the user's dashboard """
    membership_purchase = MembershipPurchase.objects.filter(member=request.user)

    
    template = "profiles/dashboard.html"
    context = {
        'membership_purchase': membership_purchase, 
    }

    return render(request, template, context)