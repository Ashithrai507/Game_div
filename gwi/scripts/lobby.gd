extends Control

@onready var player_list = $VBoxContainer/PlayerList
@onready var start_button = $VBoxContainer/StartButton
@onready var code_label = $VBoxContainer/RoomCodeLabel

func _ready():
	print("LOBBY READY")

	multiplayer.peer_connected.connect(_on_player_connected)
	multiplayer.peer_disconnected.connect(_on_player_disconnected)

	_refresh_players()

	# Show room code only for host
	if Network.is_host:
		code_label.text = "Room Code: " + Network.room_code
	else:
		code_label.hide()

	# Only host can start the game
	if not Network.is_host:
		start_button.hide()

func _on_player_connected(id):
	print("Player connected:", id)
	_refresh_players()

func _on_player_disconnected(id):
	print("Player disconnected:", id)
	_refresh_players()

func _refresh_players():
	player_list.clear()
	player_list.add_item("Host")

	for id in multiplayer.get_peers():
		player_list.add_item("Player " + str(id))

func _on_start_pressed():
	print("START GAME PRESSED")
	rpc("start_game")

@rpc("call_local", "reliable")
func start_game():
	get_tree().change_scene_to_file("res://scenes/Game.tscn")
