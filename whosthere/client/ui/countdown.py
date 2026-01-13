from direct.gui.DirectGui import DirectLabel
from panda3d.core import TextNode

class Countdown:
    def __init__(self, app, on_finish):
        self.app = app
        self.on_finish = on_finish
        self.count = 3

        self.label = DirectLabel(
            text=str(self.count),
            scale=0.25,
            pos=(0, 0, 0),
            text_align=TextNode.ACenter
        )

        self.app.taskMgr.doMethodLater(
            1, self.tick, "countdown-task"
        )

    def tick(self, task):
        self.count -= 1

        if self.count == 0:
            self.label.destroy()
            self.on_finish()
            return task.done

        self.label["text"] = str(self.count)
        return task.again
