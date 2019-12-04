from tkinter import filedialog
from tkinter import *
from Downloader import *
from ConverterToMp3 import *

class GUI:
    def __init__(self):
        self.top = Tk()

        #for link
        self.linkLabel = Label(self.top,text = "Download Link")
        self.linkLabel.grid(row=0, column = 0)
        self.link = Entry(self.top)
        self.link.grid(row=0, column = 1)

        #choose directory
        self.directoryLabel = Label(self.top,text="Download directory")
        self.directoryLabel.grid(row=1, column=0)
        self.directory = Entry(self.top)
        self.directory.grid(row=1,column=1)
        self.browse = Button(self.top,text="Browse",command = self.changeDirCallBack)
        self.browse.grid(row=1, column=2)
        self.saveDir = Button(self.top,text="Save Directory",command = self.saveDirectoryCallBack)
        self.saveDir.grid(row=2,column=0)
        temp=""
        try:
            f = open("directory.txt","r")
            temp = f.readline()
            f.close()
        except:
            temp = ""
            print("File does not exist")
        self.directory.insert(0,temp)

        self.downloadButton = Button(self.top,text="Download",command = self.downloadCallBack)
        self.downloadButton.grid(row=2,column = 1)
        self.top.mainloop()
    def changeDirCallBack(self):
        self.directory.delete(0,END)
        self.directory.insert(0,filedialog.askdirectory())

    def saveDirectoryCallBack(self):
        f = open("directory.txt", "w")
        f.write(self.directory.get())
        f.close()

    def downloadCallBack(self):
        path = self.directory.get()
        try:
            #download to mp4
            downloader = Downloader(self.link.get(), path)
            downloader.download()
            songName = downloader.getName()
            downloadedVideoPath = os.path.join(path, songName + '.mp4')

            # then convert it to mp3
            converter = ConverterToMp3(downloadedVideoPath, path)
            converter.convert(songName)
            os.remove(downloadedVideoPath)
        except:
            print("can't download")