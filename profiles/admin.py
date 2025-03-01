from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Member_Data_Private, Member_Data_Public


@admin.register(Member_Data_Private)
class Member_Data_PrivateAdmin(SummernoteModelAdmin):
    list_display = ('member', 'default_lastname', 'default_firstname',
                    'status', 'membership_level')
    readonly_fields = ('created_on', 'updated_on')
    search_fields = ('default_lastname', 'default_firstname',)
    list_filter = ('status',)


@admin.register(Member_Data_Public)
class Member_Data_PublicAdmin(SummernoteModelAdmin):
    list_display = ('member', 'public_lastname', 'public_firstname',
                    'job_title')
    readonly_fields = ('created_on', 'updated_on')
    search_fields = ('public_lastname', 'public_firstname', 'member')
    list_filter = ('member',)
