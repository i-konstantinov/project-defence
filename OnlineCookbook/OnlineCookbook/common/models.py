from django.contrib.auth import get_user_model
from django.db import models

from OnlineCookbook.recipes.models import Recipe

UserModel = get_user_model()


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        max_length=100,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
