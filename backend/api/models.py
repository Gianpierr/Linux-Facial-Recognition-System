from django.db import models
from django.contrib.auth.models import User
from .constants import (
    DetectionTypes,
    ProcessingTypes,
    EventStatusTypes,
    NotificationDeliveryTypes,
    DeliveryStatus,
    NotificationTypes
)

class Event(models.Model):
    started_at = models.DateTimeField(auto_now=True)
    ended_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    event_type = models.CharField(choices=EventStatusTypes.choices) 
    is_flagged = models.BooleanField(default=False)  # Has the picture/video been flagged for deletion
    is_reviewed = models.BooleanField(default=False) # Has user reviewed the Event
    detection_count = models.IntegerField(default=0)
    max_confidence = models.FloatField(default=0) 
    notification_sent = models.BooleanField(default=False) # have we sent a notification 
    notification_sent_at = models.DateTimeField(null=True) # when was the notification sent
    thumbnail = models.ImageField() # picture with the maximum confidence in detection of an object

    def __str__(self):
        return self.name
    
class MediaBase(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE) # need to 
    captured_at = models.DateTimeField() # timestamp when media object is captured
    created_at = models.DateField(auto_now_add=True) # creates the timestamp when created in DB
    updated_at = models.DateTimeField(auto_now=True) 
    is_flagged = models.BooleanField(default=False) # flagged for no deletion
    notes = models.TextField(blank=True, null=True)
    processing_status = models.CharField(choices = ProcessingTypes.choices)
    has_detections = models.BooleanField(default=False) # AI processing detected anything
    file_size = models.BigIntegerField() # For storage analytics

    class Meta:
        abstract = True

class Photo(MediaBase):
    image = models.ImageField(upload_to="images/") # TODO: do not forget to set the media root
    thumbnail = models.ImageField(upload_to="image_thumbnails/") # Maybe use to show the user thumbnails of their captured pictures
    image_format = models.CharField(max_length=10)
    width = models.IntegerField()
    height = models.IntegerField()
    storage_path = models.CharField()

class Video(MediaBase):
    video = models.FileField(upload_to="videos/") #TODO: do not forget to set the media root 
    thumbnail = models.ImageField(upload_to="video_thumbnails/")
    duration = models.FloatField()
    width = models.IntegerField()
    height = models.IntegerField() # might delete these attributes (currently do not see the reason behind adding yet)
    frame_rate = models.FloatField()
    codec = models.CharField(max_length=10) # compressor/decompressor type

class Notification(models.Model):
    notification_type = models.CharField(choices=NotificationTypes.choices) # we can make notification types (CRITICAL, NON-CRITICAL, URGENT ETC)
    message = models.TextField(blank=False, max_length=100) # will hold the notification message
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    delivery_method = models.CharField(choices=NotificationDeliveryTypes.choices)
    delivery_status = models.CharField(choices=DeliveryStatus.choices)
    
class Detection(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    detected_obj = models.CharField(choices=DetectionTypes.choices)
    detected_at = models.DateTimeField(auto_now=True)
    confidence = models.FloatField(default=0)
    label = models.CharField() # Using YOLO for detection which has 80+ object classes (Not to be confused with DetectionType: label is more specific)
    model_version = models.CharField()
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)
    bounding_box = models.JSONField() # For example {"x": 100, "y": 100, "width": 200, "height": 300}

