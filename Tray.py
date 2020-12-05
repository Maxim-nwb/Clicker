import pystray
from PIL import Image


class Tray():
    def __init__(self):
        # image for tray
        self._image = Image.open("tap.ico")
        # create
        self._menu = {pystray.MenuItem("Deploy", self.deploy)}
        self._icon = pystray.Icon(name ="Cliker", icon = self._image, title ="Cliker", menu = self._menu)
        # variable for determining the tray status
        self._status = True
    # run tray
    def run(self):
        self._icon.run()
    # stop tray return control main window
    def deploy(self):
        self._icon.stop()
        self._status = False