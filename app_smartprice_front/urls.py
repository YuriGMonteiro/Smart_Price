from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "app_smartprice_front"

urlpatterns = [
    path('', views.home, name="home"),
]
