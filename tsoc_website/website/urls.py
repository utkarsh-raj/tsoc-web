from django.urls import path
from . import views

urlpatterns = [
    path("", views.registration, name = "registration"),
    path("administrator", views.administrator, name = "administrator"),
]