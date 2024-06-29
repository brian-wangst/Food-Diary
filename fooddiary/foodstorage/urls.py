from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "foodstorage"
urlpatterns = [
    path('home/', views.homepage_view, name='homepage'),
]