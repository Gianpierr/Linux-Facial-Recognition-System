from django.urls import path
from .views import (
    UserView, 
    VideoView,
)


urlpatterns = [
    path('users/<int:pk>/', UserView.as_view(), name = "users"),
    path("videos/<int:pk>/", VideoView.as_view(), name = "videos")
]