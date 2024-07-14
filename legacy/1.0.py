# Remote vehicle with lights
# By SonicGamer_Episode55
from pybricks.hubs import MoveHub
from pybricks.pupdevices import Motor, Light, Remote
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
lighton = 0
remote = Remote()
hub = MoveHub()
light = Light(Port.D)
motorA = Motor(Port.A)
motorB = Motor(Port.B)
while True:
    buttons = remote.buttons.pressed()
    # Return a move depending on the button.
    if Button.LEFT_PLUS in buttons:
        motorB.run(-1000)
    if Button.LEFT_MINUS in buttons:
        motorB.run(1000)
    if Button.LEFT in buttons:
        motorB.stop()
    if Button.RIGHT_PLUS in buttons:
        motorA.run(1000)
    if Button.RIGHT_MINUS in buttons:
        motorA.run(-1000)
    if Button.RIGHT in buttons:
        motorA.stop()
    if Button.CENTER in buttons:
        if(lighton == 0) and Button.CENTER in buttons:
            light.on(100)
            lighton = 1
            wait(250)
        buttons = remote.buttons.pressed()
        if(lighton == 1) and Button.CENTER in buttons:
            light.off()
            lighton = 0
            wait(250)

    # Return no move by default.
    if not Button.RIGHT in buttons:
        if not Button.RIGHT_MINUS in buttons:
            if not Button.RIGHT_PLUS in buttons:
                motorA.stop()
    if not Button.LEFT in buttons:
        if not Button.LEFT_MINUS in buttons:
            if not Button.LEFT_PLUS in buttons:
                motorB.stop()
