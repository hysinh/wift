from django import forms
from .models import Member_Data_Private, Member_Data_Public
from membership.models import MembershipCategory


class RegistrationForm(forms.ModelForm):
    """ User selects the desired membership level """
    class Meta:
        model = Member_Data_Private
        fields = ['membership_level']

    membership_level = forms.ModelChoiceField(
        queryset=MembershipCategory.objects.all(), label='Membership Level')


class MembershipPublicDataForm(forms.ModelForm):
    """ User inputs their public profile data """
    class Meta:
        model = Member_Data_Public
        fields = ['public_firstname', 'public_lastname', 'job_title',
                  'company_name', 'website', 'imdb']

    def __init__(self, *args, **kwargs):
        """ Add placesholders and classes, remove auto-generated
        labels and set autfocus on first field - Source Code Institute
        Boutique Ado Walk-through project
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'public_firstname': 'First Name',
            'public_lastname': 'Last Name',
            'job_title': 'Job Title',
            'company_name': 'Company Name',
            'website': 'website',
            'imdb': 'IMDB',
        }

        self.fields['public_firstname'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
