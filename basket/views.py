from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from membership.models import MembershipCategory
from profiles.forms import RegistrationForm
from django.contrib import messages


def view_basket(request):
    """A view to display the basket"""
    form = RegistrationForm()
    context = {}

    categories = MembershipCategory.objects.all()
    context = {
        "form": form,
        "categories": categories,
    }

    return render(request, "basket/basket.html", context)


def add_to_basket(request, category_id):
    """Add an annual memebership to the basket"""

    selected_membership_level = get_object_or_404(MembershipCategory, pk=category_id)
    quantity = 1
    basket = request.session.get("basket", {})

    basket.clear()
    basket[category_id] = quantity
    request.session["basket"] = basket

    messages.success(
        request, f"Added {selected_membership_level} membership to your basket"
    )
    return redirect("view_basket")


def remove_from_basket(request, category_id):
    """Remove the membership from the basket"""

    try:
        selected_membership_level = get_object_or_404(
            MembershipCategory, pk=category_id
        )
        basket = request.session.get("basket", {})
        basket.pop(category_id)
        request.session["basket"] = basket
        messages.success(
            request, f"{selected_membership_level} membership removed from your basket"
        )

        return redirect("view_basket")

    except Exception as e:
        messages.error(request, f"Error removing item; {e}")
        return HttpResponse(status=500)
