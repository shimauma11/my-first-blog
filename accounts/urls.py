from django.urls import path
from .views import SignupView, UserLoginView, UserLogoutView

app_name = "accounts"

urlpatterns = [
    path("", UserLoginView.as_view(), name="login"),
    path("signup", SignupView.as_view(), name="signup"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
