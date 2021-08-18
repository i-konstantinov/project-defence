from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from OnlineCookbook.accounts.managers import OnlineCookbookUserManager


class OnlineCookbookUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    USERNAME_FIELD = 'email'

    is_staff = models.BooleanField(
        default=False,
    )
    is_superuser = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    objects = OnlineCookbookUserManager()


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    first_name = models.CharField(
        max_length=20,
        blank=True,
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
    )
    hometown = models.CharField(
        max_length=20,
        blank=True,
    )
    user = models.OneToOneField(
        OnlineCookbookUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from .signals import *
