from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import WrestlerStats


@receiver(pre_save, sender=WrestlerStats)
def calculate_ratio(sender, instance, **kwargs):
    # Make Sure No Zeros
    if instance.wins == 0:
        instance.wins = 1
    if instance.losses == 0:
        instance.losses = 1

    # Calculate the win-ratio of each Wrestler before saving
    instance.ratio = round(instance.wins / instance.losses, 2)
