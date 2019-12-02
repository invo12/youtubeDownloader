from Downloader import *
from ConverterToMp3 import *
from os import *
from subprocess import *
def main():
    #get the paths
    videosPath = "D:\\music"
    audioPath = "D:\\music"

    #download the video
    downloader = Downloader("https://www.youtube.com/watch?v=93ugDwiBVzA", videosPath)
    downloader.download()

    songName = downloader.getName()
    downloadedVideoPath = os.path.join(videosPath,songName + '.mp4')

    #then convert it to mp3
    converter = ConverterToMp3(downloadedVideoPath, audioPath)
    converter.convert(songName)

    os.remove(downloadedVideoPath)
if __name__ == '__main__':
    main()