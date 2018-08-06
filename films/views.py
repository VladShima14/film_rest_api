from django.shortcuts import render
from django.db import transaction
from django.http import Http404
from .models import Genre, Film
from .forms import GenreForm, FilmForm
# Create your views here.


def index(request):
    return render(request, 'films/index.html')


def films(request):
    films_form = FilmForm()

    if request.method == 'POST':
        previous_film_form = FilmForm(request.POST)
        if previous_film_form.is_valid():
            with transaction.atomic():
                previous_film_form.save()
            films_form = previous_film_form
    return render(request, 'films/films.html', {
        'films': Film.objects.all(),
        'form': films_form,
    })


def film(request, film_pk):
    try:
        film_form = FilmForm(instance=Film.objects.get(pk=film_pk))
    except Film.DoesNotExist:
        raise Http404('There in no such film!')

    if request.method == 'POST':
        instance = Film.objects.get(pk=film_pk)
        previous_film_form = FilmForm(request.POST, instance=instance)
        if previous_film_form.is_valid():
            with transaction.atomic():
                previous_film_form.save()
            film_form = previous_film_form

    return render(request, 'films/film.html', {
        'form': film_form,
        'genres': Genre.objects.all().filter(film=film_pk),
    })


def genres(request):
    genres_form = GenreForm()

    if request.method == 'POST':
        previous_genres_form = GenreForm(request.POST)
        if previous_genres_form.is_valid():
            with transaction.atomic():
                previous_genres_form.save()
        else:
            genres_form = previous_genres_form

    return render(request, 'films/genres.html', {
        'genres': Genre.objects.all(),
        'form': genres_form,
    })


def genre(request, genre_pk):
    try:
        genre_form = GenreForm(instance=Genre.objects.get(pk=genre_pk))
    except Genre.DoesNotExist:
        raise Http404('There in no such genre theme!')

    if request.method == 'POST':
        instance = Genre.objects.get(pk=genre_pk)
        previous_genre_form = GenreForm(request.POST, instance=instance)
        if previous_genre_form.is_valid():
            with transaction.atomic():
                previous_genre_form.save()
            genre_form = previous_genre_form

    return render(request, 'films/genre.html', {
        'form': genre_form,
    })
