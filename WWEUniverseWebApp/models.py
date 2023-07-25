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

    def name_and_date(self):
        return f"{self.show_name} ({self.show_date})"

    class Meta:
        """
        This is our meta class for Shows.
        """
        # This will make sure that the show_name is unique
        unique_together = ('show_id', 'show_date')

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


class TitleBelts(models.Model):
    """
    This is our model for representing Title Belts.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    weight_class = models.CharField(max_length=3, choices=WEIGHT_CLASSES)
    current_holder = models.ForeignKey(Wrestlers, to_field='name', on_delete=models.CASCADE, null=True)