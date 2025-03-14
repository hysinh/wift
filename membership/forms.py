from django import forms
from .models import MembershipCategory


class RegistrationForm(forms.ModelForm):
    """ Selects the desired membership level """
    class Meta:
        model = MembershipCategory
        fields = ["name"]

    name = forms.ModelChoiceField(
        queryset=MembershipCategory.objects.all(), label='Membership Level')
