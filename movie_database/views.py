import requests
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View

from movie_database.forms import MovieForm, LoginForm
from movie_database.models import Movie


class MainPage(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        movie_form = MovieForm()
        try:
            title = request.GET['title']
            movies = self.get_movies(request, title)
        except:
            movies = False
            title = False
        return render(request, 'main_page.html', {'movie_form': movie_form, 'movies': movies, 'title': title})

    def get_movies(self, request, title):
        movies = Movie.objects.filter(title__contains=title)
        paginator = Paginator(movies, 1)
        page = request.GET.get('page')
        movies = paginator.get_page(page)
        return movies

    def post(self, request):
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            title = movie_form.cleaned_data['title']
            self.look_for_movie(title)
        else:
            title = False
        movies = self.get_movies(request, title)
        return render(request, 'main_page.html', {'movie_form': movie_form, 'movies': movies, 'title': title})

    @staticmethod
    def look_for_movie(title):
        movies_json = requests.get(f'https://omdbapi.com/?s={title}&apikey=8e68ddd9').json()
        for movie in movies_json['Search']:
            try:
                Movie.objects.create(
                    title=movie['Title'],
                    year=movie['Year'],
                    imdb_id=movie['imdbID'],
                    type=movie['Type'],
                    poster=movie['Poster']
                )
            except IntegrityError:
                pass


