from django import forms
from .models import MembershipCategory

class MembershipLevelSelectionForm(forms.ModelForm):
    class Meta:
        model = MembershipCategory
        fields = ["name"]

    name = forms.ModelChoiceField(queryset=MembershipCategory.objects.all(), label='Membership Level')