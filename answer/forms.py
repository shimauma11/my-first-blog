from django import forms
from accounts.models import Problem


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ["english", "japanese", "degree"]
