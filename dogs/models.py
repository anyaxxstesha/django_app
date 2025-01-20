from django.db import models
from rest_framework.exceptions import ValidationError

NULLABLE = {"blank": True, "null": True}


class Breed(models.Model):
    SIZE_CHOICES = (
        ("XS", "Tiny"),
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Название породы",
        help_text="Укажите название породы",
    )
    size = models.CharField(
        max_length=2,
        choices=SIZE_CHOICES,
        verbose_name="Размер",
        help_text="Укажите размер",
    )
    friendliness = models.PositiveSmallIntegerField(
        verbose_name="Дружелюбность",
        help_text="Укажите уровень дружелюбности от 1 до 5",
        **NULLABLE,
    )
    trainability = models.PositiveSmallIntegerField(
        verbose_name="Дрессируемость",
        help_text="Укажите уровень дрессируемости от 1 до 5",
        **NULLABLE,
    )
    shedding_amount = models.PositiveSmallIntegerField(
        verbose_name="Шерсть",
        help_text="Укажите уровень количества шерсти от 1 до 5",
        **NULLABLE,
    )
    exercise_needs = models.PositiveSmallIntegerField(
        verbose_name="Нужда в упражнениях",
        help_text="Укажите уровень нужды в упражнениях от 1 до 5",
        **NULLABLE,
    )

    def __str__(self):
        return self.name

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        attrs_to_check = (
            self.friendliness,
            self.trainability,
            self.shedding_amount,
            self.exercise_needs,
        )
        approved_values = (1, 2, 3, 4, 5)
        for attr in attrs_to_check:
            if attr not in approved_values:
                raise ValidationError(f"The {attr} of a breed may differ from 1 to 5")
        super().save(
            *args,
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Dog(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    name = models.CharField(
        max_length=100, verbose_name="Кличка собаки", help_text="Укажите кличку собаки"
    )
    age = models.PositiveSmallIntegerField(
        verbose_name="Возраст собаки", help_text="Укажите возраст собаки"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        related_name="dogs",
        verbose_name="Порода собаки",
        help_text="Укажите породу собаки",
        **NULLABLE,
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        verbose_name="Пол собаки",
        help_text="Укажите пол собаки",
    )
    color = models.CharField(
        max_length=100,
        verbose_name="Цвет шерсти",
        help_text="Укажите цвет шерсти",
        **NULLABLE,
    )
    favorite_food = models.CharField(
        max_length=100,
        verbose_name="Любимая еда",
        help_text="Укажите любимую еду",
        **NULLABLE,
    )
    favorite_toy = models.CharField(
        max_length=100,
        verbose_name="Любимая игрушка",
        help_text="Укажите любимую игрушку",
        **NULLABLE,
    )

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return (
            f"Dog(name={self.name!r},"
            f" age={self.age!r}, breed={self.breed!r},"
            f" gender={self.gender!r}, color={self.color!r},"
            f" favorite_food={self.favorite_food!r}, favorite_toy={self.favorite_toy!r}"
        )

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        if self.age > 40:
            raise ValidationError("The lifespan of a dog does not exceed 40 years")
        super().save(
            *args,
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
