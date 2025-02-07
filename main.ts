function foward50 () {
    robot.motorTank(44, 50, 1700)
    robot.motorStop()
}
function leftTurn () {
    robot.motorStop()
    basic.pause(1000)
    robot.motorTank(19, 0, 275)
    robot.motorStop()
}
input.onButtonPressed(Button.A, function () {
    foward25()
    foward25()
    foward25()
    rightTurn()
    rightTurn()
    foward25()
    foward25()
    foward25()
})
function rightTurn () {
    robot.motorStop()
    basic.pause(1000)
    robot.motorTank(0, 30, 1100)
    robot.motorStop()
}
function foward25 () {
    // note for tmr, try to find a way to make the motors have the same power output, not speed
    robot.motorStop()
    basic.pause(1000)
    robot.motorTank(44, 50, 950)
    robot.motorStop()
}
function uTurn () {
    robot.motorTank(0, 50, 1000)
    robot.motorStop()
}
robot.inksmithK8.start()
