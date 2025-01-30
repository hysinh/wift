from django.contrib import admin
from .models import MembershipPurchase


@admin.register(MembershipPurchase)
class MembershipPurchaseAdmin(admin.ModelAdmin):
    readonly_fields = ('purchase_number', 'purchase_date',
                       'purchase_total', 'stripe_pid')
    
    fields = ('purchase_number', 'member', 'purchase_date',
              'membership_purchased', 'purchase_total',
              'stripe_pid')
    
    order = ('-date',)







