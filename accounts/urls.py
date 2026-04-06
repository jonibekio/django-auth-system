from django.urls import path
from .views import SignUpView, HomePageView, AccountUpdateView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signup/edit/", AccountUpdateView.as_view(), name="edit"),
]
