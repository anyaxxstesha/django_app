from django.contrib import admin

from dogs.models import Breed, Dog


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    """Breed admin model."""

    list_display = (
        "pk",
        "name",
        "size",
        "friendliness",
        "trainability",
        "shedding_amount",
        "exercise_needs",
    )
    list_filter = (
        "name",
        "size",
    )
    search_fields = ("name",)


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    """Dog admin model."""

    list_display = (
        "pk",
        "name",
        "age",
        "breed",
        "gender",
        "color",
        "favorite_food",
        "favorite_toy",
    )
    list_filter = (
        "name",
        "breed",
    )
    search_fields = ("name", "breed,")
