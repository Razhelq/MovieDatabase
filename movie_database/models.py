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
    favourite = models.BooleanField(default=False)


# {'Search': [{'Title': 'Beyond the Mat',
#              'Year': '1999',
#              'imdbID': 'tt0218043',
#              'Type': 'movie',
#              'Poster': 'https://m.media-amazon.com/images/M/MV5BMTQ5NDUzODkyOF5BMl5BanBnXkFtZTcwNjY3OTIyMQ@@._V1_SX300.jpg'},
#             {'Title': 'Pat & Mat', 'Year': '1976–2018', 'imdbID': 'tt0841929', 'Type': 'series', 'Poster': 'https://m.media-amazon.com/images/M/MV5BNTI1NTljM2EtYzQwNS00M2Y2LTlmOWQtZGZhNWFmYzA4MDM5XkEyXkFqcGdeQXVyMjIxMzMyMQ@@._V1_SX300.jpg'}, {'Title': 'Going to the Mat', 'Year': '2004', 'imdbID': 'tt0399104', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMjEzNzI4OTY2MF5BMl5BanBnXkFtZTgwMzQzMTE0NzE@._V1_SX300.jpg'}, {'Title': 'Salim Langde Pe Mat Ro', 'Year': '1989', 'imdbID': 'tt0241914', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMWQ2MzM3OTItMjQ4MC00MzA1LTgzYjQtYjk5YjFmOTE0N2MyXkEyXkFqcGdeQXVyMjUxMTY3ODM@._V1_SX300.jpg'}, {'Title': 'Mat the Cat', 'Year': '2005', 'imdbID': 'tt0445689', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BZDQzMGVjZTEtNWY4Ni00OTkzLWE2ODYtYWZhNTdiNjBmZGRlXkEyXkFqcGdeQXVyNjM3NTIzNjE@._V1_SX300.jpg'}, {'Title': 'Dil Pe Mat Le Yaar!!', 'Year': '2000', 'imdbID': 'tt0255120', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMjAwNzk5NzQzM15BMl5BanBnXkFtZTcwMjkxNDE0MQ@@._V1_SX300.jpg'}, {'Title': "Fool's Gold: The Story of the Brink's-Mat Robbery", 'Year': '1992', 'imdbID': 'tt0104286', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMTczMzIxMDA0OF5BMl5BanBnXkFtZTcwNDUxNzkxMQ@@._V1_SX300.jpg'}, {'Title': 'Pat & Mat', 'Year': '2016', 'imdbID': 'tt5320892', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BNTU2MWY2M2UtYmNiYy00YTM2LWI2YzItZDRmNGYzNTM1ZjI1L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjIxMzMyMQ@@._V1_SX300.jpg'}, {'Title': 'Sajan Re Phir Jhoot Mat Bolo', 'Year': '2017–2018', 'imdbID': 'tt8432526', 'Type': 'series', 'Poster': 'https://m.media-amazon.com/images/M/MV5BNzg5YTZkNzYtZWMzYi00YjljLTllZWMtMWYzMDBjOWQ0NWI3XkEyXkFqcGdeQXVyNzM4MjU3NzY@._V1_SX300.jpg'}, {'Title': 'Sajan Re Jhoot Mat Bolo', 'Year': '2009–2012', 'imdbID': 'tt2191327', 'Type': 'series', 'Poster': 'https://m.media-amazon.com/images/M/MV5BNzliNjY3N2YtMTU4NC00ZDRjLWExYjEtYWU2ZjM2ZTBmN2QwXkEyXkFqcGdeQXVyNDc0MDgzNTE@._V1_SX300.jpg'}], 'totalResults': '122', 'Response': 'True'}
