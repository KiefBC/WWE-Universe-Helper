from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import WrestlerStats


@receiver(pre_save, sender=WrestlerStats)
def calculate_ratio(sender, instance, **kwargs):
    # Make Sure No Zeros
    if instance.wins == 0 and instance.losses == 0:
        instance.ratio = 0.00
    elif instance.wins == 0:
        instance.ratio = 0.00
    elif instance.losses == 0:
        instance.ratio = 1.00
    else:
        # Calculate the win-ratio of each Wrestler before saving
        instance.ratio = round(instance.wins / instance.losses, 2)
