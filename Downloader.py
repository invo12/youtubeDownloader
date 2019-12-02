from pytube import YouTube
import os
from moviepy.editor import *

class Downloader:
    def __init__(self, link, path):
        self.link = link
        self.path = path
        self.yt = YouTube(self.link)
    def download(self):
        self.yt.streams.first().download(self.path)
    def setLink(self, link):
        self.link = link
    def setPath(self, path):
        self.path = path
    def getName(self):
        return self.yt.title