from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Member_Data_Private


@admin.register(Member_Data_Private)
class Member_Data_PrivateAdmin(SummernoteModelAdmin):
    list_display = ('default_lastname', 'default_firstname', 'status', 'membership_level')
    readonly_fields = ('created_on', 'updated_on')
    search_fields = ('default_lastname', 'default_firstname',)
    list_filter = ('status',)