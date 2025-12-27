from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserView, 
    VideoView,
    PhotoView,
    NotificationView,
    DetectionViewSet
)

router = DefaultRouter()
router.register(r'detections', DetectionViewSet, basename = 'detection')

urlpatterns = [
    path('users/', UserView.as_view(), name = "users"),
    path('users/<int:pk>/', UserView.as_view(), name = "users-detail"),
    path("videos/", VideoView.as_view(), name = "videos"),
    path("videos/<int:pk>/", VideoView.as_view(), name = "videos-detail"),
    path("photos/", PhotoView.as_view(), name = "photos"),
    path("photos/<int:pk>/", PhotoView.as_view(), name = "photos"),
    path("notifications/", NotificationView.as_view(), name = "notifications-detail"),
    path("notifications/<int:pk>/", NotificationView.as_view(), name = "notifications-detail"),
    # path("detections/", DetectionViewSet.as_view({"get":"list"}), name = "detections"),
    # path("detections/<int:pk>", DetectionViewSet.as_view({"get":"retrieve"}), name = "detections-detail"),
   path('', include(router.urls))
]