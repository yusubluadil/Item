from django.db import models
from django.contrib.auth.models import AbstractUser
from . manager import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    specialty = models.CharField(max_length=150, null=True,blank=True)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email