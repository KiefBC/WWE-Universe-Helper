from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import WrestlerStats

# calculate win ratio
@receiver(pre_save, sender=WrestlerStats)
def calculate_win_ratio(sender, instance, **kwargs):
    """
    This function calculates the win ratio for a Wrestler.
    :param instance:
    :param kwargs:
    :return:
    """

    # check if we are updating
    if instance._state.adding is False:

        # check if we have a change in wins
        if instance.wins != instance._original_wins:

            # check if we have a change in losses
            if instance.losses != instance._original_losses:

                # calculate the ratio
                instance.ratio = instance.wins / instance.losses