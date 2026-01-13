from panda3d.core import Vec3, CardMaker, WindowProperties
from direct.showbase.DirectObject import DirectObject
from math import sin, cos, radians

class FPSScene(DirectObject):
    def __init__(self, app):
        self.app = app
        self.app.disableMouse()

        # --------------------
        # Player settings
        # --------------------
        self.speed = 6.0
        self.player_height = 1.8
        self.mouse_sensitivity = 0.15

        # Rotation
        self.yaw = 0.0
        self.pitch = 0.0
        self.max_pitch = 85

        # Input
        self.keys = {
            "w": False,
            "s": False,
            "a": False,
            "d": False
        }

        # Setup
        self.setup_world()
        self.setup_camera()
        self.setup_mouse()
        self.setup_keys()

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

        # Reference cube
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
        self.app.camera.setHpr(0, 0, 0)

    # --------------------
    # Mouse setup
    # --------------------
    def setup_mouse(self):
        props = WindowProperties()
        props.setCursorHidden(True)
        self.app.win.requestProperties(props)

        self.center_mouse()

    def center_mouse(self):
        if self.app.win:
            self.app.win.movePointer(
                0,
                self.app.win.getXSize() // 2,
                self.app.win.getYSize() // 2
            )

    # --------------------
    # Keyboard
    # --------------------
    def setup_keys(self):
        for key in self.keys:
            self.accept(key, self.set_key, [key, True])
            self.accept(f"{key}-up", self.set_key, [key, False])

    def set_key(self, key, value):
        self.keys[key] = value

    # --------------------
    # Update loop
    # --------------------
    def update(self, task):
        dt = globalClock.getDt()

        self.update_mouse_look()
        self.update_movement(dt)

        return task.cont

    # --------------------
    # Mouse look
    # --------------------
    def update_mouse_look(self):
        if not self.app.mouseWatcherNode.hasMouse():
            return

        md = self.app.win.getPointer(0)

        cx = self.app.win.getXSize() // 2
        cy = self.app.win.getYSize() // 2

        dx = md.getX() - cx
        dy = md.getY() - cy

        # Apply sensitivity
        self.yaw -= dx * self.mouse_sensitivity
        self.pitch -= dy * self.mouse_sensitivity

        # Clamp pitch
        self.pitch = max(-self.max_pitch, min(self.max_pitch, self.pitch))

        # Apply rotation
        self.app.camera.setHpr(self.yaw, self.pitch, 0)

        # Recenter mouse
        self.center_mouse()

    # --------------------
    # Movement
    # --------------------
    def update_movement(self, dt):
        direction = Vec3(0, 0, 0)

        if self.keys["w"]:
            direction.y += 1
        if self.keys["s"]:
            direction.y -= 1
        if self.keys["a"]:
            direction.x -= 1
        if self.keys["d"]:
            direction.x += 1

        if direction.lengthSquared() > 0:
            direction.normalize()

            # Move relative to camera direction
            self.app.camera.setPos(
                self.app.camera,
                direction * self.speed * dt
            )
