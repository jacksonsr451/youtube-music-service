from flask import Flask
from youtube_music_service.controllers.youtube_controller import youtube_bp
from youtube_music_service.gateways.youtube_gateway import YoutubeGateway
from youtube_music_service.services.youtube_service import YoutubeService


def create_app():
    app = Flask(__name__)
    app.register_blueprint(youtube_bp, url_prefix='/youtube')
    return app
