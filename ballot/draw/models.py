from django.db import models


class Athlete(models.Model):
    name = models.CharField(max_length=50, blank=True)
    number = models.IntegerField()
