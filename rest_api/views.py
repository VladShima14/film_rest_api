from rest_framework import viewsets
from films.models import Film, Genre
from .serializers import FilmSerializer, GenreSerializer
# Create your views here.


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

