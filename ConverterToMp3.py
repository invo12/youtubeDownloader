from moviepy.editor import *
from os import *
class ConverterToMp3:
    def __init__(self,songPath,destinationPath):
        self.songPath = songPath
        self.destinationPath = destinationPath
    def convert(self,songName):
        video = VideoFileClip(self.songPath)
        video.audio.write_audiofile(os.path.join(self.destinationPath,songName + '.mp3'))