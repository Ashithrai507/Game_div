import json
import threading
from shared.protocol import MSG_LOBBY_STATE, MSG_START_GAME

class LobbyClient:
    def __init__(self, sock, on_update, on_start):
        self.sock = sock
        self.on_update = on_update
        self.on_start = on_start
        threading.Thread(target=self.listen, daemon=True).start()

    def listen(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break

            msg = json.loads(data.decode())

            if msg["type"] == MSG_LOBBY_STATE:
                self.on_update(msg["players"])

            elif msg["type"] == MSG_START_GAME:
                self.on_start()
