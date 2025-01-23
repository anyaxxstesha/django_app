from dogs.apps import DogsConfig
from dogs.views import DogViewSet, BreedViewSet

from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = DogsConfig.name
router = DefaultRouter()
router.register(r"breeds", BreedViewSet, basename="breed")
router.register(r"dogs", DogViewSet, basename="dog")

urlpatterns = [
    path("", include(router.urls)),
]
