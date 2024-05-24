from pytube import YouTube
import tkinter as tk

def download_video(link: str):
    path = "Arquivos_video"
    yt = YouTube(url = link)
    yt.streams.filter(progressive=True, file_extension="mp4").order_by(
        "resolution"
    ).desc().first().download(path)
