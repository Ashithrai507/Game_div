import socket, json
from shared.protocol import GAME_PORT, MSG_JOIN, MSG_ACCEPT

def try_join(ip, password, name):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, GAME_PORT))

    sock.send(json.dumps({
        "type": MSG_JOIN,
        "password": password,
        "name": name
    }).encode())

    reply = json.loads(sock.recv(1024).decode())
    if reply["type"] == MSG_ACCEPT:
        return sock

    sock.close()
    return None
