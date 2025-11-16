from django.db import models

class ProcessingTypes(models.TextChoices):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"

class DetectionTypes(models.TextChoices):
    PERSON = "PERSON"
    ANINAL = "ANIMAL"
    VEHICLE = "VEHICLE" # Minimum Types for testing (will add more later)
    UNKNOWN_OBJECT = "UNKNOWN_OBJECT"
    MULTIPLE_OBJECTS = "False" # Maybe change but does not support it being a Boolean False

class EventStatusTypes(models.TextChoices):
    ACTIVE = "ACTIVE"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    ARCHIVED = "ARCHIVED"

class NotificationDeliveryTypes(models.TextChoices):
    EMAIL = "EMAIL"
    SMS = "SMS"
    BOTH = "BOTH"

class NotificationTypes(models.TextChoices):
    NORMAL = "NORMAL" # Test notification types for now TODO: Add more specific notification types
    URGENT = "URGENT"
    
class DeliveryStatus(models.TextChoices):
    PENDING = "PENDING"
    SENDING = "SENDING"
    SENT = "SENT"
    FAILED = "FAILED"
    RETRYING = "RETRYING" # Note: Some of these fields are experimental 
