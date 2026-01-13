from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from client.ui.menu import MainMenu
from client.ui.join_menu import JoinMenu
from client.ui.lobby_menu import LobbyMenu
from client.network.lobby_client import LobbyClient

class GameApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.disableMouse()
        self.set_window_properties()
        self.show_main_menu()

    def set_window_properties(self):
        props = WindowProperties()
        props.setTitle("Multiplayer FPS")
        props.setSize(1280, 720)
        self.win.requestProperties(props)

    def show_lobby(self, sock):
        self.clear_ui()
        self.lobby = LobbyMenu(self)
        LobbyClient(sock, self.lobby.update_players)

        
    def show_main_menu(self):
        self.clear_ui()
        self.menu = MainMenu(self)

    def show_join_menu(self):
        self.clear_ui()
        self.join_menu = JoinMenu(self)

    def clear_ui(self):
        if hasattr(self, "menu"):
            self.menu.frame.destroy()
        if hasattr(self, "join_menu"):
            self.join_menu.frame.destroy()

app = GameApp()
app.run()
