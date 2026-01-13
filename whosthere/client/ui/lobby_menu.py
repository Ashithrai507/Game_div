from direct.gui.DirectGui import DirectFrame, DirectLabel, DirectButton
from panda3d.core import TextNode

class LobbyMenu:
    def __init__(self, app, is_host=False):
        self.app = app
        self.is_host = is_host
        self.labels = []

        self.frame = DirectFrame(
            frameColor=(0.05, 0.05, 0.05, 1),
            frameSize=(-1.3, 1.3, -1, 1)
        )

        DirectLabel(
            text="LOBBY",
            scale=0.1,
            pos=(0, 0, 0.7),
            parent=self.frame,
            text_align=TextNode.ACenter
        )

        self.player_frame = DirectFrame(
            frameColor=(0.1, 0.1, 0.1, 1),
            frameSize=(-0.8, 0.8, -0.4, 0.4),
            pos=(0, 0, 0),
            parent=self.frame
        )

        if self.is_host:
            self.start_btn = DirectButton(
                text="START GAME",
                scale=0.07,
                pos=(0, 0, -0.7),
                parent=self.frame,
                command=self.start_game
            )

    def update_players(self, players):
        for lbl in self.labels:
            lbl.destroy()
        self.labels.clear()

        y = 0.25
        for p in players:
            name = p["name"]
            if p.get("host"):
                name += " (Host)"

            lbl = DirectLabel(
                text=name,
                scale=0.06,
                pos=(0, 0, y),
                parent=self.player_frame,
                text_align=TextNode.ACenter
            )
            self.labels.append(lbl)
            y -= 0.12 #updated


    def start_game(self):
    # Notify server (host only)
        self.app.server.start_game()

