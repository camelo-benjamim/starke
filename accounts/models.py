from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name','email',]

    def __str__(self):
        return self.username
