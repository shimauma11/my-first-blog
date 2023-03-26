from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField("メールアドレス", unique=True)


class Problem(models.Model):
    english = models.CharField(max_length=100)
    japanese = models.CharField(max_length=100)
    degree = models.IntegerField()
