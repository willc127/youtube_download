import tkinter as tk
from tkinter import StringVar, Radiobutton
from audio import download_audio
from video import download_video

def create_app():
    app = tk.Tk()
    app.title("Youtube Downloader")
    app.geometry("500x250")
    app.configure(background="#e80714")
    app.resizable(False, False)

    # Create a variable to store the selected option
    selected_option = StringVar(app)
    selected_option.set("Video")  # Set the default option

    # Add a button to download based on the selected option
    def download():
        link = link_entry.get()
        if selected_option.get() == "Video":
            download_video(link)
        elif selected_option.get() == "Audio":
            download_audio(link)
        tk.Label(app, text="Download concluído!", font=("Arial", 15), background="#e80714", foreground="white").pack()

    # Create and pack widgets
    create_widgets(app, selected_option, download)

    app.mainloop()

def create_widgets(app, selected_option, download_callback):
    tk.Label(
        app,
        text="Youtube URL: ",
        font=("Arial", 18, "bold"),
        foreground="white",
        background="#e80714"
    ).pack()

    global link_entry  # Declare link_entry as global to access it in the download function
    link_entry = tk.Entry(app, width=40, font=("Arial", 15))
    link_entry.pack()

    # Create the radio buttons
    radio_video = Radiobutton(
        app,
        text="Vídeo",
        font=("Arial", 15, "bold"),
        variable=selected_option,
        value="Video",
        background="#e80714",
        foreground="white",
        selectcolor="#e80714"
    )
    radio_video.pack()

    radio_audio = Radiobutton(
        app,
        text="Áudio",
        font=("Arial", 15, "bold"),
        variable=selected_option,
        value="Audio",
        background="#e80714",
        foreground="white",
        selectcolor="#e80714"
    )
    radio_audio.pack()

    # Add a button to download
    download_button = tk.Button(
        app, text="Download", background="white", font=("Arial", 15), command=download_callback
    )
    download_button.pack()

if __name__ == "__main__":
    create_app()