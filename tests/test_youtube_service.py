import unittest
from unittest.mock import MagicMock
from youtube_music_service.entities.video import Video
from youtube_music_service.gateways.youtube_gateway import YoutubeGateway
from youtube_music_service.services.youtube_service import YoutubeService


class YoutubeServiceTestCase(unittest.TestCase):
    def test_search_videos(self):
        youtube_gateway_mock = MagicMock(YoutubeGateway)
        youtube_service = YoutubeService(youtube_gateway_mock)

        videos_mock = [
            Video(title='Video 1', video_id='123'),
            Video(title='Video 2', video_id='456')
        ]
        youtube_gateway_mock.search_videos.return_value = videos_mock

        videos = youtube_service.search_videos('music')

        youtube_gateway_mock.search_videos.assert_called_once_with('music')

        self.assertEqual(len(videos), 2)
        self.assertEqual(videos[0].title, 'Video 1')
        self.assertEqual(videos[1].title, 'Video 2')


if __name__ == '__main__':
    unittest.main()
