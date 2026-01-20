extends Node

const GAME_PORT := 8910
const DISCOVERY_PORT := 8911
const MAX_PLAYERS := 8

var is_host := false
var room_name := ""
var room_password := ""

var peer: ENetMultiplayerPeer

# LAN discovery
var udp_broadcast := PacketPeerUDP.new()
var udp_listen := PacketPeerUDP.new()

var discovered_rooms := {}


func _ready():
	print("NETWORK AUTOLOAD READY")

# ================= HOST =================
func host_game(room: String, password: String):
	peer = ENetMultiplayerPeer.new()
	peer.create_server(GAME_PORT, MAX_PLAYERS)
	multiplayer.multiplayer_peer = peer

	is_host = true
	room_name = room
	room_password = password

	print("Hosting room:", room_name)
	_start_broadcast()
	
func _get_subnet_broadcast_ip() -> String:
	for ip in IP.get_local_addresses():
		if ip.begins_with("192.168.") or ip.begins_with("10."):
			var parts = ip.split(".")
			return "%s.%s.%s.255" % [parts[0], parts[1], parts[2]]
	return "255.255.255.255"


func _start_broadcast():
	udp_broadcast.set_broadcast_enabled(true)

	var broadcast_ip = _get_subnet_broadcast_ip()
	udp_broadcast.set_dest_address(broadcast_ip, DISCOVERY_PORT)

	print("📡 Using broadcast IP:", broadcast_ip)

	var timer := Timer.new()
	timer.wait_time = 1.0
	timer.autostart = true
	timer.timeout.connect(_broadcast_room)
	add_child(timer)


func _broadcast_room():
	var msg = "%s|%d|%d" % [
		room_name,
		GAME_PORT,
		multiplayer.get_peers().size() + 1
	]
	udp_broadcast.put_packet(msg.to_utf8_buffer())
	print("📡 BROADCAST:", msg)



# ================= JOIN =================
func join_game(ip: String, password: String):
	peer = ENetMultiplayerPeer.new()
	peer.create_client(ip, GAME_PORT)
	multiplayer.multiplayer_peer = peer

	room_password = password
	print("Joining server at", ip)
