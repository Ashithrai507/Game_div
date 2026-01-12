import socket
import json
from shared.protocol import GAME_PORT, MSG_JOIN, MSG_ACCEPT

def try_join(ip, password):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, GAME_PORT))

    sock.send(json.dumps({
        "type": MSG_JOIN,
        "password": password
    }).encode())

    reply = json.loads(sock.recv(1024).decode())
    return reply["type"] == MSG_ACCEPT
