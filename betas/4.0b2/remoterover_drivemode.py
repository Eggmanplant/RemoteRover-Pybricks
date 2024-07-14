# RemoteRover
# Version 4.0 beta 2 - drive mode
# By SonicGamer_Episode55
from pybricks.hubs import MoveHub
from pybricks.pupdevices import Motor, Light, Remote, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks import version
hub = MoveHub()
lighton = 0
hub.light.on(Color.MAGENTA)
print("Finished loading drive mode.")
print("Searching for remotes...")
remote = Remote()
print("Remote connected!")
parking = ColorDistanceSensor(Port.C)
light = Light(Port.D)
motorA = Motor(Port.A)
motorB = Motor(Port.B)
inactivity_timer = StopWatch()
remote.light.off()
hub.light.on(Color.RED)
parkingCrashCheck = 1
speed = 100
while True:
    buttons = remote.buttons.pressed()
    # Reset the timer if there's any button pressed
    if buttons:
        inactivity_timer.reset()
    # Shut down if inactive for 2 minutes (120 seconds)
    if inactivity_timer.time() > 120000:  # 2 minutes in milliseconds
        hub.system.shutdown()
    # Move depending on the button.
    if Button.LEFT_PLUS in buttons:
        motorB.run(0 - speed * 10)
    if Button.LEFT_MINUS in buttons:
        motorB.run(speed * 10)
    if Button.LEFT in buttons:
        if Button.CENTER in buttons:
            if Button.RIGHT in buttons:
                print("Exiting program...")
                break
            else:
                if speed == 100 and Button.CENTER in buttons:
                    speed = 50
                    wait(250)
                    buttons = remote.buttons.pressed()
                if speed == 50 and Button.CENTER in buttons:
                    speed = 100
                    wait(250)
                print(f"Speed is now {speed}.")


        else:
            motorB.stop()
    if Button.RIGHT_PLUS in buttons:
        motorA.run(speed * 10)
    if Button.RIGHT_MINUS in buttons: 
        motorA.run(0 - speed * 10)
    if Button.RIGHT in buttons:
        if Button.CENTER in buttons:
            if parkingCrashCheck == 0 and Button.CENTER in buttons:
                parkingCrashCheck = 1
                hub.light.on(Color.RED)
                wait(250)
            buttons = remote.buttons.pressed()
            if parkingCrashCheck == 1 and Button.CENTER in buttons:
                parkingCrashCheck = 0
                hub.light.on(Color.GREEN)
                wait(250)
            print(f"CrashCheck is now {parkingCrashCheck}.")
        else:
            motorA.stop()
    if Button.CENTER in buttons:
        if lighton == 0 and Button.CENTER in buttons:
            light.on(100)
            remote.light.on(Color.WHITE)
            lighton = 1
            wait(250)
        buttons = remote.buttons.pressed()
        if lighton == 1 and Button.CENTER in buttons:
            light.off()
            remote.light.off()
            lighton = 0
            wait(250)
        print(f"Light is now {lighton}.")
    # Do not move by default.
    if not Button.RIGHT in buttons:
        if not Button.RIGHT_MINUS in buttons:
            if not Button.RIGHT_PLUS in buttons:
                motorA.stop()
    if not Button.LEFT in buttons:
        if not Button.LEFT_MINUS in buttons:
            if not Button.LEFT_PLUS in buttons:
                motorB.stop()
    # Parking crash check code below.
    if parking.distance() <= 40 and parkingCrashCheck == 1:
        if not Button.RIGHT_PLUS in buttons:
            if not Button.LEFT_PLUS in buttons:
                motorA.stop()
                motorB.stop()