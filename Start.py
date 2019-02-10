import os
import keyboard
run = True
while run:
    os.startfile("Tray.pyw")
    if keyboard.is_pressed('ctrl + a'): 
        break

#Press ctrl + a to stop the while loop


