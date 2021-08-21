from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Recipe(models.Model):
    TYPE_CHOICE_MEAT_DISH = 'meat dish'
    TYPE_CHOICE_VEGETARIAN_DISH = 'vegetarian dish'
    TYPE_CHOICE_VEGAN_DISH = 'vegan dish'

    TYPE_CHOICES = (
        (TYPE_CHOICE_MEAT_DISH, 'Meat dish'),
        (TYPE_CHOICE_VEGETARIAN_DISH, 'Vegetarian dish'),
        (TYPE_CHOICE_VEGAN_DISH, 'Vegan dish'),
    )

    type = models.CharField(
        max_length=15,
        choices=TYPE_CHOICES,
    )
    title = models.CharField(
        max_length=50,
        blank=True,
    )
    ingredients = models.TextField(
        max_length=10000,
        blank=True,
    )
    instructions = models.TextField(
        max_length=10000,
        blank=True,
    )
    image = models.ImageField(
        upload_to='recipes',
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
