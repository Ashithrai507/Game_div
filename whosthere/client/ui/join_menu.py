from direct.gui.DirectGui import DirectFrame, DirectButton, DirectLabel
from panda3d.core import TextNode
from client.network.discovery_client import DiscoveryClient

class JoinMenu:
    def __init__(self, app):
        self.app = app
        self.games = {}  # key: ip, value: game info
        self.buttons = {}

        # Root frame
        self.frame = DirectFrame(
            frameColor=(0.05, 0.05, 0.05, 1),
            frameSize=(-1.3, 1.3, -1, 1)
        )

        # Title
        self.title = DirectLabel(
            text="JOIN GAME",
            scale=0.1,
            pos=(0, 0, 0.7),
            parent=self.frame,
            text_fg=(1, 1, 1, 1),
            text_align=TextNode.ACenter
        )

        # Back button
        self.back_btn = DirectButton(
            text="BACK",
            scale=0.06,
            pos=(-1.1, 0, -0.85),
            parent=self.frame,
            command=self.go_back
        )

        # Start LAN discovery
        self.discovery = DiscoveryClient(self.on_game_found)
        self.discovery.start()

        # UI update task
        self.update_task = self.app.taskMgr.add(
        self.update_ui_task, "update-join-ui")


    def on_game_found(self, game):
        """
        Called from discovery thread.
        Store data only — no UI work here.
        """
        self.games[game["ip"]] = game

    def update_ui_task(self, task):
        """
        Runs in Panda3D main thread.
        Safe place to update UI.
        """
        y = 0.4
        for ip, game in self.games.items():
            if ip not in self.buttons:
                btn = DirectButton(
                    text=f'{game["host"]}  ({game["players"]}/{game["max"]})',
                    scale=0.07,
                    pos=(0, 0, y),
                    parent=self.frame,
                    command=self.select_game,
                    extraArgs=[game]
                )
                self.buttons[ip] = btn
                y -= 0.12
            else:
                self.buttons[ip]["text"] = f'{game["host"]}  ({game["players"]}/{game["max"]})'

        return task.cont

    def select_game(self, game):
        self.discovery.stop()
        self.app.taskMgr.remove(self.update_task)

        from client.ui.password_popup import PasswordPopup
        PasswordPopup(self.app, game, self.join_success)


    def join_success(self):
        print("Joined game successfully")
        # NEXT: show lobby


    def go_back(self):
        self.discovery.stop()
        self.app.taskMgr.remove(self.update_task)
        self.frame.destroy()
        self.app.show_main_menu()

