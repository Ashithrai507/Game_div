extends Control

@onready var room_input = $VBoxContainer/RoomNameInput

func on_create_pressed():
	Network.host_game(room_input.text)
	get_tree().change_scene_to_file("res://scenes/Lobby.tscn")

func on_back_pressed():
	get_tree().change_scene_to_file("res://scenes/MainMenu.tscn")
