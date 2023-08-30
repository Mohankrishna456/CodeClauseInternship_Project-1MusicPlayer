import tkinter as tk
import os
import fnmatch
from pygame import mixer

mixer.init()
canvas = tk.Tk()
canvas.geometry('800x700')
canvas.title('Music Player')
canvas.iconbitmap("C:\\Users\\bhamm\\Desktop\\music.ico")
canvas.config(bg = "Blue")

# rootpath = "C:\\Users\\bhamm\\Pictures\\savedmusic"
rootpath = "C:\\Users\\bhamm\\Desktop\\MusicPlayer\\saved music"
pattern = "*.mp3"

def select():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath + '\\' + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear("active")
def play_nxt():
    next_song =listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + '\\' + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.selection_set(next_song)

def play_prev():
    next_song =listBox.curselection()
    next_song = next_song[0] -  1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + '\\' + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.selection_set(next_song)
def pause_play():
    if pauseBut["text"] == "Pause":
        mixer.music.pause()
        pauseBut["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseBut["text"] = "Pause"

listBox = tk.Listbox(canvas, fg = "red", bg = "Yellow", width = 100)
listBox.pack(padx = 15, pady = 15)
label = tk.Label(canvas, text=" ", fg="Brown", bg="magenta", font=("Courier", 8))
label.pack(pady = 15)


for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert("end",filename)



tik = tk.Frame(canvas, bg="Black")
tik.pack(padx = 10, pady = 5, anchor = 'center')

prev = tk.Button(canvas, borderwidth = 0, text = "Prev", bg = "yellow", command = play_prev)
prev.pack(pady = 15, in_ = tik, side = 'left')
stopbutton =  tk.Button(canvas, borderwidth = 0, text = "Stop", bg = "red", command = stop)
stopbutton.pack(pady = 15, in_ = tik, side = 'left')
play = tk.Button(canvas, borderwidth = 0, text = "Play", bg = "green", command = select)
play.pack(pady = 15, in_ = tik, side = 'left')
pauseBut = tk.Button(canvas, borderwidth = 0, text = "Pause", bg = "chartreuse", command = pause_play)
pauseBut.pack(pady = 15, in_ = tik, side = 'left')
next = tk.Button(canvas, borderwidth = 0, text = "Next", bg = "coral", command = play_nxt )
next.pack(pady = 15, in_ = tik, side = 'left')
canvas.mainloop()
