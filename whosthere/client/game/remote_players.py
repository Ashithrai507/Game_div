from panda3d.core import CardMaker, Vec3

class RemotePlayers:
    def __init__(self, render):
        self.render = render
        self.players = {}

    def update_player(self, pid, pos, rot):
        if pid not in self.players:
            cm = CardMaker("remote")
            cm.setFrame(-0.5, 0.5, -0.5, 0.5)
            np = self.render.attachNewNode(cm.generate())
            np.setColor(0, 0, 1, 1)
            self.players[pid] = np

        p = self.players[pid]
        p.setPos(Vec3(*pos))
        p.setHpr(rot[0], 0, 0)
