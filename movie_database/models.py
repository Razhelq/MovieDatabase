import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Movie(models.Model):
    title = models.CharField(max_length=128, unique=True)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), max_value_current_year])
    type = models.CharField(max_length=128)
    imdb_id = models.CharField(max_length=32, unique=True)
    poster = models.TextField()
    user = models.ManyToManyField(User)
