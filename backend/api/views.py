from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import (
    User,
    Video,
)
from .serializers import (
    UserSerializer,
    VideoSerializer,
)

class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class VideoPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class UserView(APIView):

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
    
    def get(self, request, pk=None):
        if pk:
            try:
                user = self.get_user(pk=pk)
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
            user = User.objects.get(pk=pk).delete()
            
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
            serializer = VideoSerializer(paginated_videos, many=True)

            return paginator.get_paginated_response(serializer.data)
    
    def post(self, request ):
        
        serializer = VideoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                    serializer.data, 
                    status = status.HTTP_201_CREATED
                )
    
    def put(self, request, pk = None):
        if not pk:
            return Response(
                {"error": "VideoID required for update"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            video = Video.objects.get(id = pk)

            serializer = VideoSerializer(video, data = request.data, many = True)

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
            video = Video.objects.get(id = pk).delete()

            return Response(
                status = status.HTTP_204_NO_CONTENT
            )

        except Video.DoesNotExist:

            return Response(
                {"error": "Video not found."},
                status = status.HTTP_404_NOT_FOUND
            )









            

        