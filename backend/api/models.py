from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class ProcessingTypes:
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"



class Photo:
    image = models.ImageField(upload_to="images/") # TODO: do not forget to set the media root
    thumbnail = models.ImageField(upload_to="images/") # Maybe use to show the user thumbnails of their captured pictures
    captured_at = models.DateTimeField() 
    file_size = models.BigIntegerField() # For storage analytics
    format = models.CharField(max_length=10)
    is_flagged = models.BooleanField(default=False) # flagged for no deletion
    processing_status = models.TextChoices(choices = ProcessingTypes.choices)
    notes = models.TextField(blank=True)
    has_detections = models.BooleanField(default=False) # AI processing detected anything

    storage_path = models.CharField()




