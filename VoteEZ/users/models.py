from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="emails", unique=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    profile_pics = models.ImageField(upload_to="Images/User/Profile Pics")
    is_host = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

