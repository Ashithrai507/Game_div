from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from ui.menu import MainMenu

class GameApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()
        self.set_window_properties()

        # Current state
        self.menu = MainMenu(self)

    def set_window_properties(self):
        props = WindowProperties()
        props.setTitle("Multiplayer FPS")
        props.setSize(1280, 720)
        self.win.requestProperties(props)

app = GameApp()
app.run()
