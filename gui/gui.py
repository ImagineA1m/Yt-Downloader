from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube
import webbrowser

root = Tk()
root.geometry("1000x600")  #window size
root.title("PreTube : Download Videos Without Youtube Premium") #window title
background = "white" #background color
fg = "black" #foreground
text_color = "black" #text color
button_color = "#bdbdbd"
root.config(bg=background) # window color set to background
root.iconbitmap("images/Logo.ico")
download_btn = PhotoImage(file="images/PreTubeLogo.png/")
img_label = Label(image=download_btn, bg=background, height="190")
img_label.pack()
q = IntVar()


def start():
    question = messagebox.askquestion('Guide', 'Interested in viewing a guide on how to use this program?')
    if question == "yes":
        webbrowser.open_new("https://www.youtube.com/watch?v=CtkW9xBYzPc")
    else:
        return
    

def error():
    messagebox.showerror("PreTube Error", "Invalid Link (URL)")


def main():
    file_path = filedialog.askdirectory()

    choice = q.get()
    value = Input.get()

    if value == "" or "youtube" not in value:
        error()

    yt = YouTube(value)
    stream = None
    success = ""

    if choice == 1:
        stream = yt.streams.get_highest_resolution()
        stream.download(file_path)
        success = "High quality video downloaded"

    if choice == 2:
        stream = yt.streams.get_lowest_resolution()
        stream.download(file_path)
        success = "Low quality video downloaded"

    if choice == 3:
        stream = yt.streams.get_audio_only()
        stream.download(file_path)
        success = "Audio has been downloaded"

    if stream is not None:
        stream.download(file_path)
        messagebox.showinfo("Pre-tube", f"{success}")
        print(file_path)


Input = Entry(root, width=70, fg=text_color, borderwidth=2, relief="groove", bg="white", font="Arial 18")
button = Button(root, text="Download", fg=text_color, bg="red", borderwidth=0, command=main, font="YouTube-Sans-Bold 35")
choiceHigh = Radiobutton(root, text="High Quality (Slower) ", variable=q, value=1, height="1", bg=button_color, fg=fg, font="TravelSunday 19")
choiceLow = Radiobutton(root, text="Low Quality (Faster)", variable=q, value=2, height="1", bg=button_color, fg=fg, font="TravelSunday 19")
choiceAudio = Radiobutton(root,text="Audio Only (Offline Music)", variable=q, value=3, height="1", bg=button_color, fg=fg, font="TravelSunday 19")

Input.pack(pady=5,)
choiceHigh.pack(pady=10)
choiceLow.pack(pady=10)
choiceAudio.pack(pady=10)
button.pack(pady=60)

start()
root.mainloop()