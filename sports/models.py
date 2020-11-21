from django.db import models


class Sport(models.Model):
    name = models.CharField("Nazwa sportu",max_length=128)

    def __str__(self):
        return self.name


class Event(models.Model):
    LEVEL = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )

    what = models.ForeignKey(Sport,on_delete=models.DO_NOTHING, verbose_name='Sport')
    where = models.CharField("Adres", max_length=128)

    when = models.DateTimeField("Kiedy")
    min_players = models.PositiveIntegerField()
    max_players = models.PositiveIntegerField()
    explevel = models.IntegerField("Level",choices=LEVEL, default=1)
    city = models.CharField("Miasto",max_length=128)

    # users = models.OneToOneField(User, blank=True, on_delete=models.DO_NOTHING)
    # city = models.ForeignKey(City, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.what)
