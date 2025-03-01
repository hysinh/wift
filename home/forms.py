from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Creates a single contact form submission """
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
