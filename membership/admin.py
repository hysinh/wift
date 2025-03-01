from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MembershipCategory


@admin.register(MembershipCategory)
class MembershipCategoryAdmin(SummernoteModelAdmin):
    list_display = ('name', 'new_member_price', 'status')
    search_fields = ('name',)
    list_filter = ('status',)
    summernote_fields = ('description',)
