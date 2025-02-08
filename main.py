# input code for SO here

def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def foward50():
    robot.motor_tank(44, 50, 1700)
    robot.motor_stop()
def leftTurn():
    robot.motor_stop()
    basic.pause(1000)
    robot.motor_tank(19, 0, 275)
    robot.motor_stop()
def rightTurn():
    robot.motor_stop()
    basic.pause(1000)
    robot.motor_tank(0, 30, 1100)
    robot.motor_stop()
def foward25():
    robot.motor_tank(44, 50, 950)
    robot.motor_stop()
def uTurn():
    robot.motor_tank(0, 50, 1000)
    robot.motor_stop()
robot.inksmith_k8.start()
basic.clear_screen()
