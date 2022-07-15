import os
import urllib.request as urllib2
import pathlib
from pathlib import Path

import tkinter as tk
from tkinter import *

padxl = 700
padxr = 0

window = tk.Tk()
window.geometry('800x250')
window.configure(bg='grey')
window.resizable(False, False)
window.title("Updater")
# center window

def center_window(w=800, h=250):
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
    bg='grey',
    fg='black',
    font=('Helvetica', '30'),
    text='BehaviourApp updater'
)
name.pack(pady=(10, 0))

frame = tk.Frame(window, bg='darkgrey', width=500, height=120)
frame.pack(pady=(20, 0))
frame.pack_propagate(0)

label = tk.Label(
    frame,
    bg='darkgrey',
    fg='black',
    font=('Helvetica', '30'),
    text='One moment...'
)
label.pack(pady=(10, 0))

label_2 = tk.Label(
    frame,
    bg='darkgrey',
    fg='grey',
    font=('Helvetica', '15'),
    text="This won't take long"
)
label_2.pack(pady=(30, 0))

loading_frame = tk.Frame(window, bg='lightgrey', width=800, height=15)
loading_frame.pack(fill='x', side=tk.BOTTOM)
loading_frame.pack_propagate(0)

loading_frame_2 = tk.Frame(loading_frame, bg='lightgreen', width=100, height=15)
loading_frame_2.pack(padx=(0, 700))
loading_frame_2.pack_propagate(0)

def anim():
    global padxl, padxr

    if padxl < 701 and padxl > 0:
        padxl -= 20

    if padxl == 0:
        if padxr != 700:
            padxr += 5
        if padxr > 701:
            padxl = 700
            padxr = 0

    if padxr < 701 and padxr > 0:
        padxr += 20

    loading_frame_2.pack(padx=(padxr, padxl))
    window.after(10, anim)

def update():
    applink = urllib2.urlopen('Link to latest BehaviourApp .pyw file')
    contents = applink.read()

    this_file = Path(__file__)
    myfile = this_file / ".." / "BehaviourApp.pyw"
    myfile.write_bytes(contents)

    verlink = urllib2.urlopen('Link to the version number')
    contents = verlink.read()

    this_file = Path(__file__)
    myfile = this_file / ".." / "version.txt"
    myfile.write_bytes(contents)

    window.after(1, startapp)

def exit():
    window.destroy()
    exit()

def startapp():
    this_file = Path(__file__)
    app = this_file / ".." / "BehaviourApp.pyw"
    os.startfile(app)

    window.after(1000, exit)



center_window(800, 250)

window.after(1, update)
window.after(1, anim)

window.mainloop()
