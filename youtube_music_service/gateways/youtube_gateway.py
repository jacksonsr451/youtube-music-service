from googleapiclient.discovery import build

from youtube_music_service.entities.video import Video


class YoutubeGateway:
    def __init__(self, api_key):
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def search_videos(self, query, max_results=5) -> list:
        response = self.youtube.search().list(part='snippet', type='video',
                                              q=query, maxResults=max_results).execute()
        videos = []
        for item in response.get('items', []):
            videos.append(
                Video(title=item['snippet']['title'], video_id=item['id']['videoId']))
        return videos
