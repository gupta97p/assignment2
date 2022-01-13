from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.contrib.auth.models import UserManager



# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=20, unique=True, blank=False)
    email=models.EmailField(max_length=10, blank=False, unique=True)
    first_name=models.CharField(max_length=10, blank=False, unique=True)
    last_name=models.CharField(max_length=10, blank=False)
    age=models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    company_name=models.CharField(max_length=10, blank=False)
    city=models.CharField(max_length=10, blank=False)
    state=models.CharField(max_length=10, blank=False)
    zip=models.IntegerField(blank=False)
    web=models.CharField(max_length=10, blank=False)
    
    objects = UserManager()

    def __str__(self):
        return self.username