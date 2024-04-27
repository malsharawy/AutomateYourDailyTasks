from pytube import YouTube
from sys import argv
from pytube import YouTube
import tkinter as tk


link = argv[1]
yt = YouTube(link)

print("title = ", yt.title)
print("Views = ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download(link)
print("Download Complete!!")

# Run the script
def download_video(link):

    yt = YouTube(link)

    print("title = ", yt.title)
    def download_video_gui():
        link = entry.get()
        yt = YouTube(link)
        
        title_label.config(text="Title: " + yt.title)
        views_label.config(text="Views: " + str(yt.views))
        
        yd = yt.streams.get_highest_resolution()
        yd.download()
        
        download_label.config(text="Download Complete!!")

    # Create the GUI window
    window = tk.Tk()
    window.title("YouTube Video Downloader")

    # Create the input entry
    entry = tk.Entry(window, width=50)
    entry.pack()

    # Create the download button
    download_button = tk.Button(window, text="Download", command=download_video_gui)
    download_button.pack()

    # Create the labels
    title_label = tk.Label(window, text="Title: ")
    title_label.pack()

    views_label = tk.Label(window, text="Views: ")
    views_label.pack()

    download_label = tk.Label(window, text="")
    download_label.pack()

    # Run the GUI
    window.mainloop()
    print("Views = ", yt.views)

    yd = yt.streams.get_highest_resolution()

    yd.download()
    print("Download Complete!!")

# Run the script
download_video("https://www.youtube.com/watch?v=9bZkp7q19f0")
# python main.py https://www.youtube.com/watch?v=9bZkp7q19f0
