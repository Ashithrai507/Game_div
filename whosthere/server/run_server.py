from server.tcp_server import GameServer
from server.discovery_server import DiscoveryBroadcaster
import threading

PASSWORD = "1234"

server = GameServer(PASSWORD)
server.start()

broadcaster = DiscoveryBroadcaster("Ashith's Game")
threading.Thread(
    target=broadcaster.broadcast_loop,
    daemon=True
).start()

input("Server running. Press ENTER to stop\n")
