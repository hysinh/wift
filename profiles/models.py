from django.db import models
from django.contrib.auth.models import User
from membership.models import Category


STATUS = ((0, "Inactive"), (1, "Active"))

class MemberProfile_Private(models.Model):
    """
    Stores a single Member's Profile Private data
    """
    member = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_level = models.ForeignKey(Category, on_delete=models.PROTECT)
    default_firstname = models.CharField(max_length=80, null=False, blank=False)
    default_lastname = models.CharField(max_length=80, null=False, blank=False)
    default_street_address1 = models.CharField(max_length=80, null=False, blank=False)
    default_street_address2 = models.CharField(max_length=80, null=False, blank=False)
    default_town_or_city = models.CharField(max_length=40, null=False, blank=False)
    default_county = models.CharField(max_length=80, null=False, blank=False)
    default_postcode = models.CharField(max_length=20, null=False, blank=False)
    default_country = models.CharField(max_length=20, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['default_lastname', 'default_firstname']

    def __str__(self):
        return f"{self.user.username}"

