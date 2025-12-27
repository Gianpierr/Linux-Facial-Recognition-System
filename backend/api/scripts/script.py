from api.models import (
    Photo,
    Video,
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
    EventSerializer,
    NotificationSerializer,
    DetectionSerializer
)

from api.constants import (
    DetectionTypes,
    ProcessingTypes,
    EventStatusTypes,
    NotificationDeliveryTypes,
    DeliveryStatus,
    NotificationTypes
)

from api.models import (
    User,
    Notification,
    Detection
)

def run():
    Video.objects.all().delete()


    # event = Event.objects.get(id = 4)


    # data = {
    #     "event": event.id,
    #     "detected_obj": DetectionTypes.PERSON,
    #     "detected_at": timezone.now().isoformat(),
    #     "label": "Label",
    #     "model_version": "modelv1",
    #     "photo": None,
    #     "video": None,
    #     "bounding_box": {"x": 100, "y": 100}
    # }

    

   

    # serializer = DetectionSerializer(data = data)

    # if serializer.is_valid():
    #     serializer.save()
        

    
    
    

    