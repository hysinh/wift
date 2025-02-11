from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from membership.models import MembershipCategory
from profiles.models import Member_Data_Private


def basket_contents(request):
    basket_items = []
    total = 0
    product_count = 0

    basket = request.session.get('basket', {})

    existing_members = Member_Data_Private.objects.all()
    existing_member = Member_Data_Private.objects.filter(member=request.user)
    print(existing_member)

    if existing_member.exists():
        for category_id, quantity in basket.items():
            selected_membership_level = get_object_or_404(MembershipCategory, pk=category_id)
            total += quantity * selected_membership_level.renewal_price
            product_count += quantity
            basket_items.append({
                'category_id': category_id,
                'quantity': quantity,
                'selected_membership_level': selected_membership_level,
                'price': selected_membership_level.renewal_price
            })
    
    else:
        for category_id, quantity in basket.items():
            selected_membership_level = get_object_or_404(MembershipCategory, pk=category_id)
            total += quantity * selected_membership_level.new_member_price
            product_count += quantity
            basket_items.append({
                'category_id': category_id,
                'quantity': quantity,
                'selected_membership_level': selected_membership_level,
                'price': selected_membership_level.new_member_price
            })

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
    }

    return context