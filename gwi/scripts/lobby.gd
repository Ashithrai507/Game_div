extends Control

@onready var code_label = $VBoxContainer/RoomCodeLabel
@onready var player_list = $VBoxContainer/PlayerList
@onready var start_button = $VBoxContainer/StartButton

func _ready():
	multiplayer.peer_connected.connect(_on_peer_change)
	multiplayer.peer_disconnected.connect(_on_peer_change)

	_refresh_players()

	# Show room code ONLY to host
	if Network.is_host:
		code_label.text = "Room Code: " + Network.room_code
	else:
		code_label.hide()

	# Only host can start game
	if not Network.is_host:
		start_button.hide()

func _on_peer_change(_id = 0):
	_refresh_players()

func _refresh_players():
	player_list.clear()
	player_list.add_item("Host")

	for id in multiplayer.get_peers():
		player_list.add_item("Player " + str(id))

func _on_start_pressed():
	rpc("start_game")

@rpc("call_local", "reliable")
func start_game():
	get_tree().change_scene_to_file("res://scenes/Game.tscn")
