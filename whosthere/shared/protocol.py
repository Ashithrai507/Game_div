DISCOVERY_PORT = 54545
GAME_PORT = 6000

DISCOVERY_MAGIC = "PYFPS_DISCOVERY"
MSG_JOIN = "join"
MSG_ACCEPT = "accept"
MSG_REJECT = "reject"
MSG_LOBBY_STATE = "lobby_state"
MSG_START_GAME = "start_game"


def make_discovery_packet(host_name, players, max_players):
    return {
        "magic": DISCOVERY_MAGIC,
        "host": host_name,
        "players": players,
        "max": max_players,
        "port": GAME_PORT
    }
