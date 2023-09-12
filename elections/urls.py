from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signUp", views.signUp, name="signUp"),
    path("login_user", views.login_user, name="login_user"),
    path("home", views.home, name="home"),
]