from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import (
    User
)
from .serializers import (
    UserSerializer
)

class UserPagination(PageNumberPagination):
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
        if not pk:
            return Response(
                {"error": "UserID required for update"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response(
                {"error": "User does not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        