# signals.py

from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_out
from django.utils import timezone
from django.db.models.signals import m2m_changed
from clone.models import Cart
from django.dispatch import receiver
from django.utils import timezone

@receiver(m2m_changed, sender=Cart.products.through)
def update_cart_total(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        instance.update_total_amount()
