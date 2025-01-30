import uuid
from django.db import models
from membership.models import MembershipCategory
from profiles.models import User


class MembershipPurchase(models.Model):

    purchase_number = models.CharField(max_length=32, null=False, editable=False)
    member = models.ForeignKey(User, on_delete=models.RESTRICT, null=False, blank=False)
    membership_purchased = models.ForeignKey(MembershipCategory, on_delete=models.RESTRICT, null=False, blank=False)
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchase_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_purchase_number(self):
        """
        Generates a random, unique purchase number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        """
        Overrises the original save method to set the purchase number if it hasn't already been set
        """
        if not self.purchase_number:
            self.purchase_number = self._generate_purchase_number()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.purchase_number