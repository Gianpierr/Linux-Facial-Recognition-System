import parameterized
from rest_framework.exceptions import ErrorDetail
from django.test import TestCase
from django.utils import timezone

from .models import (
    Event, 
    Video, 
    Photo,
    Notification
)
from .serializers import (
    VideoSerializer,
    PhotoSerializer,
    EventSerializer
)


class VideoTest(TestCase):
    """ Test class for Video """

    def setUp(self):
        # clean up first
        Video.objects.all().delete()

        self.event = Event.objects.create(
            event_type='MOTION',
            is_flagged=False,
            is_reviewed=False,
            detection_count=5,
            max_confidence=0.85,
            notification_sent=False,
        )
    
        self.video = Video.objects.create(
            event=self.event,
            captured_at=timezone.now(),
            processing_status='COMPLETED',
            has_detections=True,
            file_size=15728640,
            duration=45.5,
            width=6767,
            height=42069,
            frame_rate=30.0,
            codec='H264',
        )

    def test_video_creation(self):
        video = self.video
        self.assertEqual(video.width, 6767)
        self.assertEqual(video.height, 42069)

    def test_update_video(self):
        video = Video.objects.get(id = 1)
        self.assertEqual(video.width, 6767)
        
        Video.objects.filter(id = 1).update(height = 420, width = 6967 )

        video = Video.objects.get(id = 1)

        assert video.height == 420
        assert video.width == 6967

    def test_video_serializer_to_json(self):
        data = VideoSerializer( instance = self.video ).data
        
        self.assertEqual(data["processing_status"], 'COMPLETED')
        self.assertEqual(data["file_size"], 15728640)

    def test_video_serializer_to_obj(self):
        
        video_data = {
            'event': self.event.id,
            'captured_at': timezone.now().isoformat(),
            'processing_status': 'PENDING',
            'file_size': 5242880,
            'video_format': 'mp4',
            'duration': 30.5,
            'storage_path': '/videos/new_test.mp4',
            'width': 1920,
            'height': 1080,
            'frame_rate': 30.0,
            'codec': 'h264',
        }

        serializer = VideoSerializer(data = video_data)

        
        self.assertFalse(serializer.is_valid())
        print(serializer.errors)
        
        self.assertEqual(serializer.errors, {
            'video': [ErrorDetail(string='No file was submitted.', code='required')]
            }
        ) # TODO: Add a case where there is a video object (library)
    ### 🚧 More tests WIP 🚧


        


    


