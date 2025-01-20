# Generated by Django 5.1.5 on 2025-01-20 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Breed",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название породы",
                        max_length=100,
                        verbose_name="Название породы",
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("XS", "Tiny"),
                            ("S", "Small"),
                            ("M", "Medium"),
                            ("L", "Large"),
                        ],
                        help_text="Укажите размер",
                        max_length=2,
                        verbose_name="Размер",
                    ),
                ),
                (
                    "friendliness",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Укажите уровень дружелюбности от 1 до 5",
                        null=True,
                        verbose_name="Дружелюбность",
                    ),
                ),
                (
                    "trainability",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Укажите уровень дрессируемости от 1 до 5",
                        null=True,
                        verbose_name="Дрессируемость",
                    ),
                ),
                (
                    "shedding_amount",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Укажите уровень количества шерсти от 1 до 5",
                        null=True,
                        verbose_name="Шерсть",
                    ),
                ),
                (
                    "exercise_needs",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Укажите уровень нужды в упражнениях от 1 до 5",
                        null=True,
                        verbose_name="Нужда в упражнениях",
                    ),
                ),
            ],
            options={
                "verbose_name": "Порода",
                "verbose_name_plural": "Породы",
            },
        ),
        migrations.CreateModel(
            name="Dog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите кличку собаки",
                        max_length=100,
                        verbose_name="Кличка собаки",
                    ),
                ),
                (
                    "age",
                    models.PositiveSmallIntegerField(
                        help_text="Укажите возраст собаки",
                        verbose_name="Возраст собаки",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")],
                        help_text="Укажите пол собаки",
                        max_length=1,
                        verbose_name="Пол собаки",
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        blank=True,
                        help_text="Укажите цвет шерсти",
                        max_length=100,
                        null=True,
                        verbose_name="Цвет шерсти",
                    ),
                ),
                (
                    "favorite_food",
                    models.CharField(
                        blank=True,
                        help_text="Укажите любимую еду",
                        max_length=100,
                        null=True,
                        verbose_name="Любимая еда",
                    ),
                ),
                (
                    "favorite_toy",
                    models.CharField(
                        blank=True,
                        help_text="Укажите любимую игрушку",
                        max_length=100,
                        null=True,
                        verbose_name="Любимая игрушка",
                    ),
                ),
                (
                    "breed",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите породу собаки",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="dogs",
                        to="dogs.breed",
                        verbose_name="Порода собаки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Собака",
                "verbose_name_plural": "Собаки",
            },
        ),
    ]
