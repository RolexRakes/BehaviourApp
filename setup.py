print("BehaviourApp")

print()
print("DISCLAIMER:")
print()
print("By using BehaviourApp in it's beta stage you acknowledge that:")
print()
print("BehaviourApp is not in it's final stage and is only in beta testing.")
print("BehaviourApp is not liable for negligent missuse, faults, loss of data or consequential damage.")
print("Many things about this program may change in the future.")
print("Please give feedback to the creator of this app about what you like and don't like.")
print()
input("Press enter to acknowledge this statement and start GUI")
print()
print("One moment...")

global perms
import os
import time
import urllib.request as urllib2
import pathlib
from pathlib import Path

import tkinter as tk
from tkinter import messagebox
from tkinter import *

def setup_finished():
    pass

height = 70
pad = 10

global animatewelcomerun
print("Starting user GUI")
window = tk.Tk()
window.geometry('900x500')
window.configure(bg='darkblue')
window.resizable(False, False)
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

#
#

def agreetos():

    count = 0
    height = 70

    # ANIMATION TIMMEEE
    global setup_finished
    window.after(10, setup_finished_animation)
    setup_finished = "yes"

setup_frame = tk.Frame(window, bg='lightgrey', width=800, height=360)

frame_3 = tk.Frame(setup_frame, bg='darkgrey', width=250, height=90)
frame_2 = tk.Frame(setup_frame, bg='black', width=250, height=40)

tos_label = tk.Label(frame_3, height=1, bg='darkgrey', fg='white', font=(
    'Helvetica', '10'), text="By clicking 'I agree' you agree that you have read and acknowledged BehaviourApp's Terms of Service.")
agree_button = tk.Button(frame_3, text="I agree", width=30, height=2, bg="grey", fg="white", command=agreetos)

#
#

window.title("BETA: BehaviourApp - Setup")

count = 0
padwhy = 130

ran = "no"
frame_max_h = "no"
sl3_made = "no"
entry_made = "no"
widgets_destroyed = "no"


def animatelabel():
    global count, padwhy, ran, frame_max_h, sl3_made, setup_label_3, entry_made, entry
    if count < 109:
        padwhy -= 1
        count += 1

        if frame_max_h == "yes":
            pass
        else:
            try:
                setup_frame_2.pack(pady=(padwhy, 0))
            except Exception:
                frame_max_h = "yes"

        window.after(5, animatelabel)

    if count > 108:
        if ran == "yes":
            pass
        else:
            ran = "yes"

            if sl3_made == "yes":
                pass
            else:
                setup_label_3 = tk.Label(setup_frame, height=1, bg='lightgrey', fg='black', font=(
                    'Helvetica', '20'), text="What would you like BehaviourApp to call you?")
                setup_label_3.pack(pady=(60, 0), side=tk.TOP)
                sl3_made = "yes"

            if entry_made == "yes":
                pass
            else:
                entry = tk.Entry(
                    setup_frame, fg="black", bg="white", width=50, justify='center', font=('Arial 20'))
                entry.pack(pady=(30, 0), padx=10)
                entry_made = "yes"

                entry.focus()

            count = 0
            ran = "no"

def submit(event):
    global setup_label_3, newusername
    newusername = entry.get()
    entry.destroy()
    setup_label_3.destroy()

    frame_2.pack(fill='x')
    frame_2.pack_propagate(0)

    setup_label_3 = tk.Label(frame_2, height=1, bg='black', fg='white', font=(
        'Helvetica', '13'), text="Welcome to BehaviourApp, " + newusername + ".")
    setup_label_3.pack(pady=(7, 0))

    perm_label = tk.Label(setup_frame, height=1, bg='lightgrey', fg='black', font=(
        'Helvetica', '16'), text="BehaviourApp needs you to agree with the Terms of Service for the next part.")
    perm_label.pack(pady=(20, 0), side=tk.TOP)

    opentos_button = tk.Button(setup_frame, text="Open Terms of Service",
                                width=30, height=2, bg="blue", fg="yellow", command=opentos)
    opentos_button.pack(pady=(30, 0))

def opentos():
    this_file = Path(__file__)
    tos = this_file / ".." / "Legal" / "ToS.txt"
    os.startfile(tos)

    frame_3.pack(fill='x', pady=(10, 0))
    frame_3.pack_propagate(0)

    tos_label.pack(pady=(10, 0), side=tk.TOP)

    agree_button.pack(pady=(5, 0))

frame_1 = tk.Frame(window, bg='blue', width=250, height=70)
frame_1.pack(side=tk.TOP, fill='x')
frame_1.pack_propagate(0)

label_top = tk.Label(frame_1, bg='blue', fg='white', font=(
    'Helvetica', '32'), text='BehaviourApp')
label_top.pack(pady=(10, 0))

setup_label = tk.Label(window, bg='darkblue', fg='lightgreen', font=(
    'Helvetica', '20'), text='Setup')
setup_label.pack(pady=(10, 0), side=tk.TOP)

setup_frame.pack(pady=(10, 0))
setup_frame.pack_propagate(0)

setup_frame_2 = tk.Frame(setup_frame, bg='grey', width=800, height=130)
setup_frame_2.pack(pady=(130, 0), fill='x')
setup_frame_2.pack()

setup_label_2 = tk.Label(setup_frame_2, bg='grey', fg='white', font=(
    'Helvetica', '20'), text='Welcome to BehaviourApp!')
setup_label_2.pack(pady=(10, 0), side=tk.TOP)

setup_label_3 = tk.Label(setup_frame_2, bg='grey', fg='lightgrey', font=(
    'Helvetica', '15'), text="Let's get you setup.")
setup_label_3.pack(pady=(10, 0), side=tk.TOP)
    

def setup_finished_animation():
    global widgets_destroyed

    if setup_finished == "yes":
        if widgets_destroyed == "yes":
            pass
        if widgets_destroyed == "no":
            yesno = messagebox.askyesno("Permission needed", "BehaviourApp will be installed in the BehaviourApp Data folder on your device/user drive. Are you okay with this?")

            if yesno == False:
                window.destroy()
                exit()

            setup_label.destroy()
            setup_frame.destroy()
            frame_1.destroy()

            ba_label = tk.Label(window, bg='blue', fg='white', font=('Helvetica', '32'), text='BehaviourApp')
            ba_label.pack(pady=(210, 0))

            window.configure(bg='blue')
            widgets_destroyed = "yes"

        time.sleep(0.7)

        label_bottom = tk.Label(window, bg='blue', fg='lightgrey', font=('Arial', '20'), text='Thanks for choosing BehaviourApp!')
        label_bottom.pack(pady=(5, 50))

        def one():
            global status_label

            status_label = tk.Label(window,
                                    bg='blue',
                                    fg='black',
                                    font=('Arial', '20'),
                                    text='Downloading and installing BehaviourApp and sub-programs...'
                                    )
            status_label.pack(pady=(20, 0))

            window.after(1, updrestart)

        def updrestart():  
            def restart():
                this_file = Path(__file__)
                tos = this_file / ".." / "BehaviourApp.pyw"
                os.startfile(tos)

                window.destroy()
                exit()
                

            def second():
                applink = urllib2.urlopen('https://drive.google.com/u/2/uc?id=1DmdKVNgoI01X1eKExGHzRMNnT7wcFTQu&export=download&confirm=t&uuid=65f53607-95fa-4ae8-9360-a4182b2b6e15')
                contents = applink.read()

                this_file = Path(__file__)
                myfile = this_file / ".." / "BehaviourApp.pyw"
                myfile.write_bytes(contents)

                applink2 = urllib2.urlopen('https://drive.google.com/u/2/uc?id=15XKyEGaEsPoFDigcTju5OL2zgXUpGEkA&export=download&confirm=t&uuid=82b70616-a105-4d32-a741-80c3f1c60906')
                contents = applink2.read()

                this_file = Path(__file__)
                myfile = this_file / ".." / "updater.pyw"
                myfile.write_bytes(contents)

                window.after(1, finished)

            def finished():
                status_label['text'] = 'Finished all tasks successfully.'

                restarting_label = tk.Label(window,
                                    bg='blue',
                                    fg='black',
                                    font=('Arial', '15'),
                                    text='Starting BehaviourApp...'
                                    )
                restarting_label.pack(pady=(10, 0))
                
                window.after(1, restart)

            this_file = Path(__file__)
            myfile = this_file / ".." / "username.txt"
            myfile.write_text(newusername)

            verlink = urllib2.urlopen('https://drive.google.com/u/2/uc?id=19js8ABpL7aM_WsQSGHSdqnrApdcGYdQa&export=download')
            contents = verlink.read()

            this_file = Path(__file__)
            myfile = this_file / ".." / "version.txt"
            myfile.write_bytes(contents)


            window.after(1, second)

        window.after(1, one)


window.bind('<Return>', submit)
window.after(2500, animatelabel)
window.after(10, setup_finished_animation)
center_window(900, 500)
window.mainloop()
