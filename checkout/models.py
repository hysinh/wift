import uuid
from django.db import models
from membership.models import MembershipCategory
from profiles.models import User
from datetime import date
from decimal import Decimal
from datetime import datetime


class MembershipPurchase(models.Model):

    purchase_number = models.CharField(max_length=32, null=False, editable=False)
    member = models.ForeignKey(User, on_delete=models.RESTRICT, null=False, blank=False)
    membership_purchased = models.ForeignKey(MembershipCategory, on_delete=models.RESTRICT,
                                             null=False, blank=False)
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchase_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_purchase_number(self):
        """
        Generates a random, unique purchase number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number if it hasn't been set already
        """
        if not self.purchase_number:
            self.purchase_number = self._generate_purchase_number()
        super().save(*args, **kwargs)

    def update_purchase_total(self):
        """ Updates the purchase total dependent on the membership level selected """
        self.purchase_total = Decimal(self.membership_purchased.new_member_price)
        self.save()

    def get_purchase_date(self):
        return self.purchase_date.strftime("%d-%m-%Y")

    # determines if the membership is active
    @property
    def is_active(self):
        # return date.today() >= self.purchase_date and date.today() < (self.purchase_date + 365)
        return date.today() >= self.purchase_date and date.today() < (self.purchase_date + 365)
    
    # determines if the membership is inactive
    @property
    def is_inactive(self):
        return date.today() >= (self.purchase_date + 365)
    
    def __str__(self):
        return self.purchase_number