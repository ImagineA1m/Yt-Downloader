from tkinter import *
from tkinter import messagebox
from pytube import YouTube
root = Tk()
root.geometry("1000x600")  #window size
root.title("PreTube : Download Videos Without Youtube Premium") #window title
root.iconbitmap("Logo.ico") #window logo
background = "white" #background color
fg = "#333" #foreground
text_color = "black" #text color
button_color = "red"
root.config(bg=background) # window color set to background
download_btn = PhotoImage(file="PreTubeLogo.png")
img_label = Label(image=download_btn , bg=background, height="190")
img_label.pack()
q = IntVar()
def error():
    messagebox.showerror("PreTube Error", "Invalid Link (URL)")


def main():
    choice = q.get()
    value = Input.get()

    if value == "" or "youtube" not in value:
        error()

    yt = YouTube(value)
    stream = None
    success = ""

    if choice == 1:
        stream = yt.streams.get_highest_resolution()
        stream.download()
        success = "High quality video downloaded"

    if choice == 2:
        stream = yt.streams.get_lowest_resolution()
        stream.download()
        success = "Low quality video downloaded"

    if choice == 3:
        stream = yt.streams.get_audio_only()
        success = "Audio has been downloaded"

    if stream is not None:
        stream.download()
        successlabel = Label(root, text="Success : " + success)
        successlabel.pack()


Input = Entry(root, width=70, fg = text_color, borderwidth=2,relief="groove", bg="white", font="Arial 18" )
button = Button(root, text="Download", fg=text_color, bg="red", borderwidth=0, command=main, font="YouTube-Sans-Bold 30")
choiceHigh = Radiobutton(root, text="High Quality (Slower) ", variable=q, value=1, height="1", bg=button_color, fg=fg,font="Arial 19")
choiceLow = Radiobutton(root, text="Low Quality (Faster)", variable=q, value=2, height="1" , bg=button_color, fg=fg,font="Arial 19")
choiceAudio = Radiobutton(root,text="Audio Only (Offline Music)", variable=q, value=3,height="1", bg=button_color, fg=fg,font="Arial 19")

Input.pack(pady=5,)
choiceHigh.pack(pady=10)
choiceLow.pack(pady=4)
choiceAudio.pack(pady=4)
button.pack(pady=4)

root.mainloop()
