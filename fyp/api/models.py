from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):

    username = models.CharField(
        blank=True, null=True, max_length=30, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    patient_status = models.BooleanField(default=False)
    doctor_status = models.BooleanField(default=False)
    admin_status = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.first_name + " " + self.last_name


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    profile = models.CharField(max_length=100)
    rating = models.IntegerField(null=False)
    phone = models.CharField(max_length=15)
    about = models.TextField(max_length=500, default="Description")
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name
