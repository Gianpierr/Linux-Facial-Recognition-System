from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class ProcessingTypes(models.TextChoices):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"

class Event(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

class MediaBase(models.Model):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING) # need to 
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



