from django.urls import path

from tts import views

urlpatterns = [
    path("register/", views.UsersRegister.as_view(), name="register"),
]
