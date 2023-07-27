from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import WrestlerStats


@receiver(pre_save, sender=WrestlerStats)
def calculate_ratio(sender, instance, **kwargs):
    # Calculate the win-ratio of each Wrestler to 2 decimal places
    instance.ratio = round(instance.wins / instance.losses, 2)
