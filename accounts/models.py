from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    # Authentication
    email = models.EmailField(unique=True, max_length=251)
    password = models.CharField(max_length=128)

    # Personal Information
    first_name = models.CharField(max_length=80, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    # media
    profile_picture = models.ImageField(upload_to="profile_picture/",blank=True,null=True)

    # Social Links
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    website = models.URLField(blank=True)

    # Permissions 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # TimeStamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    # REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
