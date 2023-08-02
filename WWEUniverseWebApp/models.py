from django.db import models
from django.utils.text import slugify
from .helpers import MONTHS, WEIGHT_CLASSES, DAYS_OF_WEEK, YEARS, DAYS_OF_MONTH


class Shows(models.Model):
    """
    This is our model for representing Wrestling shows.
    """
    id = models.AutoField(primary_key=True)
    show_id = models.IntegerField(default=1)
    show_name = models.CharField(max_length=100)
    show_date = models.CharField(max_length=3, choices=DAYS_OF_WEEK, default='MON')

    def __str__(self):
        return self.show_name

    def save(self, *args, **kwargs):
        """
        This is our save method for Shows.
        :param args:
        :param kwargs:
        :return:
        """

        if not self.pk:
            # Check if the Show already exists
            show_exists = Shows.objects.filter(show_name=self.show_name).first()

            if show_exists:
                # If Show exists, use its ID
                self.show_id = show_exists.show_id
            else:
                # If Show doesn't exist, create a new ID
                # Get the last Show ID
                max_show_id = Shows.objects.all().aggregate(models.Max('show_id'))['show_id__max']
                # We use or 0 because if there are no Shows, max_show_id will be None
                self.show_id = (max_show_id or 0) + 1

        super(Shows, self).save(*args, **kwargs)

    @staticmethod
    def show_choices():
        """
        This method returns a list of Shows.
        :return:
        """

        # Build our Show Choices
        SHOW_CHOICES = [
            (show.show_id, show.show_name) for show in set(Shows.objects.all().order_by('show_name'))
        ]

        return SHOW_CHOICES


class Wrestlers(models.Model):
    """
    This is our model for representing Wrestlers.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    weight_class = models.CharField(max_length=3, choices=WEIGHT_CLASSES)

    def __str__(self):
        return self.name


class TitleBelts(models.Model):
    """
    This is our model for representing Title Belts.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    weight_class = models.CharField(max_length=3, choices=WEIGHT_CLASSES)

    def __str__(self):
        return self.name


class WrestlerStats(models.Model):
    """
    This will be our model for representing the stats of each Wrestler.
    Recording both Wins and Losses to calculate a ratio.
    """

    id = models.AutoField(primary_key=True)
    wrestler = models.OneToOneField(Wrestlers, on_delete=models.CASCADE, related_name='stats')
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ratio = models.FloatField(default=0.0)



class TitleHolders(models.Model):
    """
    This will be our model for representing the History of Title Holders.
    """
    id = models.AutoField(primary_key=True)
    wrestler = models.ForeignKey(Wrestlers, on_delete=models.CASCADE, default=1)
    title_belt = models.ForeignKey(TitleBelts, on_delete=models.CASCADE, default=1)
    month_won = models.CharField(max_length=2, choices=MONTHS, blank=True, default='01')
    day_won = models.CharField(choices=DAYS_OF_MONTH, max_length=2, blank=True, default='1')
    month_lost = models.CharField(max_length=2, choices=MONTHS, blank=True, default='01')
    day_lost = models.CharField(choices=DAYS_OF_MONTH, max_length=2, blank=True, default='1')
    year_won = models.CharField(max_length=4, choices=YEARS, blank=True, default='1')
    year_lost = models.CharField(max_length=4, choices=YEARS, blank=True, default='1')


class WrestlerShow(models.Model):
    """
    This will be our model for representing the Wrestlers on each Show.
    """

    id = models.AutoField(primary_key=True)
    wrestler = models.ForeignKey(Wrestlers, on_delete=models.CASCADE, default=1)
    show = models.ForeignKey(Shows, on_delete=models.CASCADE, default=1)
