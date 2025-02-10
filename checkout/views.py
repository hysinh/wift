from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import MembershipPrivateDataForm, MembershipPurchaseForm
from .models import MembershipPurchase
from membership.models import MembershipCategory
from basket.contexts import basket_contents

import stripe
import json


# def checkout(request):
#     stripe_public_key = settings.STRIPE_PUBLIC_KEY
#     stripe_secret_key = settings.STRIPE_SECRET_KEY

#     # delete - printing to check values
#     # basket = request.session.get('basket', {})
#     # print(basket)
#     # for category_id, quantity in basket.items():
#     #     category_id = category_id
#     #     quantity = quantity
#     # print(category_id)
#     # print(quantity)
#     # selected_membership = get_object_or_404(MembershipCategory, pk=category_id)
#     # print(selected_membership.name)
#     # purchase_total = selected_membership.new_member_price * quantity
#     # print(purchase_total)
#     # enddelete
#     if request.method == "POST":
#         basket = request.session.get("basket", {})
#         print(basket)
#         for category_id, quantity in basket.items():
#             category_id = category_id
#             quantity = quantity
#         print(category_id)
#         print(quantity)
#         selected_membership = get_object_or_404(MembershipCategory, pk=category_id)
#         print(selected_membership.name)
#         purchase_total = selected_membership.new_member_price * quantity
#         print(purchase_total)
#         purchase_form = MembershipPurchaseForm()
#         # the form data for the Membership Private Data form
#         form_data = {
#             "default_firstname": request.POST["default_firstname"],
#             "default_lastname": request.POST["default_lastname"],
#             "default_street_address1": request.POST["default_street_address1"],
#             "default_street_address2": request.POST["default_street_address2"],
#             "default_town_or_city": request.POST["default_town_or_city"],
#             "default_county": request.POST["default_county"],
#             "default_postcode": request.POST["default_postcode"],
#             "default_country": request.POST["default_country"],
#         }

#         member_info_form = MembershipPrivateDataForm(form_data)
#         if purchase_form.is_valid() and member_info_form.is_valid():
#             purchase = purchase_form.save(commit=False)
#             member_info = member_info_form.save(commit=False)
#             # sets the request.user as the member
#             purchase.member = request.user
#             member_info.member = request.user
#             print(request.user)
#             # sets the membership level purchased
#             purchase.membership_purchased = selected_membership
#             member_info.membership_level = selected_membership
#             print(member_info.membership_level)
#             purchase.purchase_total = selected_membership.new_member_price * quantity
#             pid = request.POST.get("client_secret").split("_secret")[0]
#             purchase.stripe_pid = pid
#             print(pid)
#             purchase.save()
#             member_info.save()
#             return redirect(
#                 reverse('checkout_success', args=[purchase.purchase_number])
#             )
#         else:
#             messages.error(
#                 request,
#                 "There was an error with your form.\
#                            Please double check your information.",
#             )
#     else:
#         basket = request.session.get("basket", {})
#         current_basket = basket_contents(request)

#         if not basket:
#             messages.error(request, "There's nothing in your basket at the moment")
#             return redirect(reverse("join"))

#         current_basket = basket_contents(request)
#         total = current_basket["total"]
#         print(total)
#         stripe_total = round(total * 100)
#         print(stripe_total)
#         stripe.api_key = stripe_secret_key
#         intent = stripe.PaymentIntent.create(
#             amount=stripe_total,
#             currency=settings.STRIPE_CURRENCY,
#         )
#         print(intent)
#         member_data_form = MembershipPrivateDataForm()
#         purchase_form = MembershipPurchaseForm()

#         if not stripe_public_key:
#             messages.warning(
#                 request,
#                 "Stripe public key is missing. \
#                 Did you forget to set it in your environment?",
#             )

#         template = "checkout/checkout.html"
#         context = {
#             "member_data_form": member_data_form,
#             "purchase_form": purchase_form,
#             "stripe_public_key": stripe_public_key,
#             "client_secret": intent.client_secret,
#         }

#         return render(request, template, context)


def checkout_test(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        basket = request.session.get("basket", {})
        print(basket)
        for category_id, quantity in basket.items():
            category_id = category_id
            quantity = quantity
        print(category_id)
        print(quantity)
        selected_membership = get_object_or_404(MembershipCategory, pk=category_id)
        print(selected_membership.name)
        print(selected_membership.id)
        purchase_total = selected_membership.new_member_price * quantity
        print(purchase_total)

        form_data = {
            'membership_purchased_id': selected_membership.id,
            'purchase_total': purchase_total,
        }
        print(form_data)
        member_data = {
            'default_firstname': request.POST["default_firstname"],
            'default_lastname': request.POST["default_lastname"],
            'default_street_address1': request.POST["default_street_address1"],
            'default_street_address2': request.POST["default_street_address2"],
            'default_town_or_city': request.POST["default_town_or_city"],
            'default_county': request.POST["default_county"],
            'default_postcode': request.POST["default_postcode"],
            'default_country': request.POST["default_country"],
        }
        print(member_data)
        purchase_form = MembershipPurchaseForm(form_data)
        membership_form = MembershipPrivateDataForm()
        if purchase_form.is_valid():
            purchase = purchase_form.save(commit=False)
            purchase.member = request.user
            purchase.membership_purchased_id = selected_membership.id
            purchase.purchase_total = purchase_total
            pid = request.POST.get('client_secret').split("_secret")[0]
            purchase.stripe_pid = pid
            print(pid)
            purchase.save()
            if membership_form.is_valid():
                member_private_data = membership_form.save(commit=False)
                messages.success(request, 'Member data form was valid')
                
            
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[purchase.purchase_number]))
        else:
            messages.error(
                request,
                "There was an errory with your form. \
                    Please double check your information."
            )     
    else:
        basket = request.session.get("basket", {})
        if not basket:
            messages.error(request, "There's nothing in your basket at the moment")
            return redirect(reverse("join"))
        
        current_basket = basket_contents(request)
        total = current_basket['total']
        print(total)
        stripe_total = round(total * 100)
        print(stripe_total)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        print(intent)
        member_data_form = MembershipPrivateDataForm()
        purchase_form = MembershipPurchaseForm()

        if not stripe_public_key:
            messages.warning(
                request,
                "Stripe public key is missing. \
                Did you forget to set it in your environment?",
            )

        template = "checkout/checkout_test.html"
        context = {
            "member_data_form": member_data_form,
            "purchase_form": purchase_form,
            "stripe_public_key": stripe_public_key,
            "client_secret": intent.client_secret,
        }

        return render(request, template, context)
    

def checkout_success(request, purchase_number):
    """ Handle successful checkouts """
    save_info = request.session.get('save_info')
    purchase = get_object_or_404(MembershipPurchase, purchase_number=purchase_number)
    member = request.user
    print(member.email)
    messages.success(request, f'Purchase successfully processed! \
                     Your purchase number is {purchase_number}. A confirmation \
                     email will be sent to {member.email}.')
    
    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'purchase': purchase,
        'member': member,
    }

    return render(request, template, context)
