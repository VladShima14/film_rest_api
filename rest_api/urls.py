from rest_framework import routers, serializers, viewsets
from .views import FilmViewSet, GenreViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'film', FilmViewSet, 'film-list')
router.register(r'genre', GenreViewSet, 'genre-detail')

urlpatterns = router.urls
