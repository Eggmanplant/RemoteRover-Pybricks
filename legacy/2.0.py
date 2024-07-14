# Remote vehicle with lights
# By SonicGamer_Episode55
from pybricks.hubs import MoveHub
from pybricks.pupdevices import Motor, Light, Remote, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
lighton = 0
remote = Remote()
hub = MoveHub()
parking = ColorDistanceSensor(Port.C)
light = Light(Port.D)
motorA = Motor(Port.A)
motorB = Motor(Port.B)
inactivity_timer = StopWatch()
remote.light.off()
measureDistance = 0
while True:
    buttons = remote.buttons.pressed()
    # Reset the timer if there's any button pressed
    if buttons:
        inactivity_timer.reset()
    # Shut down if inactive for 2 minutes (120 seconds)
    if inactivity_timer.time() > 120000:  # 2 minutes in milliseconds
        hub.system.shutdown()
    # Return a move depending on the button.
    if Button.LEFT_PLUS in buttons:
        motorB.run(-1000)
    if Button.LEFT_MINUS in buttons:
        motorB.run(1000)
    if Button.LEFT in buttons:
        if Button.RIGHT in buttons:
            if Button.CENTER in buttons:
                hub.system.shutdown()
        else:
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
            remote.light.on(Color.WHITE)
            lighton = 1
            wait(250)
        buttons = remote.buttons.pressed()
        if(lighton == 1) and Button.CENTER in buttons:
            light.off()
            remote.light.off()
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
    if parking.distance() <= 40:
        if not Button.RIGHT_PLUS in buttons:
            if not Button.LEFT_PLUS in buttons:
                motorA.stop()
                motorB.stop()