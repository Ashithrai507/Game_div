import socket
import json
import threading
from shared.protocol import DISCOVERY_PORT, DISCOVERY_MAGIC

class DiscoveryClient:
    def __init__(self, on_game_found):
        self.on_game_found = on_game_found
        self.running = True

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("", DISCOVERY_PORT))

    def listen(self):
        while self.running:
            data, addr = self.sock.recvfrom(1024)
            try:
                msg = json.loads(data.decode())
            except:
                continue

            if msg.get("magic") != DISCOVERY_MAGIC:
                continue

            msg["ip"] = addr[0]
            self.on_game_found(msg)

    def start(self):
        threading.Thread(target=self.listen, daemon=True).start()

    def stop(self):
        self.running = False
        self.sock.close()
