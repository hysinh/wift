from django.contrib import admin
from .models import MembershipPurchase


@admin.register(MembershipPurchase)
class MembershipPurchaseAdmin(admin.ModelAdmin):
    readonly_fields = ('purchase_number', 'purchase_date',  'member', 
                       'membership_purchased', 'purchase_total', 'stripe_pid')
    list_display = ('purchase_number', 'member', 'membership_purchased', 'purchase_date')
    order = ('-date',)
    search_fields = ['member']







