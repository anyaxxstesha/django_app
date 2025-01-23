from rest_framework.viewsets import ModelViewSet
from django.db.models import Subquery, Avg, OuterRef, Count, Value
from django.db.models.functions import Coalesce
from dogs.models import Breed, Dog
from dogs.serializers import (
    BreedSerializer,
    DogSerializer,
    DogDetailSerializer,
    DogListSerializer,
    BreedListSerializer,
)


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()

    def get_queryset(self):
        if self.action == "list":
            return Breed.objects.annotate(
                dogs_amount=Coalesce(
                    Subquery(
                        Dog.objects.filter(breed=OuterRef("id"))
                        .values("breed")
                        .annotate(dogs_amount=Count("*"))
                        .values("dogs_amount")
                    ),
                    Value(0),
                )
            )
        return Breed.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return BreedListSerializer
        return BreedSerializer


class DogViewSet(ModelViewSet):

    def get_queryset(self):
        if self.action == "list":
            return Dog.objects.annotate(
                avg_breed_age=Subquery(
                    Dog.objects.filter(breed=OuterRef("breed"))
                    .values("breed")
                    .annotate(avg_breed_age=Avg("age"))
                    .values("avg_breed_age")
                )
            )
        if self.action == "retrieve":
            self.serializer_class = DogDetailSerializer
            return Dog.objects.filter(pk=self.kwargs.get("pk")).annotate(
                dogs_amount_same_breed=Subquery(
                    Dog.objects.filter(breed=OuterRef("breed"))
                    .values("breed")
                    .annotate(dogs_amount_same_breed=Count("*"))
                    .values("dogs_amount_same_breed")
                )
            )
        return Dog.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return DogListSerializer
        if self.action == "retrieve":
            return DogDetailSerializer
        return DogSerializer
