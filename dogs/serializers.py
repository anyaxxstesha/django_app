from rest_framework.serializers import ModelSerializer, DecimalField, IntegerField

from dogs.models import Breed, Dog


class BreedSerializer(ModelSerializer):
    """Standard serializer for Breed entity."""

    class Meta:
        """Meta data for BreedSerializer."""

        model = Breed
        fields = "__all__"


class BreedListSerializer(ModelSerializer):
    """Serializer for Breed list endpoint."""

    dogs_amount = IntegerField(read_only=True, default=0)

    class Meta:
        """Metadata for BreedListSerializer."""

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
    """Standard serializer for Dog entity."""

    class Meta:
        """Meta data for DogSerializer."""

        model = Dog
        fields = "__all__"


class DogListSerializer(ModelSerializer):
    """Serializer for Dog list endpoint."""

    avg_breed_age = DecimalField(4, 2, coerce_to_string=False, read_only=True)

    class Meta:
        """Metadata for BreedListSerializer."""

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
    """Serializer for dog detail endpoint."""

    dogs_amount_same_breed = IntegerField(read_only=True)

    class Meta:
        """Metadata for DogDetailSerializer."""

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
