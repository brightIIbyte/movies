from django.shortcuts import render
from django.views.generic.base import View

from.models import Movie


class MoviesView(View):
    """Список фильмов"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movie_list.html", {"movie_list": movies})

class MovieDataView(View):
    """Полное описание фильма"""
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        return render(request, "movies/movie_detail.html", {"movie:movie"})

#static