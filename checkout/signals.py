from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import MembershipPurchase

@receiver(post_save, sender=MembershipPurchase)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update purchase total on membership level update/create
    """
    instance.purchase_total.update_purchase_total()
