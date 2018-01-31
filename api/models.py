import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email


class NPO(models.Model):
    organization_name = models.CharField(max_length=255)
    org_short_name = models.CharField(max_length=12, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    admin_user = models.OneToOneField(User, on_delete=models.PROTECT,
                                      related_name='npo_admin')
    employees = models.ManyToManyField(User)

    def __str__(self):
        return '%s, Active: %s' % (self.org_short_name, self.active)
