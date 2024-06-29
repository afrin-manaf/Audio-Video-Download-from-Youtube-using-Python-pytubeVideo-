from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_audio(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp3")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
    except Exception as e:
        print(e)

        url = "https://www.youtube.com/results?search_query=rick+roll "
        save_path = "C:/Users/User/Desktop/Sem 2/Projects/Downloader"

        download_audio(url, save_path)


