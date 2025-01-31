from django import forms
from .models import Member_Data_Private
from membership.models import MembershipCategory

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Member_Data_Private
        fields = ['membership_level']

    membership_level = forms.ModelChoiceField(queryset=MembershipCategory.objects.all(), label='Membership Level')