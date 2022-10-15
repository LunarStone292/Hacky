import os

try:
    import pytube
    from pytube import Playlist
    os.system("cls")
except:
    dd = os.system("pip3 install pytube")
    if(dd == 1):
        dd2 = os.system("pip install pytube")
        if(dd2 == 1):
            print("\n Error")
        else:
            print("")
    else:
        print("")

def youtube_download():
    print("\n\n 1. Download a video")
    print(" 2. Download a playlist")
    scelta = int(input("\n PyTube => "))
    if(scelta == 1):
        url = input(" Enter the Youtube url: ")
        try:
            yt = pytube.YouTube(url)
        except:
            print(" Error")
            exit()
        print("\n")
        print(' Title:', yt.title)
        print(' Author:', yt.author)
        print(' Published date:', yt.publish_date.strftime("%Y-%m-%d"))
        print(' Number of views:', yt.views)
        print(' Length of video:', yt.length, 'seconds')
        print("\n Downloading the Video...")
        try:
            yt.streams.get_highest_resolution().download()
            os.system(f'''move "{yt.title}" downloads''')
            print("\n Done.")
        except:
            print("\u001b[37m Error")
            exit()
    elif(scelta == 2):
        urlP = input("\n Enter the Youtube Playlist url: ")
        p = Playlist(f'{urlP}')
        print(f'\n Downloading: {p.title}')
        print('\n Number of videos in playlist: %s' % len(p.video_urls))
        for video in p.videos:
            audioStream = video.streams.get_by_itag('140')
            audioStream.download('downloads')
        print("\n Done.")
youtube_download()