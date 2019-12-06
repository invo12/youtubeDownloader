from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from Downloader import *
from ConverterToMp3 import *
import time
import threading

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

        self.currentRow = 3
        self.top.mainloop()

    def changeDirCallBack(self):
        self.directory.delete(0,END)
        self.directory.insert(0,filedialog.askdirectory())

    def saveDirectoryCallBack(self):
        f = open("directory.txt", "w")
        f.write(self.directory.get())
        f.close()

    def downloadCallBack(self):
        threading.Thread(target=self.download).start()

    def download(self):
        progressBar = ttk.Progressbar(self.top, orient="horizontal", length=286, mode="determinate")
        progressBar.grid(row=self.currentRow, column=0)

        progressBarText = StringVar()
        progressBarText.set('')
        progressBarLabel = Label(self.top, textvariable=progressBarText)
        progressBarLabel.grid(row=self.currentRow, column=1)

        self.currentRow += 1
        path = self.directory.get()
        path = path.replace('/','\\')
        try:
            progressBarText.set('Downloading')
            #download to mp4
            downloader = Downloader(self.link.get(), path, progressBar)
            downloader.download()
            songName = downloader.getName()
            songName = songName.replace(',','').replace('.','')
            downloadedVideoPath = os.path.join(path, songName + '.mp4')

            # then convert it to mp3

            converter = ConverterToMp3(downloadedVideoPath, path)
            t = threading.Thread(target=self.convert,args=(downloadedVideoPath,path,songName,progressBarText))
            t.start()
            progressBarText.set('Converting to mp3')
            t.join()
        except Exception as e:
            progressBarText.set("Can't download")
            print(str(e))
        finally:
            t = threading.Thread(target=self.waitToDestroy,args=(progressBar,progressBarLabel))
            t.start()
            self.currentRow-=1

    def waitToDestroy(self,progressBar,label):
        time.sleep(5)
        progressBar.destroy()
        label.destroy()

    def convert(self,downloadedVideoPath,path,songName,progressBarText):
        converter = ConverterToMp3(downloadedVideoPath, path)
        converter.convert(songName)
        os.remove(downloadedVideoPath)
        progressBarText.set('Done')