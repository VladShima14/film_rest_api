from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "Genre: {}".format(self.name)


class Film(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey('Genre', related_name='film', blank=True, null=True)

    def __str__(self):
        return "Film name: {}".format(self.name)
