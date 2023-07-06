import unittest
from flask import Flask
from unittest.mock import patch
from youtube_music_service.controllers.youtube_controller import youtube_bp
from youtube_music_service.entities.video import Video


class YoutubeControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(youtube_bp, url_prefix='/youtube')
        self.client = self.app.test_client()

    @patch('youtube_music_service.controllers.youtube_controller.YoutubeService')
    def test_search(self, youtube_service_mock):
        youtube_service = youtube_service_mock.return_value
        youtube_service.search_videos.return_value = [
            Video(title='Video 1', video_id='123'),
            Video(title='Video 2', video_id='456')
        ]

        response = self.client.get('/youtube/search?query=music')

        self.assertEqual(response.status_code, 200)

        youtube_service.search_videos.assert_called_once_with('music')

        expected_data = [
            {
                'title': 'Video 1',
                'video_id': '123',
                'video_url': 'https://www.youtube.com/watch?v=123'
            },
            {
                'title': 'Video 2',
                'video_id': '456',
                'video_url': 'https://www.youtube.com/watch?v=456'
            },
        ]
        self.assertEqual(response.get_json(), expected_data)


if __name__ == '__main__':
    unittest.main()
