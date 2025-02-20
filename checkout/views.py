from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from profiles.models import Member_Data_Private
from .forms import MembershipPrivateDataForm, MembershipPurchaseForm
from profiles.forms import RegistrationForm
from .models import MembershipPurchase
from membership.models import MembershipCategory
from basket.contexts import basket_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        print(pid)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        print(stripe.api_key)
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            # 'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        print(stripe.PaymentIntent)
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment was not \
            processed right now. Please try again.')
        return HttpResponse(content=e, status=400)


@login_required()
def checkout(request):
    """
    Displays the checkout page and handles a purchase.
    Creates/updates the member private profile
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    print(stripe_public_key)
    print('inside the checkout view')
    basket = request.session.get("basket", {})
    print(basket)
    # member_data_form = MembershipPrivateDataForm()
    # purchase_form = MembershipPurchaseForm()
    context = {}
    
    current_basket = basket_contents(request)
    print(current_basket)
    total = current_basket['total']
    print(total)
    stripe_total = round(total * 100)
    print(stripe_total)
    stripe.api_key = stripe_secret_key
    print('stripe_api_key')
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)  # delete

    member_data_form = MembershipPrivateDataForm()
    print(member_data_form)
    purchase_form = MembershipPurchaseForm()
    """ A view to return the Contact page """
    return render(request, 'public/contact.html')
    
    # template = "checkout/checkout.html"
    # context = {
    #     # "member_data_form": member_data_form,
    #     # "purchase_form": purchase_form,
    #     # "stripe_public_key": stripe_public_key,
    #     # "client_secret": intent.client_secret,
    # }

    # return render(request, template, context)

    # member_data_form = MembershipPrivateDataForm()
    # purchase_form = MembershipPurchaseForm()

    # template = "checkout/checkout.html"
    # context = {
    #     "member_data_form": member_data_form,
    #     "purchase_form": purchase_form,
    #     # "stripe_public_key": stripe_public_key,
    #     # "client_secret": intent.client_secret,
    # }

    # return render(request, template, context)



    # Check to see if user has an existing Member Profile
    # existing_member = Member_Data_Private.objects.filter(member=request.user)
    # print(existing_member)

    # if existing_member:
    #     """ A view to transfer to checkout existing member view """
    #     return redirect(reverse('checkout_existing_member'))
    
    # else:
    #     if request.method == "POST":
    #         basket = request.session.get("basket", {})
    #         for category_id, quantity in basket.items():
    #             category_id = category_id
    #             quantity = quantity
    #         selected_membership = get_object_or_404(MembershipCategory, pk=category_id)
    #         purchase_total = selected_membership.new_member_price * quantity
    #         print(selected_membership)
    #         # data for membership purchase
    #         form_data = {
    #             'membership_purchased_id': selected_membership.id,
    #             'purchase_total': purchase_total,
    #         }
            
    #         # private data to create member profile
    #         member_data = {
    #             'default_firstname': request.POST["default_firstname"],
    #             'default_lastname': request.POST["default_lastname"],
    #             'default_street_address1': request.POST["default_street_address1"],
    #             'default_street_address2': request.POST["default_street_address2"],
    #             'default_town_or_city': request.POST["default_town_or_city"],
    #             'default_county': request.POST["default_county"],
    #             'default_postcode': request.POST["default_postcode"],
    #             'default_country': request.POST["default_country"],
    #         }
    #         print(member_data)
    #         purchase_form = MembershipPurchaseForm(form_data)
    #         membership_form = MembershipPrivateDataForm(member_data)
    #         if purchase_form.is_valid():
    #             purchase = purchase_form.save(commit=False)
    #             purchase.member = request.user
    #             print(purchase.member)
    #             purchase.membership_purchased_id = selected_membership.id
    #             purchase.purchase_total = purchase_total
    #             pid = request.POST.get('client_secret').split('_secret')[0]
    #             purchase.stripe_pid = pid
    #             purchase.save()
    #             if membership_form.is_valid():
    #                 member_private_data = membership_form.save(commit=False)
    #                 member_private_data.member = request.user
    #                 member_private_data.membership_level = selected_membership
    #                 member_private_data.save()
    #                 messages.success(request, 'Member profile information was saved')
    #             request.session['save_info'] = 'save-info' in request.POST
    #             return redirect(reverse('checkout_success', args=[purchase.purchase_number]))
    #         else:
    #             messages.error(
    #                 request,
    #                 "There was an errory with your form. \
    #                     Please double check your information."
    #             )     
    #     else:
    #         basket = request.session.get("basket", {})
    #         print(basket)
    #         if not basket:
    #             messages.error(request, "There's nothing in your basket at the moment")
    #             return redirect(reverse("join"))
            
    #         current_basket = basket_contents(request)
    #         total = current_basket['total']
    #         stripe_total = round(total * 100)
    #         stripe.api_key = stripe_secret_key
    #         intent = stripe.PaymentIntent.create(
    #             amount=stripe_total,
    #             currency=settings.STRIPE_CURRENCY,
    #         )
    #         print(intent)  # delete
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


def checkout_existing_member(request):
    """
    Displays the checkout page and handles a purchase.
    Creates/updates the member private profile
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    original_profile = get_object_or_404(Member_Data_Private, member=request.user)
    print(original_profile)

    if request.method == "POST":
        basket = request.session.get("basket", {})
        for category_id, quantity in basket.items():
            category_id = category_id
            quantity = quantity
        selected_membership = get_object_or_404(MembershipCategory, pk=category_id)
        purchase_total = selected_membership.renewal_price * quantity
        print(selected_membership)
        print(purchase_total)
        # data for membership purchase
        form_data = {
            'membership_purchased_id': selected_membership.id,
            'purchase_total': purchase_total,
        }

        # private data to update member profile
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

        purchase_form = MembershipPurchaseForm(form_data)
        membership_form = MembershipPrivateDataForm(member_data, instance=original_profile)
        if purchase_form.is_valid():
            purchase = purchase_form.save(commit=False)
            purchase.member = request.user
            purchase.membership_purchased_id = selected_membership.id
            purchase.purchase_total = purchase_total
            pid = request.POST.get('client_secret').split("_secret")[0]
            purchase.stripe_pid = pid
            purchase.save()
            print(purchase.member)
            # Updates the member's private data profile
            if membership_form.is_valid():
                member_private_data = membership_form.save(commit=False)
                member_private_data.membership_level = selected_membership
                member_private_data.save()
                print(member_private_data.membership_level)
                messages.success(request, 'Member profille information was updated')
            return redirect(reverse('checkout_success_renewal', args=[purchase.purchase_number]))
        else:
            messages.error(
                request,
                "There was an errory with your form. \
                    Please double check your information."
            )     
    # open view with member profile pre-populating form
    else:
        basket = request.session.get("basket", {})
        if not basket:
            messages.error(request, "There's nothing in your basket at the moment")
            return redirect(reverse("join"))
        
        current_basket = basket_contents(request)
        total = current_basket['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        print(intent)
        member_data_form = MembershipPrivateDataForm(instance=original_profile)
        purchase_form = MembershipPurchaseForm()

        if not stripe_public_key:
            messages.warning(
                request,
                "Stripe public key is missing. \
                Did you forget to set it in your environment?",
            )

        template = "checkout/checkout_existing_member.html"
        context = {
            "member_data_form": member_data_form,
            "purchase_form": purchase_form,
            "stripe_public_key": stripe_public_key,
            "client_secret": intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, purchase_number):
    """ Handle successful checkouts """
    purchase = get_object_or_404(MembershipPurchase, purchase_number=purchase_number)
    member = request.user
    messages.success(request, f'Purchase successfully processed!')
    
    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'purchase': purchase,
        'member': member,
    }

    return render(request, template, context)


def checkout_success_renewal(request, purchase_number):
    """ Handle successful renewal checkouts """
    purchase = get_object_or_404(MembershipPurchase, purchase_number=purchase_number)
    member = request.user
    messages.success(request, f'Renewal successfully processed!')
    
    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success_renewal.html'
    context = {
        'purchase': purchase,
        'member': member,
    }

    return render(request, template, context)
