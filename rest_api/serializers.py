from rest_framework import serializers
from films.models import Film, Genre


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    film = serializers.StringRelatedField(many=False)

    class Meta:
        model = Genre
        fields = ('name', 'film')


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    genre = serializers.StringRelatedField(many=False)

    class Meta:
        model = Film
        fields = ('name', 'genre')
