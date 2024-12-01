from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Model


class User(AbstractUser):
    fio = models.CharField(max_length=100)
    phone = models.CharField(max_length=11, unique=True, null=True)
    email = models.EmailField(unique=True)


class Statement(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unique_id = models.IntegerField(unique=True)
    imposter = models.CharField(max_length=150)
    describe = models.CharField(max_length=500)
    status = models.CharField(max_length=20, default='На рассмотрении')