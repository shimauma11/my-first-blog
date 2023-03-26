from django.contrib import admin
from .models import Problem
from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.register(User)
admin.site.register(Problem)