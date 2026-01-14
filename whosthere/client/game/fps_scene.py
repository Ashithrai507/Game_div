import json
from panda3d.core import (
    Vec3, CardMaker, WindowProperties,
    CollisionNode, CollisionRay, CollisionPlane, Plane,
    CollisionTraverser, CollisionHandlerQueue, BitMask32
)
from direct.showbase.DirectObject import DirectObject
from panda3d.core import BitMask32

class FPSScene(DirectObject):
    def __init__(self, app):
        self.app = app
        self.app.disableMouse()

        # --------------------
        # Player settings
        # --------------------
        self.speed = 6.0
        self.player_height = 1.8
        self.gravity = 25.0
        self.jump_strength = 9.0
        self.mouse_sensitivity = 0.15

        # Rotation
        self.yaw = 0.0
        self.pitch = 0.0
        self.max_pitch = 85

        # State
        self.vertical_velocity = 0.0
        self.on_ground = False
        self.cursor_locked = True

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
    # WORLD
    # ------------------------------------------------
    def setup_world(self):
        # Load ground model
        self.ground = self.app.loader.loadModel("maps/ground.glb")
        self.ground.reparentTo(self.app.render)
        self.ground.setPos(0, 0, 0)
        self.ground.setScale(1)

        # Enable collision on the model
        self.ground.node().setIntoCollideMask(BitMask32.bit(1))
            # Optional reference cube (keep for debugging)

        cube = CardMaker("cube")
        cube.setFrame(-0.5, 0.5, -0.5, 0.5)
        self.ref = self.app.render.attachNewNode(cube.generate())
        self.ref.setPos(2, 8, 1)
        self.ref.setColor(1, 0, 0, 1)
        
        # Reference cube
        cube = CardMaker("cube")
        cube.setFrame(-0.5, 0.5, -0.5, 0.5)
        self.ref = self.app.render.attachNewNode(cube.generate())
        self.ref.setPos(3, 12, 1)
        self.ref.setColor(1, 0, 0, 1)

    # ------------------------------------------------
    # CAMERA
    # ------------------------------------------------
    def setup_camera(self):
        self.app.camera.reparentTo(self.app.render)
        self.app.camera.setPos(0, 0, self.player_height)
        self.app.camera.setHpr(0, 0, 0)

    # ------------------------------------------------
    # COLLISION
    # ------------------------------------------------
    def setup_collision(self):
        self.traverser = CollisionTraverser()
        self.handler = CollisionHandlerQueue()

        # Ray starts ABOVE feet and goes down
        ray = CollisionRay(0, 0, 0.2, 0, 0, -1)
        cnode = CollisionNode("playerRay")
        cnode.addSolid(ray)
        cnode.setFromCollideMask(BitMask32.bit(1))
        cnode.setIntoCollideMask(BitMask32.allOff())

        self.ray_np = self.app.camera.attachNewNode(cnode)
        self.traverser.addCollider(self.ray_np, self.handler)

    # ------------------------------------------------
    # INPUT
    # ------------------------------------------------
    def setup_keys(self):
        for k in self.keys:
            self.accept(k, self.set_key, [k, True])
            self.accept(f"{k}-up", self.set_key, [k, False])

        self.accept("space", self.jump)
        self.accept("escape", self.unlock_cursor)
        self.accept("enter", self.lock_cursor)

    def set_key(self, key, value):
        self.keys[key] = value

    # ------------------------------------------------
    # CURSOR
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
        self.app.win.movePointer(
            0,
            self.app.win.getXSize() // 2,
            self.app.win.getYSize() // 2
        )

    # ------------------------------------------------
    # UPDATE LOOP
    # ------------------------------------------------
    def update(self, task):
        dt = globalClock.getDt()

        if self.cursor_locked:
            self.update_mouse_look()
            self.update_movement(dt)

        self.apply_gravity(dt)
        return task.cont

    # ------------------------------------------------
    # MOUSE LOOK
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
    # MOVEMENT
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

            # Rotate movement vector by camera orientation (CORRECT WAY)
            move_vec = self.app.camera.getQuat().xform(direction)

            self.app.camera.setPos(
                self.app.camera,
                move_vec * self.speed * dt
            )

    # ------------------------------------------------
    # GRAVITY + GROUND COLLISION
    # ------------------------------------------------
    def apply_gravity(self, dt):
        self.traverser.traverse(self.app.render)

        if self.handler.getNumEntries() > 0:
            self.handler.sortEntries()
            hit = self.handler.getEntry(0)
            ground_z = hit.getSurfacePoint(self.app.render).getZ()
            desired_z = ground_z + self.player_height

            if self.app.camera.getZ() <= desired_z:
                self.app.camera.setZ(desired_z)
                self.vertical_velocity = 0
                self.on_ground = True
                return

        self.on_ground = False
        self.vertical_velocity -= self.gravity * dt
        self.app.camera.setZ(
            self.app.camera.getZ() + self.vertical_velocity * dt
        )

    # ------------------------------------------------
    # JUMP
    # ------------------------------------------------
    def jump(self):
        if self.on_ground:
            self.vertical_velocity = self.jump_strength
            self.on_ground = False
