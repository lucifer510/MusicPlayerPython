from tkinter import filedialog
from tkinter import *
import pygame
import os

root = Tk()
root.title('Music Player')
root.geometry("500x400")

# Initialize Pygame Mixer
pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ""
paused = False
def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name,ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songList.insert("end", song)

    songList.selection_set(0)
    current_song = songs[songList.curselection()[0]]

def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory , current_song))
        pygame.mixer.music.play(loops=0)

    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global current_song, paused
    try:
        songList.selection_clear(0, END)
        songList.select_set(songs.index(current_song)+1)
        current_song = songs[songList.curselection()[0]]
        play_music()
    except:
        pass

def back_music():
    global current_song, paused
    try:
        songList.selection_clear(0, END)
        songList.select_set(songs.index(current_song)-1)
        current_song = songs[songList.curselection()[0]]
        play_music()
    except:
        pass


organize_menu = Menu(menubar,tearoff=0)
organize_menu.add_command(label="Select Folder", command=load_music)
menubar.add_cascade(label="Organize", menu=organize_menu)

# Create Playlist Box
songList = Listbox(root, bg="black", fg="green", width=100, height=20)
songList.pack()

play_btn_img = PhotoImage(file="play.png")
pause_btn_img = PhotoImage(file="pause.png")
next_btn_img = PhotoImage(file="next.png")
back_btn_img = PhotoImage(file="back.png")

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_img, borderwidth=0, command=play_music)
pause_btn = Button(control_frame, image=pause_btn_img, borderwidth=0, command=pause_music)
next_btn = Button(control_frame, image=next_btn_img, borderwidth=0, command=next_music)
back_btn = Button(control_frame, image=back_btn_img, borderwidth=0, command=back_music)

play_btn.grid(row=0, column=1, padx=10, pady=7)
pause_btn.grid(row=0, column=2, padx=10, pady=7)
next_btn.grid(row=0, column=3, padx=10, pady=7)
back_btn.grid(row=0, column=0, padx=10, pady=7)

root.mainloop()