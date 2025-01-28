from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MemberProfile_Private


@admin.register(MemberProfile_Private)
class MemberProfile_PrivateAdmin(SummernoteModelAdmin):
    list_display = ('default_lastname', 'default_firstname', 'status', 'membership_level')
    search_fields = ('default_lastname', 'default_firstname',)
    list_filter = ('status',)