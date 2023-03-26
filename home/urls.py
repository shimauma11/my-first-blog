from django.urls import path
from .views import HomeView

app_name = "home"
urlpatterns = [
    path("", HomeView, name="home"),
]
