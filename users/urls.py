from django.urls import path

from users import views

urlpatterns = [
    path("register/", views.UsersRegister.as_view(), name="register"),
    path("login/", views.Login.as_view(), name="login"),
]
