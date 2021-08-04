from django.contrib import admin
from django.urls import path, include
import views

urlpatterns = [
    path("", views.root),
    path("time_display", views.index),
]