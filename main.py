from tkinter import *
import winsound
import tkinter.font as font


def stop_playing():
    top.destroy()


def select_item(event):
    global selected_wav_file  # this is a global variable (a .wav filename which I can pass into
    # the play_audio function when I select a .wav file)
    index = playList.curselection()[0]
    selected_wav_file = playList.get(index)
    # pass the selected_wav_file in to play_audio to play upon selecting it and play the sound
    play_audio_1(selected_wav_file)


def play_audio_1(filename):
    winsound.PlaySound(filename, winsound.SND_ASYNC)


top = Tk()
top.title("my sound List")
playList = Listbox(top, height=8, width=50)
# Bind Listbox to select_item function
playList.bind("<<ListboxSelect>>", select_item)
playList.insert(1, "meowing_1.wav")
playList.insert(2, "mooing.wav")
playList.insert(3, "fireworks.wav")
playList.insert(4, "train.wav")
playList.insert(5, "dogbarking_1.wav")
playList.insert(6, "clapping.wav")
playList.insert(6, "carspeeding.wav")


playList.pack()

# stop playing button
myFont = font.Font(family='Courier', size=20, weight='bold')

stop_playing_btn = Button(top, text="Stop Playing", width=16, command=stop_playing, bg='#0052cc', fg='#ffffff')

stop_playing_btn.place(x=25, y=100)
stop_playing_btn['font'] = myFont
stop_playing_btn.pack()

top.mainloop()

