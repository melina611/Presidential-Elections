from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_user, name="login_user"),
    path("signUp", views.signUp, name="signUp"),
    path("profile", views.profile, name="profile"),
]