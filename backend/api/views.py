from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .models import (
    User,
    Video,
    Photo,
    Notification,
    Detection,
    Event
)
from .serializers import (
    UserSerializer,
    VideoSerializer,
    PhotoSerializer,
    NotificationSerializer,
    DetectionSerializer,
    EventSerializer
)

class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class VideoPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PhotoPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class NotificationPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
class DetectionPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            try:
                user = User.objects.get(id = pk)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        else:
            users = User.objects.all()
            paginator = UserPagination()
            paginated_users = paginator.paginate_queryset(users, request)
            serializer = UserSerializer(paginated_users, many=True)

            return paginator.get_paginated_response(serializer.data)
        
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        # if primary key is not in request, return Error
        if not pk:
            return Response(
                {"error": "UserID required for update"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            user = User.objects.get(pk=pk) # get the user in question 
            serializer = UserSerializer(user, data=request.data, partial=True) # update that user

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "UserID not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            User.objects.get(pk=pk).delete()
            
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        except User.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )
            

class VideoView(APIView):
    def get(self, request, pk = None):
        if pk:
            try:
                video = Video.objects.get(id = pk)
                data = VideoSerializer(video).data
                return Response(data)
            except Video.DoesNotExist:
                return Response(
                    {"error": "Video not found."},
                    status = status.HTTP_404_NOT_FOUND
                )
        else:
            
            videos = Video.objects.all()
            paginator = VideoPagination()
            paginated_videos = paginator.paginate_queryset(videos, request)
            serializer = VideoSerializer(paginated_videos, many = True)

            return paginator.get_paginated_response(serializer.data)
    
    def post(self, request ):
        
        serializer = VideoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                    serializer.data, 
                    status = status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
    
    def put(self, request, pk = None):
        if not pk:
            return Response(
                {"error": "VideoID required for update"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            video = Video.objects.get(id = pk)

            serializer = VideoSerializer(video, data = request.data, partial = True)

            if serializer.is_valid():
                serializer.save()

                return Response(
                    serializer.data,
                    status = status.HTTP_200_OK
                )
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST
            )
            
        except Video.DoesNotExist:
            return Response(
                {"error": "Video not found."},
                status = status.HTTP_404_NOT_FOUND                
            )
    
    def delete(self, request, pk = None):
        if not pk:
            return Response(
                {"error": "VideoID required for deletion."}
            )
        try:
            Video.objects.get(id = pk).delete()
            return Response(
                status = status.HTTP_204_NO_CONTENT
            )

        except Video.DoesNotExist:
            return Response(
                {"error": "Video not found."},
                status = status.HTTP_404_NOT_FOUND
            )
        
class PhotoView(APIView):
    def get(self, request, pk = None):
        if pk:
            try:
                photo = Photo.objects.get(id = pk)
                serializer = PhotoSerializer(photo)
                return Response(
                    serializer.data,
                    status = status.HTTP_200_OK
                )

            except Photo.DoesNotExist:
                return Response(
                    {"error": "Photo not found."},
                    status = status.HTTP_404_NOT_FOUND
                ) 
        
        photos = Photo.objects.all()

        paginator = PhotoPagination()

        paginated_photos = paginator.paginate_queryset(photos, request)

        serializer = PhotoSerializer(paginated_photos, many = True)

        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = PhotoSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk = None):
        if not pk:
            return Response(
                {"error": "PhotoID required for update."},
                status = status.HTTP_400_BAD_REQUEST
            )
        try:
            photo = Photo.objects.get(id = pk)
            serializer = PhotoSerializer(photo, request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status = status.HTTP_200_OK
                )
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
        except Photo.DoesNotExist:
            return Response(
                {"error": "PhotoID required for update."}
            )
        
    def delete(self, request, pk = None):
        if not pk:
            return Response(
                {"error": "PhotoID not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            Photo.objects.get(pk=pk).delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        except Photo.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

class NotificationView(APIView):
    def get(self, request, pk = None):
        if not pk:
            notifications = Notification.objects.all()
            paginator = NotificationPagination()
            paginated_notifs = paginator.paginate_queryset(notifications, request)
            serializer = NotificationSerializer(paginated_notifs, many = True)

            return paginator.get_paginated_response(serializer.data)

        try:
            notification = Notification.objects.get(id = pk)
            serializer = NotificationSerializer(notification)
            return Response(
                serializer.data,
                status = status.HTTP_200_OK
            )
        except Notification.DoesNotExist:
            return Response(
                {"error": "Notification not found."},
                status = status.HTTP_404_NOT_FOUND
            )
    
    def post(self, request):
        serializer = NotificationSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
    
    def put(self, request, pk = None ):
        
        if not pk:
            return Response(
                {"error": "NotificationID required for update."},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        try:
            notification = Notification.objects.get(id = pk)
            serializer = NotificationSerializer(instance = notification, data = request.data, partial = True)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status = status.HTTP_200_OK
                )
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

        except Notification.DoesNotExist:
            
            return Response(
                {"error": "NotificationID required for update."},
                status = status.HTTP_404_NOT_FOUND
            )
        
    def delete(self, request, pk = None):
        if not pk:
            return Response(
                {"error": "NotificationID required for deletion"},
                status = status.HTTP_400_BAD_REQUEST
            )

        try:

            Notification.objects.get(id = pk).delete()
            return Response(
                status = status.HTTP_204_NO_CONTENT
            )
        except Notification.DoesNotExist:
            return Response(
                {"error": "NotificationID required for deletion."},
                status = status.HTTP_404_NOT_FOUND
            )


class DetectionViewSet(viewsets.ReadOnlyModelViewSet):
    """ 
    Read-only API for detections (created by AI processessing , not users)
    Provides: list() and retreive() only
    """
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializer

class EventViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer












            

        