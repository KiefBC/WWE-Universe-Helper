from django.db import models
from django.utils.text import slugify

# The only weight classes available
WEIGHT_CLASSES = [
    ('LHW', 'Light Heavyweight'),
    ('HW', 'Heavyweight'),
    ('SHW', 'Super Heavyweight'),
    ('CW', 'Cruiserweight'),
]

# The only days of the week available
DAYS_OF_WEEK = [
    ('MON', 'Monday'),
    ('TUE', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THU', 'Thursday'),
    ('FRI', 'Friday'),
    ('SAT', 'Saturday'),
    ('SUN', 'Sunday'),
]



# TODO: Remove show_date from Shows - it is not needed, why does it matter?
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
        """
        This method returns the name of the Wrestler.
        :return:
        """

        wrestler_name = self.name.title()
        return wrestler_name


class TitleBelts(models.Model):
    """
    This is our model for representing Title Belts.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    weight_class = models.CharField(max_length=3, choices=WEIGHT_CLASSES)
    current_holder = models.ForeignKey(Wrestlers, to_field='name', on_delete=models.CASCADE, null=True)


class WrestlerStats(models.Model):
    """
    This will be our model for representing the stats of each Wrestler.
    Recording both Wins and Losses to calculate a ratio.
    """

    id = models.AutoField(primary_key=True)
    wrestler = models.ForeignKey(Wrestlers, to_field='name', on_delete=models.CASCADE)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ratio = models.FloatField(default=0.0)
