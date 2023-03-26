from django.shortcuts import render
from django.views.generic import ListView
from accounts.models import Problem

# Create your views here.


class HomeView(ListView):
    template_name = "home/home.html"
    model = Problem
    context_object_name = "problems"
    queryset = model.objects.select_related("user").order_by("-created_at")
