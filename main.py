def foward50():
    robot.motor_tank(50, 44, 1700)
    robot.motor_stop()
def leftTurn():
    robot.motor_steer(90, 100, 500)
    robot.motor_stop()

def on_button_pressed_a():
    
    foward25()
input.on_button_pressed(Button.A, on_button_pressed_a)

def rightTurn():
    robot.inksmith_k8.motor_steer(-90, 60, 500)
    robot.motor_steer(-90, 60, 500)
    robot.motor_stop()
def foward25():
    # note for tmr, try to find a way to make the motors have the same power output, not speed
    robot.motor_tank(50, 50, 850)
    robot.motor_stop()
def uTurn():
    robot.motor_steer(90, 100, 850)
    robot.motor_stop()
robot.inksmith_k8.start()