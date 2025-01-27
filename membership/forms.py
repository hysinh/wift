from django import forms
from .models import Category

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]