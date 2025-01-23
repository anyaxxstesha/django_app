from rest_framework.serializers import ModelSerializer, DecimalField, IntegerField

from dogs.models import Breed, Dog


class BreedSerializer(ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"


class BreedListSerializer(ModelSerializer):
    dogs_amount = IntegerField(read_only=True, default=0)

    class Meta:
        model = Breed
        fields = [
            "id",
            "name",
            "size",
            "friendliness",
            "trainability",
            "shedding_amount",
            "exercise_needs",
            "dogs_amount",
        ]


class DogSerializer(ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"


class DogListSerializer(ModelSerializer):
    avg_breed_age = DecimalField(4, 2, coerce_to_string=False, read_only=True)

    class Meta:
        model = Dog
        fields = [
            "id",
            "name",
            "age",
            "breed",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
            "avg_breed_age",
        ]


class DogDetailSerializer(ModelSerializer):
    dogs_amount_same_breed = IntegerField(read_only=True)

    class Meta:
        model = Dog
        fields = [
            "id",
            "name",
            "age",
            "breed",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
            "dogs_amount_same_breed",
        ]
