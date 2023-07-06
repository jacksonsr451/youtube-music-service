import dotenv
from flask import Blueprint, request, jsonify
from youtube_music_service.dtos.search_request import SearchRequest
from youtube_music_service.dtos.search_response import SearchResponse
from youtube_music_service.services.youtube_service import YoutubeService
from youtube_music_service.gateways.youtube_gateway import YoutubeGateway

youtube_bp = Blueprint('youtube', __name__)


dotenv.load_dotenv()


@youtube_bp.route('/search')
def search():
    request_data = SearchRequest.from_dict(request.args)
    query = request_data.query

    youtube_gateway = YoutubeGateway(dotenv.get_key('.env', 'API_KEY'))
    youtube_service = YoutubeService(youtube_gateway)
    videos = youtube_service.search_videos(query)

    return jsonify(SearchResponse(videos).to_dict())
