from panda3d.core import (
    Vec3, CardMaker, WindowProperties, CollisionNode,
    CollisionRay, CollisionTraverser, CollisionHandlerQueue
)
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
        self.gravity = 20.0
        self.jump_velocity = 0.0
        self.mouse_sensitivity = 0.15

        # Rotation
        self.yaw = 0.0
        self.pitch = 0.0
        self.max_pitch = 85

        # States
        self.cursor_locked = True
        self.on_ground = False
        self.vertical_velocity = 0.0

        # Input
        self.keys = {"w": False, "s": False, "a": False, "d": False}

        # Setup
        self.setup_world()
        self.setup_camera()
        self.setup_collision()
        self.lock_cursor()
        self.setup_keys()

        # Update loop
        self.app.taskMgr.add(self.update, "fps-update")

    # ------------------------------------------------
    # World
    # ------------------------------------------------
    def setup_world(self):
        cm = CardMaker("ground")
        cm.setFrame(-50, 50, -50, 50)
        self.ground = self.app.render.attachNewNode(cm.generate())
        self.ground.setHpr(0, -90, 0)
        self.ground.setPos(0, 0, 0)
        self.ground.setColor(0.15, 0.15, 0.15, 1)

        # Visual reference
        cube = CardMaker("cube")
        cube.setFrame(-0.5, 0.5, -0.5, 0.5)
        self.ref = self.app.render.attachNewNode(cube.generate())
        self.ref.setPos(2, 10, 1)
        self.ref.setColor(1, 0, 0, 1)

    # ------------------------------------------------
    # Camera
    # ------------------------------------------------
    def setup_camera(self):
        self.app.camera.reparentTo(self.app.render)
        self.app.camera.setPos(0, 0, self.player_height)
        self.app.camera.setHpr(0, 0, 0)

    # ------------------------------------------------
    # Collision (Ground)
    # ------------------------------------------------
    def setup_collision(self):
        self.traverser = CollisionTraverser()
        self.handler = CollisionHandlerQueue()

        ray = CollisionRay(0, 0, 0, 0, 0, -1)
        cnode = CollisionNode("groundRay")
        cnode.addSolid(ray)
        self.ray_np = self.app.camera.attachNewNode(cnode)

        self.traverser.addCollider(self.ray_np, self.handler)

    # ------------------------------------------------
    # Cursor control
    # ------------------------------------------------
    def lock_cursor(self):
        props = WindowProperties()
        props.setCursorHidden(True)
        self.app.win.requestProperties(props)
        self.cursor_locked = True
        self.center_mouse()

    def unlock_cursor(self):
        props = WindowProperties()
        props.setCursorHidden(False)
        self.app.win.requestProperties(props)
        self.cursor_locked = False

    def center_mouse(self):
        if self.app.win:
            self.app.win.movePointer(
                0,
                self.app.win.getXSize() // 2,
                self.app.win.getYSize() // 2
            )

    # ------------------------------------------------
    # Input
    # ------------------------------------------------
    def setup_keys(self):
        for key in self.keys:
            self.accept(key, self.set_key, [key, True])
            self.accept(f"{key}-up", self.set_key, [key, False])

        self.accept("escape", self.unlock_cursor)
        self.accept("enter", self.lock_cursor)

    def set_key(self, key, value):
        self.keys[key] = value

    # ------------------------------------------------
    # Update loop
    # ------------------------------------------------
    def update(self, task):
        dt = globalClock.getDt()

        if self.cursor_locked:
            self.update_mouse_look()

        self.update_movement(dt)
        self.apply_gravity(dt)

        return task.cont

    # ------------------------------------------------
    # Mouse look
    # ------------------------------------------------
    def update_mouse_look(self):
        if not self.app.mouseWatcherNode.hasMouse():
            return

        md = self.app.win.getPointer(0)
        cx = self.app.win.getXSize() // 2
        cy = self.app.win.getYSize() // 2

        dx = md.getX() - cx
        dy = md.getY() - cy

        self.yaw -= dx * self.mouse_sensitivity
        self.pitch -= dy * self.mouse_sensitivity
        self.pitch = max(-self.max_pitch, min(self.max_pitch, self.pitch))

        self.app.camera.setHpr(self.yaw, self.pitch, 0)
        self.center_mouse()

    # ------------------------------------------------
    # Movement
    # ------------------------------------------------
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
            self.app.camera.setPos(
                self.app.camera,
                self.app.camera.getQuat() * direction * self.speed * dt
            )

    # ------------------------------------------------
    # Gravity & ground collision
    # ------------------------------------------------
    def apply_gravity(self, dt):
        self.traverser.traverse(self.app.render)

        if self.handler.getNumEntries() > 0:
            self.handler.sortEntries()
            hit = self.handler.getEntry(0)
            ground_z = hit.getSurfacePoint(self.app.render).getZ()

            cam_z = self.app.camera.getZ()
            desired_z = ground_z + self.player_height

            if cam_z <= desired_z:
                self.app.camera.setZ(desired_z)
                self.vertical_velocity = 0
                self.on_ground = True
                return

        self.on_ground = False
        self.vertical_velocity -= self.gravity * dt
        self.app.camera.setZ(
            self.app.camera.getZ() + self.vertical_velocity * dt
        )
