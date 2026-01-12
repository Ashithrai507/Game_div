import socket
import json
import time
from shared.protocol import DISCOVERY_PORT, make_discovery_packet

class DiscoveryBroadcaster:
    def __init__(self, host_name, max_players=10):
        self.host_name = host_name
        self.max_players = max_players
        self.players = 1  # host included
        self.running = True

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def broadcast_loop(self):
        while self.running:
            packet = make_discovery_packet(
                self.host_name,
                self.players,
                self.max_players
            )
            data = json.dumps(packet).encode()

            self.sock.sendto(
                data,
                ("<broadcast>", DISCOVERY_PORT)
            )

            time.sleep(1)  # broadcast every second

    def stop(self):
        self.running = False
        self.sock.close()
