class YoutubeService:
    def __init__(self, youtube_gateway):
        self.youtube_gateway = youtube_gateway

    def search_videos(self, query):
        return self.youtube_gateway.search_videos(query)
