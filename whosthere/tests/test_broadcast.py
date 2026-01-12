import threading
from server.discovery_server import DiscoveryBroadcaster

broadcaster = DiscoveryBroadcaster("Ashith's Game")

threading.Thread(
    target=broadcaster.broadcast_loop,
    daemon=True
).start()

input("Broadcasting... press ENTER to stop\n")
