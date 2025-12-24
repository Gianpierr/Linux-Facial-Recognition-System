from django.contrib.auth.models import User
from rest_framework import serializers
from .models import (
    UserProfile,
    Photo,
    Video,
    Event,
    MediaBase
)

from .constants import (
    DetectionTypes,
    ProcessingTypes,
    EventStatusTypes,
    NotificationDeliveryTypes,
    DeliveryStatus,
    NotificationTypes
)

# TODO: Change to Model Serializer

class UserProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    phone = serializers.CharField(max_length=15)
    profile_pic = serializers.ImageField(required=False )

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

        if profile := validated_data.pop("profile"):
            user = User.objects.create(**validated_data)
            profile = UserProfile.objects.create(user = user, **profile)

        return user
    
    def update(self, instance, validated_data):
        validated_data.pop("password", None ) # Remove password if present
        for attr, value in validated_data.items(): # iterate through update fields and set
            setattr(instance, attr, value)

        instance.save()
        return instance
    
    # TODO: Add validation methods

# Another way to create a serializer (alot faster and better)
# Add a create and update method for you (Vewy nihhh!)
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = [
            'id', 'started_at', 'ended_at', 'created_at', 'updated_at',
            'event_type', 'detection_count', 'max_confidence', 'notification_sent',
            'notification_sent_at', 'thumbnail'
        ]
        

class MediaBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaBase
        fields = '__all__'
        read_only_fields = [
            'captured_at', 'created_at', 'updated_at', 'has_detections',
            'processing_status', 'file_size' 
        ]

        extra_kwargs = {
            'description' :{'required': False, 'allow_null': True},
        }
        



class PhotoSerializer(serializers.Serializer):
    image = serializers.ImageField(required=False, allow_null=True)
    image_format = serializers.CharField(max_length=10)
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    storage_path = serializers.CharField()
    
    def create(self, validated_data):
        return Photo.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    
    