from django.shortcuts import render
from django.http import HttpResponse
from example.models import Movie, Genre
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from example.forms import MovieForm, GenreForm


class MovieListView(ListView):
    model = Movie
    template_name = "genmovlist.html"
    context_object_name = "movies"


class GenreListView(ListView):
    model = Genre
    template_name = "gengenlist.html"
    context_object_name = "genres"


class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    success_url = "../../start/movie_list_by_class_view/"
    template_name = "movie_add.html"


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    success_url = '../../start/genre_list_by_class_view/'
    template_name = "genre_add.html"


class MovieEditView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "movie_update.html"
    success_url = '../../../start/movie_list_by_class_view/'


class GenreEditView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = "genre_update.html"
    success_url = '../../../start/genre_list_by_class_view/'


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"


class GenreDetailView(DetailView):
    model = Genre
    template_name = "genre_detail.html"


class MovieDelete(DeleteView):
    model = Movie
    template_name = "movie_confirm_delete.html"
    success_url = '../../../start/movie_list_by_class_view/'


class GenreDelete(DeleteView):
    model = Genre
    template_name = "genre_confirm_delete.html"
    success_url = '../../../start/genre_list_by_class_view/'


def hello(request):
    return HttpResponse("Pure http response from django")


def hello_and_name(request, name):
    return HttpResponse(f"Pure response with variable: {name}")


def movies_list(request):
    movies = Movie.objects.all()
    return render(request, "movieslist.html", {"movies": movies})


def genre_list(request):
    genres = Genre.objects.all()
    return render(request, "genreslist.html", {"genres": genres})


def first_page(request):
    return render(request, "index.html")


