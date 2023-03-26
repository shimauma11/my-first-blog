from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
# Create your models here.


class User(AbstractUser):
    email = models.EmailField("メールアドレス", unique=True)


class Problem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="problems"
    )
    english = models.CharField(max_length=100)
    japanese = models.CharField(max_length=100)
    degree = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
