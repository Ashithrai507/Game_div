extends Node

const GAME_PORT := 8910
const CODE_PORT := 9000
const MAX_PLAYERS := 8

var is_host := false
var room_name := ""
var room_password := ""
var room_code := ""

var peer: ENetMultiplayerPeer
var udp := PacketPeerUDP.new()

func _ready():
	print("NETWORK READY")

# =========================
# ROOM CODE GENERATION
# =========================
func generate_room_code(length := 5) -> String:
	const chars = "abcdefghijklmnopqrstuvwxyz0123456789"
	var rng = RandomNumberGenerator.new()
	rng.randomize()
	var code := ""

	for i in range(length):
		code += chars[rng.randi_range(0, chars.length() - 1)]
	return code

# =========================
# HOST
# =========================
func host_game(room: String, password: String):
	room_code = generate_room_code()
	room_name = room
	room_password = password
	is_host = true

	print("ROOM CODE:", room_code)

	peer = ENetMultiplayerPeer.new()
	peer.create_server(GAME_PORT, MAX_PLAYERS)
	multiplayer.multiplayer_peer = peer

	udp.bind(CODE_PORT, "*")

func _process(_delta):
	if not is_host:
		return

	while udp.get_available_packet_count() > 0:
		var msg = udp.get_packet().get_string_from_utf8()
		var ip = udp.get_packet_ip()

		if msg == "WHO_HAS|" + room_code:
			udp.set_dest_address(ip, CODE_PORT)
			udp.put_packet(("I_HAVE|" + room_code).to_utf8_buffer())
			print("Responded to code request from", ip)

# =========================
# JOIN
# =========================
func join_game(ip: String, password: String):
	room_password = password
	peer = ENetMultiplayerPeer.new()
	peer.create_client(ip, GAME_PORT)
	multiplayer.multiplayer_peer = peer
	print("Joining host at", ip)

func get_subnet_prefix() -> String:
	for ip in IP.get_local_addresses():
		if ip.begins_with("192.168.") or ip.begins_with("10."):
			var p = ip.split(".")
			return "%s.%s.%s." % [p[0], p[1], p[2]]
	return "192.168.1."
