import pystray
from PIL import Image


class Tray():
    def __init__(self):
        # image for tray
        self._image = Image.open("tap.ico")
        # create
        self._menu = {pystray.MenuItem("Deploy", self.deploy)}
        self._icon = pystray.Icon(name ="Cliker", icon = self._image, title ="Cliker", menu = self._menu)
    def run(self):
        self._icon.run()
    def deploy(self):
        pass