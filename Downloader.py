from pytube import YouTube

class Downloader:
    def __init__(self, link, path, progressBar):
        self.link = link
        self.path = path
        self.progressBar = progressBar
        self.yt = YouTube(self.link,on_progress_callback=self.progress)
    def download(self):
        self.yt.streams.first().download(self.path)
    def setLink(self, link):
        self.link = link
    def setPath(self, path):
        self.path = path
    def getName(self):
        return self.yt.title
    def progress(self,stream,chunk,file_handle,bytes_remaining):
        size = self.yt.streams.first().filesize
        self.progressBar['maximum'] = 100
        p = 0
        progress = p
        p = 100-self.percent(bytes_remaining, size)
        self.progressBar["value"] = int(p)
        self.progressBar.update()

    def percent(self, tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc