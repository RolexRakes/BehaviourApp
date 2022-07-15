ver = 2

import os
import urllib.request as urllib2
import pathlib
from pathlib import Path
from configparser import ConfigParser

import tkinter as tk
from tkinter import messagebox
from tkinter import *

config = ConfigParser()
config.read("configurations.ini")

print(config["username"]["username"])

window = tk.Tk()
window.geometry('900x500')
window.configure(bg='blue')
window.resizable(False, False)
window.attributes('-alpha', 0.0)
window.title("BETA: BehaviourApp")
# center window


def center_window(w=900, h=500):
    # get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
# center window


name = tk.Label(
    window,
    bg='blue',
    fg='white',
    font=('Helvetica', '32'),
    text='BehaviourApp'
)
name.pack(pady=(210, 0))

slogan = tk.Label(window,
                  bg='blue',
                  fg='lightgrey',
                  font=('Arial', '20'),
                  text="It's your lesson."
                  )
slogan.pack(pady=(5, 50))

count = 0.0


def fadein():
    global count
    count += 0.1

    if count > 0.9:
        window.attributes('-alpha', 1)

        global status_label
        status_label = tk.Label(window,
                                bg='blue',
                                fg='black',
                                font=('Arial', '20'),
                                text='Checking for updates...'
                                )
        status_label.pack(pady=(20, 0))

        window.after(1, checkupdates)

    else:
        window.attributes('-alpha', count)
        window.after(20, fadein)

def update():
    yesno = messagebox.askyesno("Update available", "There is a new version of BehaviourApp available. Do you want to update? (If you choose no, BehaviourApp will continue on version "+ str(ver) +")")
    if yesno == True:
        window.destroy()

        this_file = Path(__file__)
        file = this_file / ".." / "updater.pyw"
        os.startfile(file)

        exit()

    if yesno == False:
        window.after(1, main)

def checkupdates():
    global version
    verlink = urllib2.urlopen('Link to the latest version number')
    contents = verlink.read()

    this_file = Path(__file__)
    myfile = this_file / ".." / "version.txt"
    myfile.write_bytes(contents)

    this_file = Path(__file__)
    myfile = this_file / ".." / "version.txt"
    version = myfile.read_text()

    version = int(version)

    if ver == version:
        window.after(1, welcome)
    if ver != version:
        status_label['text'] = "Found update from version "+ str(ver) +" to version "+ str(version) +""
        window.after(1, update)

def welcome():
    status_label['text'] = "Welcome to BehaviourApp, "+ username +"!"
    window.after(2000, main)

def main():
    window.configure(bg='grey')

    status_label.destroy()
    slogan.destroy()
    name.destroy()


center_window(900, 500)
#
window.after(1, fadein)
#
window.mainloop()
