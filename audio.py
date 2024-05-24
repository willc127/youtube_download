from pytube import YouTube
import moviepy.editor as mp
import re
import os


def download_audio(link: str):
    path = "Arquivos_audio"
    yt = YouTube(link)
    # Fazer o dowload
    ys = yt.streams.filter(only_audio=True).first().download(path)
    # Converter o video(mp4) para mp3
    for file in os.listdir(
        path
    ):  # For para percorrer dentro da pasta passada anteriormente
        if re.search("mp4", file):  # If verificando se o arquivo e .MP4
            mp4_path = os.path.join(
                path, file
            )  # Cria uma variavel para armazenar o arquivo .MP4
            mp3_path = os.path.join(
                path, os.path.splitext(file)[0] + ".mp3"
            )  # Variavel que cria o nome do arquivo e adiciona .MP3 ao final
            new_file = mp.AudioFileClip(mp4_path)  # Cria o arquivo de áudio (.MP3)
            new_file.write_audiofile(
                mp3_path
            )  # Renomeia o arquivo, setando o nome criado anteriormente
            os.remove(mp4_path)  # Remove o arquivo .MP4
