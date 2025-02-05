from django.shortcuts import render, redirect, reverse
from .forms import MembershipPrivateDataForm, MembershipPurchase
from django.contrib import messages


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('join'))
    
    member_data_form = MembershipPrivateDataForm()
    purchase_form = MembershipPurchase()
    template = 'checkout/checkout.html'
    context = {
        'member_data_form': member_data_form,
        'purchase_form': purchase_form,
    }

    return render(request, template, context)
