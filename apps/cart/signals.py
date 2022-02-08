from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Cart


@receiver(post_save, sender=get_user_model())
def create_user_cart(sender, **kwargs):
    if kwargs['created']:
        Cart(user=kwargs['instance']).save()
