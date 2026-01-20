extends Control

@onready var room_input = $VBoxContainer/RoomNameInput
@onready var password_input = $VBoxContainer/PasswordInput
@onready var code_label = $VBoxContainer/RoomCodeLabel

func _ready():
	code_label.text = "Room Code: -----"

func on_create_pressed():
	Network.host_game(room_input.text, password_input.text)

	# Show generated room code
	code_label.text = "Room Code: " + Network.room_code

	# Small delay so host can see the code (optional)
	await get_tree().create_timer(0.5).timeout

	get_tree().change_scene_to_file("res://scenes/Lobby.tscn")

func on_back_pressed():
	get_tree().change_scene_to_file("res://scenes/MainMenu.tscn")
