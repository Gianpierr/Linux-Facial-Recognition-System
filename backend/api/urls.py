from django.urls import path
from .view import home

urlpatterns = [
    path('', home)
]