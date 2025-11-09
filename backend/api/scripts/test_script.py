from api.models import Photo, MediaBase, ProcessingTypes
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection


def run():
    
    print(ProcessingTypes.choices)