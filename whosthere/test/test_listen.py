from client.network.discovery_client import DiscoveryClient

def on_game_found(game):
    print("\nFOUND GAME:")
    for k, v in game.items():
        print(f"  {k}: {v}")

client = DiscoveryClient(on_game_found)
client.start()

input("\nListening for games... press ENTER to stop\n")
