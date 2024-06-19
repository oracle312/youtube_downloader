
import os
from pytube import YouTube, exceptions
from tkinter import *
from time import time

for i in os.listdir(os.getcwd()):
    if i == "downloads":
        break
    else:
        os.mkdir("downloads")
        
# Download video
def VideoDownload(entry_field):
    try:
        start_time = time()
        download_location = "downloads/"
        YouTube(entry_field).streams.first().download(download_location)
        end_time = time()
        
        window = Tk()
        window.title("Download Status")
        window.resizable(False, False)
        window.geometry("150x80")
        window.grid_columnconfigure(0, weight=1)
        window.grid_rowconfigure((0,1), weight=1)
        msg = StringVar()
        msg.set(f"다운로드 성공 !!\n소요시간 : {round(end_time-start_time,3)} 초")
        label =  Label(window, text=msg.get())
        label.grid(row=0, column=0)
        button = Button(window, text="확인", command=window.destroy)
        button.grid(row=1, column=0)
        window.mainloop()

    except exceptions.RegexMatchError:
        error = Tk()
        error.title("Error")
        error.resizable(False, False)
        error.geometry("150x50")
        error.grid_rowconfigure((0,1), weight=1)
        error.grid_columnconfigure(0, weight=1)
        error_label = Label(error, text="유효한 주소를 넣어주세요")
        error_label.grid(row=0, column=0)
        button = Button(error, text="확인", command=error.destroy)
        button.grid(row=1, column=0)
        error.mainloop()
        
main = Tk()
main.title("유튜브 다운로더")
main.grid_rowconfigure((0,1),weight=1)
main.grid_columnconfigure((0,1),weight=1)
main.geometry("350x50")
main.resizable(False, False)
Label(main, text="유튜브 영상 주소 : ").grid(row=0,column=0)
entry = Entry(main)
entry.grid(row=0,column=1)
Button(main, text="다운로드", command=lambda *args: VideoDownload(entry.get())).grid(row=0, column=2)
main.mainloop()
    
    

 