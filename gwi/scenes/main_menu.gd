extends Control

func _ready():
	print("MAIN MENU READY")

func on_host_pressed():
	print("HOST PRESSED")
	get_tree().change_scene_to_file("res://scenes/HostMenu.tscn")

func on_join_pressed():
	print("JOIN PRESSED")
	get_tree().change_scene_to_file("res://scenes/JoinMenu.tscn")

func quit_game():
	print("QUIT PRESSED")
	get_tree().quit()
