import json
import threading
from shared.protocol import MSG_LOBBY_STATE, MSG_START_GAME

class LobbyServer:
    def __init__(self):
        self.players = []   # list of player names
        self.clients = []   # client sockets
        self.lock = threading.Lock()

    def add_player(self, name, sock):
        with self.lock:
            self.players.append(name)
            self.clients.append(sock)
        self.broadcast()

    def remove_player(self, sock):
        with self.lock:
            if sock in self.clients:
                idx = self.clients.index(sock)
                self.clients.pop(idx)
                self.players.pop(idx)
        self.broadcast()

    def broadcast(self):
        msg = json.dumps({
            "type": MSG_LOBBY_STATE,
            "players": self.players
        }).encode()

        for c in self.clients:
            try:
                c.send(msg)
            except:
                pass

    def start_game(self):
        msg = json.dumps({
            "type": MSG_START_GAME
        }).encode()

        for c in self.clients:
            c.send(msg)
