from direct.gui.DirectGui import DirectFrame, DirectEntry, DirectButton, DirectLabel
from panda3d.core import TextNode

class PasswordPopup:
    def __init__(self, app, game, on_success):
        self.app = app
        self.game = game
        self.on_success = on_success

        self.frame = DirectFrame(
            frameColor=(0, 0, 0, 0.8),
            frameSize=(-0.6, 0.6, -0.4, 0.4)
        )

        DirectLabel(
            text="Enter Password",
            scale=0.07,
            pos=(0, 0, 0.25),
            parent=self.frame,
            text_align=TextNode.ACenter
        )

        self.entry = DirectEntry(
            scale=0.06,
            pos=(-0.4, 0, 0),
            width=10,
            parent=self.frame,
            obscured=True
        )

        DirectButton(
            text="JOIN",
            scale=0.06,
            pos=(0, 0, -0.2),
            parent=self.frame,
            command=self.submit
        )

    def submit(self):
        from client.network.tcp_client import try_join
        ok = try_join(self.game["ip"], self.entry.get())

        if ok:
            self.frame.destroy()
            self.app.show_lobby(is_host=False)

