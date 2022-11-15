from django.urls import path

from tts import views

urlpatterns = [
    path("project/", views.ProjectView.as_view()),
    path("project/<int:pk>/", views.ProjectDetailView.as_view()),
]
