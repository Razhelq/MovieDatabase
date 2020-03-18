import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=128, unique=True)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), max_value_current_year])
    type = models.CharField(max_length=128, unique=True)
    poster = models.TextField()
    user = models.ManyToManyField(User)
