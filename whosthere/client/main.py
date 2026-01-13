from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from client.ui.menu import MainMenu
from client.ui.join_menu import JoinMenu
from client.ui.lobby_menu import LobbyMenu
from client.network.lobby_client import LobbyClient
import threading
from server.tcp_server import GameServer
from server.discovery_server import DiscoveryBroadcaster
from client.ui.lobby_menu import LobbyMenu

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
    def start_host(self, password):
        # Start TCP server
        self.server = GameServer(password)
        self.server.start()

        # Start LAN broadcast
        self.broadcaster = DiscoveryBroadcaster("Ashith's Game")
        threading.Thread(
            target=self.broadcaster.broadcast_loop,
            daemon=True
        ).start()

    # Host enters lobby as Player1
        self.clear_ui()
        self.lobby = LobbyMenu(self, is_host=True)
        self.lobby.update_players(["HOST"])

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
