
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


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096
def musicWindow():

   
    print("\n\t\t\t\t MUSIC PLAYER")

    #Client GUI starts here

    
    window=Tk()

    window.title('music window')
    window.geometry("500x350")
    window.configure(bg='lightSkyBlue')

    
    
    
    global listbox
    selectLabel = Label(window, text= "Select Song", bg="lightSkyBlue",font = ("Calibri",8))
    selectLabel.place(x=2, y=1)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox', bg="lightSkyBlue",borderwidth=2,font = ("Calibri",10))
    listbox.place(x=10, y=18)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton=Button(window,text="play",width=10,bd=1,bg="skyBlue", font = ("Calibri",10),command=play)
    playButton.place(x=30,y=200)

    stopButton=Button(window,text="stop",width=10,bd=1,bg="skyBlue", font = ("Calibri",10),command=stop)
    stopButton.place(x=200,y=200)

    Upload=Button(window,text="upload",width=10,bd=1,bg="skyBlue", font = ("Calibri",10))
    Upload.place(x=30,y=250)

    Download=Button(window,text="download",width=10,bd=1,bg="skyBlue", font = ("Calibri",10))
    Download.place(x=200,y=250)

    infoLabel = Label(window, text= "",fg= "blue", font = ("Calibri",8))
    infoLabel.place(x=4, y=200)

   

    window.mainloop()


def handleShowList(client):
    global listbox
    global clients
    song_counter=0
    for file in os.listdir('shared_files'):
        filename=os.fsdecode(file)
        listbox.insert(song_counter,filename)
        song_counter+=1
def stop():
    global infoLabel
    global song_selected
    
 
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")
   
def play():
    global infoLabel
    global song_selected
    song_selected=listbox.get(ANCHOR)
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected!=""):
        infoLabel.configure(text="NOW PLAYING:"+song_selected)
    else:
        infoLabel.configure(text="")
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

   
    musicWindow()

setup()


