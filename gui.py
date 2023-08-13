from tkinter import *
from tkinter import messagebox
from pytube import YouTube
root = Tk()
root.geometry("1000x600") #window size
root.title("PreTube : Download Videos Without Youtube Premium") #window title
root.iconbitmap("Logo.ico") #window logo
background = "#4a5459" #background color
clr = "#899ca5" #foreground
text_color = "#d4d2d1" #text color
root.config(bg=background) # window color set to background

download_btn = PhotoImage(file="ytlogo.png")


img_label = Label(image=download_btn , bg=background, height="190")
img_label.pack()
q = IntVar()


def error():
    messagebox.showerror("PreTube Error", "Invalid Link (URL)")


def test():
    choice = q.get()
    value = Input.get()

    if value == "" or "youtube" not in value:
        error()

    if choice == 1:
        yt = YouTube(value)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        success = Label(root, text="Success It's Downloaded", fg="green")
        success.pack()
        
    if choice == 2:
        yt = YouTube(value)
        stream = yt.streams.get_lowest_resolution()
        stream.download()
        success = Label(root, text="Success It's Downloaded", fg="green")
        success.pack()

    if choice == 3:
        yt = YouTube(value)
        stream = yt.streams.get_audio_only()
        stream.download()
        success = Label(root, text="Success It's Downloaded", fg="green")
        success.pack()
    

Input = Entry(root, width=70,fg = text_color, bg=clr, font="Helvetica 19")
button = Button(root, text="Download", fg=background, bg=clr, command=test, font="Arial 19")
choiceHigh = Radiobutton(root, text="High Quality (Slower) ", variable=q, value=1, height="3", bg=background, fg=clr,font="Arial 19")
choiceLow = Radiobutton(root, text="Low Quality (Faster)", variable=q, value=2, height="3" , bg=background, fg=clr,font="Arial 19")
choiceAudio = Radiobutton(root,text="Audio Only (Offline Music)", variable=q, value=3,height="3", bg=background, fg=clr,font="Arial 19")
Input.pack()
choiceHigh.pack()
choiceLow.pack()
choiceAudio.pack()
button.pack()

root.mainloop()
