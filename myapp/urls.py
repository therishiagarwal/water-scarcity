# myapp/urls.py

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.groundwater_map, name='home'),
]
