extends Control

@onready var room_list = $VBoxContainer/RoomList
@onready var password_input = $VBoxContainer/PasswordInput

func _ready():
	print("JOIN MENU READY")
	Network.discovered_rooms.clear()
	_start_listening()

func _start_listening():
	Network.udp.bind(Network.DISCOVERY_PORT)
	Network.udp.set_broadcast_enabled(true)

func _process(_delta):
	while Network.udp.get_available_packet_count() > 0:
		var data = Network.udp.get_packet().get_string_from_utf8()
		_handle_room_packet(data)

func _handle_room_packet(data: String):
	var parts = data.split("|")
	if parts.size() < 3:
		return

	var room_name = parts[0]
	var port = parts[1]
	var players = parts[2]
	var ip = Network.udp.get_packet_ip()

	if not Network.discovered_rooms.has(room_name):
		Network.discovered_rooms[room_name] = {
			"ip": ip,
			"port": port
		}
		room_list.add_item("%s (%s players)" % [room_name, players])

func on_join_pressed():
	var selected = room_list.get_selected_items()
	if selected.is_empty():
		return

	var text = room_list.get_item_text(selected[0])
	var room_name = text.split(" ")[0]
	var info = Network.discovered_rooms[room_name]

	Network.join_game(info.ip, password_input.text)
	get_tree().change_scene_to_file("res://scenes/Lobby.tscn")

func on_back_pressed():
	get_tree().change_scene_to_file("res://scenes/MainMenu.tscn")
