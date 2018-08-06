from django.conf.urls import url

from .views import index, films, film, genres, genre

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^genres/$', genres, name='genres'),
    url(r'^genres/(?P<genre_pk>[0-9]+)/', genre, name='genre'),

    url(r'^films/$', films, name='films'),
    url(r'^films/(?P<film_pk>[0-9]+)/', film, name='film'),
]
