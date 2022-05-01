import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound
import pygame
from pygame import mixer
import os
import time

PORT = 8050
IP_ADDRESS = '192.168.1.26'
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox = None
filePathLabel = None
infoLabel = None

global song_counter
song_counter = 0

for file in os.listdir('shared files'):
    filename = os.fsdecode(file)
    listbox.insert(song_counter, filename)
    song_counter = song_counter + 1


def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")


def openMusicWindow():

    print("\n\t\t\t\tIP MESSENGER")

   
    window=Tk()

    window.title('MUSIC WINDOW')
    window.geometry("500x350")
    window.configure(bg='LightSkyBlue')

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    selectlabel = Label(window, text= "Select A Song",bg='LightSkyBlue', font = ("Calibri",10))
    selectlabel.place(x=10, y=8)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox',bg='LightSkyBlue',borderwidth=2, font = ("Calibri",10))
    listbox.place(x=10, y=70)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton=Button(window,text="Play",width=10, bd=1,bg='LightSkyBlue', font = ("Calibri",10))
    playButton.place(x=30,y=200)

    Stop=Button(window,text="Stop",bd=1,width=10,bg='LightSkyBlue', font=("Calibri",10),command=stop)
    Stop.place(x=200,y=200)

    Upload=Button(window,text="Upload",width=10, bd=1,bg='LightSkyBlue', font = ("Calibri",10))
    Upload.place(x=30,y=250)

    Download = Button(window, text= "Download", width=10, bd=1,bg='LightSkyBlue',font = ("Calibri",10))
    Download.place(x=200, y=250)

    infoLabel = Label(window,text="", fg="blue",font = ("Calibri",10))
    infoLabel.place(x=4,y=280)

    resumeButton = Button(window, text="Resume", width=10, bd=1, bg="LightSkyBlue", font=("Calibri",10),command=resume)
    resumeButton.place(x=30,y=250)

    pauseButton = Button(window, text="Pause", width=10, bd=1, bg="LightSkyBlue", font=("Calibri",10),command=pause)
    pauseButton.place(z=200,y=250)

    window.mainloop()


def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()


def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()






def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

setup()
openMusicWindow()














