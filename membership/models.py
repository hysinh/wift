from django.db import models

STATUS = ((0, "Inactive"), (1, "Active"))


class MembershipCategory(models.Model):
    """
    Stores a single membership category
    """
    name = models.CharField(max_length=254)
    description = models.TextField()
    new_member_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, null=False)
    renewal_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['new_member_price', 'name']
        verbose_name_plural = 'Membership Categories'

    def __str__(self):
        return f"{self.name}"
