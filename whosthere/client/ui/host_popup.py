from direct.gui.DirectGui import DirectFrame, DirectEntry, DirectButton, DirectLabel
from panda3d.core import TextNode

class HostPopup:
    def __init__(self, app):
        self.app = app

        self.frame = DirectFrame(
            frameColor=(0, 0, 0, 0.85),
            frameSize=(-0.6, 0.6, -0.4, 0.4)
        )

        DirectLabel(
            text="CREATE ROOM",
            scale=0.08,
            pos=(0, 0, 0.25),
            parent=self.frame,
            text_align=TextNode.ACenter
        )

        DirectLabel(
            text="Numeric Password",
            scale=0.05,
            pos=(0, 0, 0.05),
            parent=self.frame,
            text_align=TextNode.ACenter
        )

        self.entry = DirectEntry(
            scale=0.06,
            pos=(-0.35, 0, -0.05),
            width=8,
            parent=self.frame,
            obscured=True,
            command=self.submit
        )

        DirectButton(
            text="CREATE",
            scale=0.06,
            pos=(0, 0, -0.25),
            parent=self.frame,
            command=self.submit
        )

    def submit(self, *_):
        password = self.entry.get().strip()

        if not password.isdigit():
            self.entry.set("")
            return

        self.frame.destroy()
        self.app.start_host(password)
