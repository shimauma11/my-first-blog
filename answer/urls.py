from django.urls import path
from .views import ProblemCreateView

app_name = "answer"

urlpatterns = [
    path("create/", ProblemCreateView.as_view(), name="create"),
]
