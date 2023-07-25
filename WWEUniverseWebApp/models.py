from django.db import models

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

    class Meta:
        """
        This is our meta class for Shows.
        """
        # This will make sure that the show_name is unique
        unique_together = ('show_name', 'show_date')

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


class WrestlerStats(models.Model):
    """
    This is our model for representing Wrestler Stats.
    """

    id = models.AutoField(primary_key=True)
    name = models.ForeignKey(Wrestlers, on_delete=models.CASCADE)
    wins = models.IntegerField()
    losses = models.IntegerField()
    ratio = models.FloatField(default=float('inf'))


class TitleBelts(models.Model):
    """
    This is our model for representing Title Belts.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    weight_class = models.CharField(max_length=3, choices=WEIGHT_CLASSES)
    current_holder = models.ForeignKey(Wrestlers, to_field='name', on_delete=models.CASCADE, null=True)
    show = models.ForeignKey(Shows, on_delete=models.CASCADE)

    # if the belt is retired
    retired = models.BooleanField(default=False)
    retired_date = models.DateField(null=True)


class WrestlerTitles(models.Model):
    """
    This is our model for representing Title Belts held by Wrestlers.
    """

    id = models.AutoField(primary_key=True)
    wrestler = models.ForeignKey(Wrestlers, on_delete=models.CASCADE)
    title_belt = models.ForeignKey(TitleBelts, on_delete=models.CASCADE)


class WrestlerShows(models.Model):
    """
    This is our model for representing Shows Wrestlers have been on.
    """

    id = models.AutoField(primary_key=True)
    wrestler = models.ForeignKey(Wrestlers, on_delete=models.CASCADE)
    show = models.ForeignKey(Shows, on_delete=models.CASCADE)


class Matches(models.Model):
    """
    This is our model for representing Matches on the Shows
    """

    id = models.AutoField(primary_key=True)
    show = models.ForeignKey(Shows, on_delete=models.CASCADE)
    wrestler_one = models.ForeignKey(Wrestlers, on_delete=models.CASCADE, related_name='wrestler_one')
    wrestler_two = models.ForeignKey(Wrestlers, on_delete=models.CASCADE, related_name='wrestler_two')
    winner = models.ForeignKey(Wrestlers, on_delete=models.CASCADE, related_name='winner')
    loser = models.ForeignKey(Wrestlers, on_delete=models.CASCADE, related_name='loser')
    championship_match = models.BooleanField(default=False)
    title_belt = models.ForeignKey(TitleBelts, on_delete=models.CASCADE, null=True)
    match_date = models.CharField(max_length=3, choices=DAYS_OF_WEEK)

    # if we have a PPV
    ppv = models.BooleanField(default=False)
    ppv_name = models.CharField(max_length=100, blank=True)
    ppv_date = models.CharField(max_length=3, choices=DAYS_OF_WEEK, blank=True)
