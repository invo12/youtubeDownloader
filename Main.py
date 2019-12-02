from Downloader import *
def main():
    downloader = Downloader("https://www.youtube.com/watch?v=HUIllVCwWGU","D:\\music")
    downloader.download()

if __name__ == '__main__':
    main()