from panda3d.core import Vec3, CardMaker
from direct.showbase.DirectObject import DirectObject

class FPSScene(DirectObject):
    def __init__(self, app):
        self.app = app
        self.app.disableMouse()

        # --------------------
        # Player settings
        # --------------------
        self.speed = 6.0
        self.player_height = 1.8

        # --------------------
        # Setup world
        # --------------------
        self.setup_world()
        self.setup_camera()

        # Input
        self.keys = {"w": False, "s": False}
        self.accept("w", self.set_key, ["w", True])
        self.accept("w-up", self.set_key, ["w", False])
        self.accept("s", self.set_key, ["s", True])
        self.accept("s-up", self.set_key, ["s", False])

        # Update loop
        self.app.taskMgr.add(self.update, "fps-update")

    # --------------------
    # World
    # --------------------
    def setup_world(self):
        # Ground
        cm = CardMaker("ground")
        cm.setFrame(-50, 50, -50, 50)
        self.ground = self.app.render.attachNewNode(cm.generate())
        self.ground.setHpr(0, -90, 0)
        self.ground.setPos(0, 10, 0)
        self.ground.setColor(0.15, 0.15, 0.15, 1)

        # Reference cube (so movement is obvious)
        cube_cm = CardMaker("cube")
        cube_cm.setFrame(-0.5, 0.5, -0.5, 0.5)
        self.cube = self.app.render.attachNewNode(cube_cm.generate())
        self.cube.setPos(0, 15, 1)
        self.cube.setColor(1, 0, 0, 1)

    # --------------------
    # Camera
    # --------------------
    def setup_camera(self):
        self.app.camera.reparentTo(self.app.render)
        self.app.camera.setPos(0, 0, self.player_height)

    # --------------------
    # Input
    # --------------------
    def set_key(self, key, value):
        self.keys[key] = value

    # --------------------
    # Update loop
    # --------------------
    def update(self, task):
        dt = globalClock.getDt()

        if self.keys["w"]:
            self.app.camera.setY(
                self.app.camera, self.speed * dt
            )
        if self.keys["s"]:
            self.app.camera.setY(
                self.app.camera, -self.speed * dt
            )

        return task.cont
