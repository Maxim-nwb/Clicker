import pystray
from PIL import Image


class Tray():
    def __init__(self):
        # image for tray
        self._image = Image.open("tap.ico")
        # create
        self._menu = (pystray.MenuItem("Deploy", self.deploy), pystray.MenuItem("Save", self.save))
        self._icon = pystray.Icon(name ="Cliker", icon = self._image, title ="Cliker", menu = self._menu)
        # variable for determining the tray status
        self._status = None
    # run tray
    def run(self):
        self._status = "RUN"
        self._icon.run()
    # stop tray return control main window
    def deploy(self):
        self._status = "STOP"
        self._icon.stop()

    def save(self):
        self._status = "SAVE"
        self._icon.stop()