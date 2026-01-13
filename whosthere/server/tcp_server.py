import socket, threading, json
from shared.protocol import (
    GAME_PORT, MSG_JOIN, MSG_ACCEPT, MSG_REJECT, MSG_LOBBY_STATE, MSG_START_GAME
)

class GameServer:
    def __init__(self, password):
        self.password = password
        self.players = []   # list of dicts: {name, is_host}
        self.clients = []          # list of sockets
        self.lock = threading.Lock()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("", GAME_PORT))
        self.sock.listen(10)

    def start(self):
        threading.Thread(target=self.accept_loop, daemon=True).start()

    def start_game(self):
        msg = json.dumps({
            "type": MSG_START_GAME
        }).encode()

        for c in self.clients:
            try:
                c.send(msg)
            except:
                pass
            
    def accept_loop(self):
        while True:
            client, addr = self.sock.accept()
            threading.Thread(
                target=self.handle_client,
                args=(client,),
                daemon=True
            ).start()

    def handle_client(self, client):
        try:
            data = client.recv(1024)
            msg = json.loads(data.decode())

            if msg["type"] == MSG_JOIN:
                if msg["password"] != self.password:
                    client.send(json.dumps({"type": MSG_REJECT}).encode())
                    client.close()
                    return

                name = msg.get("name", "Unknown")

                with self.lock:
                    is_host = len(self.players) == 0
                    self.players.append({
                        "name": name,
                        "host": is_host
                    })
                    self.clients.append(client)

                client.send(json.dumps({"type": MSG_ACCEPT}).encode())
                self.broadcast_lobby()

                while True:
                    if not client.recv(1024):
                        break
        finally:
            self.remove_client(client)


    def remove_client(self, client):
        with self.lock:
            if client in self.clients:
                idx = self.clients.index(client)
                self.clients.pop(idx)
                self.players.pop(idx)
        self.broadcast_lobby()

    def broadcast_lobby(self):
        msg = json.dumps({
            "type": MSG_LOBBY_STATE,
            "players": self.players
        }).encode()

        for c in self.clients:
            try:
                c.send(msg)
            except:
                pass

