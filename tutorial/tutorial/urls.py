"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from example.views import hello, hello_and_name, movies_list, genre_list, first_page
from example.views import MovieListView, GenreListView
from example.views import MovieCreateView, GenreCreateView, MovieEditView, GenreEditView, GenreDetailView, GenreDelete, \
    MovieDetailView, MovieDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/', first_page),
    path('hello/', hello),
    path('hello/<str:name>/', hello_and_name),
    # path('start/movieslist/', movies_list),
    # path('start/genreslist/', genre_list),
    path('start/movie_list_by_class_view/', MovieListView.as_view(), name='movie_list'),
    path('start/genre_list_by_class_view/', GenreListView.as_view(), name='genre_list'),
    path('movie/add/', MovieCreateView.as_view()),
    path('genre/add/', GenreCreateView.as_view()),
    path('movie/edit/<int:pk>/', MovieEditView.as_view(), name="movie_edit"),
    path('genre/edit/<int:pk>/', GenreEditView.as_view(), name="genre_edit"),
    path('genre/detail/<int:pk>/', GenreDetailView.as_view(), name="genre_detail"),
    path('genre/delete/<int:pk>/', GenreDelete.as_view(), name="genre_delete"),
    path('movie/detail/<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
    path('movie/delete/<int:pk>/', MovieDelete.as_view(), name="movie_delete"),
]
