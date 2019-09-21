from pystray import MenuItem as item
import pystray
from PIL import Image
import webbrowser
def tray():
    def action():
        exit(0)
    def helppage():
        webbrowser.open_new(r"https://github.com/kai9987kai/System-Tray-Filler/wiki")
    image = Image.open("image.png")
    menu = (item('Help', helppage), item('Close', action))
    icon = pystray.Icon("name", image, "test", menu)
    icon.run()

tray()
