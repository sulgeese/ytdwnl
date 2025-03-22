import os
import logging

from aiogram.types import FSInputFile
from yt_dlp import YoutubeDL


logger = logging.getLogger(__name__)

class Download:
    def __init__(self, url: str):
        self.opts = {
            'paths': {'home': 'tmp/'},
            'logger': logging.getLogger('youtube-dl'),
        }
        self.url = url
        self.path = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.path and os.path.exists(self.path):
            os.remove(self.path)
        return True

    def audio(self) -> FSInputFile:
        opts = self.opts
        opts['format'] = 'm4a/bestaudio/best'
        opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
        with YoutubeDL(opts) as ydl:
            info = ydl.extract_info(self.url, download=True)
            self.path = info['requested_downloads'][0]['filename']
            title = f"{info['title']}.m4a"
            audio_id = FSInputFile(self.path, title)
            return audio_id