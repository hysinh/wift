from django.contrib import admin
from .models import MembershipPurchase


@admin.register(MembershipPurchase)
class MembershipPurchaseAdmin(admin.ModelAdmin):
    readonly_fields = ('purchase_number', 'purchase_date',  'member', 
                       'membership_purchased', 'purchase_total', 'stripe_pid')
    
    order = ('-date',)







