from django.shortcuts import render
from .forms import ProblemForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.


class ProblemCreateView(CreateView):
    form_class = ProblemForm
    success_url = reverse_lazy("home:home")
    template_name = "answer/problemCreate.html"

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)
