from django import forms
from .models import MembershipPurchase
from profiles.models import Member_Data_Private


class MembershipPurchaseForm(forms.ModelForm):
    class Meta:
        model = MembershipPurchase
        exclude = ('purchase_number', 'member', 'membership_purchased',
                   'purchase_date', 'purchase_total', 'stripe_pid')


class MembershipPrivateDataForm(forms.ModelForm):
    class Meta:
        model = Member_Data_Private
        fields  = ['default_firstname', 'default_lastname',
                   'default_street_address1', 'default_street_address2',
                   'default_town_or_city', 'default_county', 'default_postcode',
                   'default_country',]
        
    def __init__(self, *args, **kwargs):
        """ Add placesholders and classes, remove auto-generated
        labels and set autfocus on first field - Source Code Institute
        Boutique Ado Walk-through project
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_firstname': 'First Name',
            'default_lastname': 'Last Name',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County, State or Locality',
            'default_postcode': 'Postal Code',
            'default_country': 'Country',
        }

        self.fields['default_firstname'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':   
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

