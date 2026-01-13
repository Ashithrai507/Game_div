from direct.gui.DirectGui import DirectButton, DirectFrame, DirectLabel
from panda3d.core import TextNode

class MainMenu:
    def __init__(self, app):
        self.app = app

        # Root container
        self.frame = DirectFrame(
            frameColor=(0.05, 0.05, 0.05, 1),
            frameSize=(-1.3, 1.3, -1, 1)
        )

        # Title
        self.title = DirectLabel(
            text="MULTIPLAYER FPS",
            scale=0.12,
            pos=(0, 0, 0.6),
            parent=self.frame,
            text_fg=(1, 1, 1, 1),
            text_align=TextNode.ACenter
        )

        # Buttons
        self.host_btn = self.create_button(
            "HOST GAME", 0.2, self.on_host
        )

        self.join_btn = self.create_button(
            "JOIN GAME", 0.05, self.on_join
        )

        self.quit_btn = self.create_button(
            "QUIT", -0.1, self.on_quit
        )

    def create_button(self, text, y, command):
        return DirectButton(
            text=text,
            scale=0.08,
            pos=(0, 0, y),
            parent=self.frame,
            command=command,
            frameColor=(0.15, 0.15, 0.15, 1),
            text_fg=(1, 1, 1, 1),
            relief=1
        )

    def on_host(self):
        from client.ui.host_popup import HostPopup
        HostPopup(self.app)


    def on_join(self):
        self.frame.destroy()
        self.app.show_join_menu()


    def on_quit(self):
        self.app.userExit()
