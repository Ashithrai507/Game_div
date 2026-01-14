import threading
import socket

from panda3d.core import getModelPath
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

# UI
from client.ui.menu import MainMenu
from client.ui.join_menu import JoinMenu
from client.ui.lobby_menu import LobbyMenu

# Server & Networking
from server.tcp_server import GameServer
from server.discovery_server import DiscoveryBroadcaster
from client.network.tcp_client import try_join
from client.network.lobby_client import LobbyClient

from client.ui.countdown import Countdown
from client.game.fps_scene import FPSScene

class GameApp(ShowBase):
    def __init__(self):
        getModelPath().appendDirectory("client/assets")
        ShowBase.__init__(self)

        self.disableMouse()
        self.set_window_properties()

        self.menu = None
        self.join_menu = None
        self.lobby = None

        self.show_main_menu()

    # -----------------------------
    # Window setup
    # -----------------------------
    def set_window_properties(self):
        props = WindowProperties()
        props.setTitle("Multiplayer FPS")
        props.setSize(1280, 720)
        self.win.requestProperties(props)

    # -----------------------------
    # UI State Management
    # -----------------------------
    def clear_ui(self):
        if self.menu:
            self.menu.frame.destroy()
            self.menu = None

        if self.join_menu:
            self.join_menu.frame.destroy()
            self.join_menu = None

        if self.lobby:
            self.lobby.frame.destroy()
            self.lobby = None

    def show_main_menu(self):
        self.clear_ui()
        self.menu = MainMenu(self)

    def show_join_menu(self):
        self.clear_ui()
        self.join_menu = JoinMenu(self)

    def show_lobby(self, sock, is_host=False):
        self.clear_ui()
        self.lobby = LobbyMenu(self, is_host=is_host)

        LobbyClient(
            sock,
            self.lobby.update_players,
            self.start_countdown
        )

    def start_countdown(self):
        self.clear_ui()
        Countdown(self, self.start_game_scene)

    def start_game_scene(self):
        FPSScene(self)
    # -----------------------------
    # HOST GAME FLOW
    # -----------------------------
    def start_host(self, password):
        """
        Called after host enters numeric password
        """

        # 1️⃣ Start TCP server
        self.server = GameServer(password)
        self.server.start()

        # 2️⃣ Start LAN broadcast
        self.broadcaster = DiscoveryBroadcaster("Ashith's Game")
        threading.Thread(
            target=self.broadcaster.broadcast_loop,
            daemon=True
        ).start()

        # 3️⃣ Host connects to its OWN server via TCP
        hostname = socket.gethostname()
        sock = try_join("127.0.0.1", password, hostname)

        if not sock:
            print("Host failed to join its own server")
            return

        # 4️⃣ Enter lobby (host = true)
        self.show_lobby(sock, is_host=True)


# -----------------------------
# Run App
# -----------------------------
app = GameApp()
app.run()
