from django.contrib.auth.models import User
from rest_framework import serializers
from models import (
    UserProfile
)

# TODO: Change to Model Serializer

class UserProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    phone = serializers.CharField(max_length=15)
    profile_pic = serializers.ImageField()

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items(): # iterate through update fields and set
            setattr(instance, attr, value)

        instance.save()
        return instance
    


class UserSerializer(serializers.Serializer):
    """ Serializer for user """
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    password = serializers.CharField(write_only=True, min_length=8)
    profile = UserProfileSerializer(required=False) 
    

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        validated_data.pop("password", None ) # Remove password if present
        for attr, value in validated_data.items(): # iterate through update fields and set
            setattr(instance, attr, value)

        instance.save()
        return instance
    
    # TODO: Add validation methods