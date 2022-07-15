from pathlib import Path
from game_.scripting.action import Action


class LoadAssetsAction(Action):

    def __init__(self, audio_service, video_service):
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        # TODO: change the assets paths to whatever they should be
        self._audio_service.load_sounds("game/assets/sounds")
        self._video_service.load_fonts("game/assets/fonts")
        self._video_service.load_images("game/assets/images")
        self._video_service.load_images("game/assets/images/stars")
        self._video_service.load_images("game/assets/images/Ship1")
        self._video_service.load_images("game/assets/images/Ship2")
        self._video_service.load_images("game/assets/images/Ship3")
        self._video_service.load_images("game/assets/images/Explosion")
        