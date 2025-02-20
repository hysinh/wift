from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'read', )
    search_fields = ['name']
    list_filter = ['read']