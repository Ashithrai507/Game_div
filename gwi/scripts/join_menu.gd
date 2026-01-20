extends Control

@onready var code_input = $VBoxContainer/CodeInput

var udp := PacketPeerUDP.new()
var scanning := false

func on_join_pressed():
	var code = code_input.text.strip_edges().to_lower()
	if code == "":
		return

	udp.bind(Network.CODE_PORT, "*")
	scanning = true
	_scan_subnet(code)

func _scan_subnet(code: String):
	var base = Network.get_subnet_prefix()

	for i in range(1, 255):
		udp.set_dest_address(base + str(i), Network.CODE_PORT)
		udp.put_packet(("WHO_HAS|" + code).to_utf8_buffer())

func _process(_delta):
	if not scanning:
		return

	while udp.get_available_packet_count() > 0:
		var msg = udp.get_packet().get_string_from_utf8()
		var ip = udp.get_packet_ip()

		if msg == "I_HAVE|" + code_input.text.to_lower():
			scanning = false
			Network.join_game(ip)
			get_tree().change_scene_to_file("res://scenes/Lobby.tscn")

func on_back_pressed():
	get_tree().change_scene_to_file("res://scenes/MainMenu.tscn")
