from django import forms
from .models import Category

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

    name = forms.ModelChoiceField(queryset=Category.objects.all(), label='Membership Level')