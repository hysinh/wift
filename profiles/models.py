from django.db import models
from django.contrib.auth.models import User
from membership.models import MembershipCategory
from django_countries.fields import CountryField


STATUS = ((0, "Inactive"), (1, "Active"))

class Member_Data_Private(models.Model):
    """
    Stores a single Member's Profile Private data
    """
    member = models.ForeignKey(User, on_delete=models.RESTRICT)
    membership_level = models.ForeignKey(MembershipCategory, on_delete=models.PROTECT)
    default_firstname = models.CharField(max_length=80, null=False, blank=False)
    default_lastname = models.CharField(max_length=80, null=False, blank=False)
    default_street_address1 = models.CharField(max_length=80, null=False, blank=False)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=False, blank=False)
    default_county = models.CharField(max_length=80, null=False, blank=False)
    default_postcode = models.CharField(max_length=20, null=False, blank=False)
    default_country = CountryField(blank_label='Country *', null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['member', 'default_lastname', 'default_firstname']
        verbose_name_plural = 'Member Data Private'

    def __str__(self):
        return f"{self.default_firstname} {self.default_lastname}"


class Member_Data_Public(models.Model):
    """
    Stores a single Member's Profile Public data
    """
    member = models.OneToOneField(User, on_delete=models.RESTRICT)
    public_firstname = models.CharField(max_length=80, null=True, blank=True)
    public_lastname = models.CharField(max_length=80, null=True, blank=True)
    # profile_image = CloudinaryField('image', default='placeholder')
    job_title = models.CharField(max_length=200, null=False, blank=False)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    # public_email = models.EmailField(max_length=254, null=True)
    # public_telephone = 
    website = models.URLField(max_length=200, null=True)
    imdb = models.URLField(max_length=200, null=True)
    # film_tv_credits = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.member.username
    
    class Meta:
        ordering = ['member', 'public_lastname', 'public_firstname']
        verbose_name_plural = 'Member Data Public'

