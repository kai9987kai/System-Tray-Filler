import os
import keyboard
from tkinter import *
from tkinter import ttk
import threading
def startthread():
    x1 = threading.Thread(target=Start, daemon=True)
    x1.start()  
def Start():
    run = True
    while run:
        os.startfile("Tray.pyw")
        if keyboard.is_pressed('ctrl + a'):
            break
def ExitButton():
    exit(0)
def mainthread(): 
    window = Tk()
    button = ttk.Button(window, text="Start", command = startthread)
    button2 = ttk.Button(window, text="EXIT - STOP SCRIPT", command = ExitButton)
    button.pack()
    button2.pack()
    ttk.Label(window, text="""The emergency fail safe key
        combo is ctrl + a""", anchor=E).pack()
    window.title("Windows Tray Filler")
    try:
        window.iconbitmap('favicon.ico')
    except:
        pass
    window.resizable(False, False)
    window.mainloop()
mainthread()
