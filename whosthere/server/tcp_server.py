import socket
import threading
import json
from shared.protocol import GAME_PORT, MSG_JOIN, MSG_ACCEPT, MSG_REJECT

class GameServer:
    def __init__(self, password):
        self.password = password
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("", GAME_PORT))
        self.sock.listen(10)

    def start(self):
        threading.Thread(target=self.accept_loop, daemon=True).start()

    def accept_loop(self):
        while True:
            client, addr = self.sock.accept()
            threading.Thread(
                target=self.handle_client,
                args=(client,),
                daemon=True
            ).start()

    def handle_client(self, client):
        data = client.recv(1024)
        msg = json.loads(data.decode())

        if msg["type"] == MSG_JOIN:
            if msg["password"] == self.password:
                client.send(json.dumps({
                    "type": MSG_ACCEPT
                }).encode())
            else:
                client.send(json.dumps({
                    "type": MSG_REJECT
                }).encode())
                client.close()
