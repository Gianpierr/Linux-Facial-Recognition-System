from api.models import (
    Photo,
    MediaBase, 
    ProcessingTypes, 
    UserProfile,
    Event
)
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from api.serializers import (
    UserSerializer,
    UserProfileSerializer,
    PhotoSerializer,
    EventSerializer
)

def run():

    event_data = {
        'event_type': 'MOTION',  # or whatever your EventStatusTypes choices are
        'is_flagged': False,
        'is_reviewed': False,
        'detection_count': 5,
        'max_confidence': 0.85,
        'notification_sent': False,
        'notification_sent_at': None,
        'ended_at': None,
        'thumbnail': None,  # or provide an actual image file
    }
    
    event_serializer = EventSerializer(data=event_data)

    if event_serializer.is_valid():
        event_serializer.save()
    

    