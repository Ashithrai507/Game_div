from panda3d.core import Vec3
from direct.showbase.DirectObject import DirectObject

class FPSScene(DirectObject):
    def __init__(self, app):
        self.app = app
        self.app.disableMouse()

        self.speed = 5
        self.heading = 0
        self.pitch = 0

        self.app.taskMgr.add(self.update, "fps-update")

        self.accept("w", self.set_key, ["w", True])
        self.accept("w-up", self.set_key, ["w", False])
        self.keys = {"w": False}

    def set_key(self, key, value):
        self.keys[key] = value

    def update(self, task):
        dt = globalClock.getDt()

        if self.keys["w"]:
            self.app.camera.setY(
                self.app.camera, self.speed * dt
            )

        return task.cont
