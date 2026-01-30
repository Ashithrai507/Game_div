extends CharacterBody2D

const SPEED = 200
const JUMP_FORCE = -350
const GRAVITY = 900

func _physics_process(delta):
	# Gravity
	if not is_on_floor():
		velocity.y += GRAVITY * delta

	# Left / Right
	var direction = Input.get_axis("left", "right")
	velocity.x = direction * SPEED

	# Jump
	if Input.is_action_just_pressed("space") and is_on_floor():
		velocity.y = JUMP_FORCE

	move_and_slide()
