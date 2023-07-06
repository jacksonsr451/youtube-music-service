class SearchResponse:
    def __init__(self, videos):
        self.videos = videos

    def to_dict(self):
        return [{'title': video.title, 'video_id': video.video_id, 'video_url': f"https://www.youtube.com/watch?v={video.video_id}"}
                for video in self.videos]
