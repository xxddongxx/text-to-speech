from django.urls import path

from tts import views

urlpatterns = [
    path("project/", views.ProjectView.as_view()),
]
