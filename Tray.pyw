from pystray import MenuItem as item
import pystray
from PIL import Image

def tray():
    def action():
        exit()
    image = Image.open("image.png")
    menu = (item('Help', action), item('Close', action))
    icon = pystray.Icon("name", image, "test", menu)
    icon.run()

tray()





    
    


    


  

    
    





