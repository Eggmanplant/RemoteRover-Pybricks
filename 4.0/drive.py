# RemoteRover
# Version 4.0 - drive mode
# By SonicGamer_Episode55

# Configuration

# Automatically enable the light:
# Default: 0
light = 0

# Automatically enable the parking mode - Highly recommended:
# Default: 1
parking = 1

# Default speed: Supported values: 50, 100:
# Default: 100
speed = 100

# Code begins here:

from pybricks.hubs import MoveHub
from pybricks.pupdevices import Motor, Light, Remote, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks import version

device_hub = MoveHub()
device_hub.light.on(Color.MAGENTA)

print("Searching for the remote...")

device_remote = Remote()

print("")
print("Finished loading the drive mode!")
print("Try to figure out the keybinds.")
print("They are using the red and center buttons on the remote.")
print("")

device_cds = ColorDistanceSensor(Port.C)
device_light = Light(Port.D)
device_motorA = Motor(Port.A)
device_motorB = Motor(Port.B)

inactivity_timer = StopWatch()

if not light == 0:
    device_remote.light.on(Color.WHITE)
    device_light.on(100)
else:
    device_remote.light.off()
    device_light.off()

if not parking == 0:
    device_hub.light.on(Color.RED)
else:
    device_hub.light.on(Color.GREEN)

while True:
    buttons = device_remote.buttons.pressed()

    # Reset the timer if there's any button pressed

    if buttons:
        inactivity_timer.reset()

    # Shut down if inactive for 2 minutes (120 seconds)

    if inactivity_timer.time() > 120000:  # 2 minutes in milliseconds
        device_hub.system.shutdown()

    # Move depending on the button.

    if Button.LEFT_PLUS in buttons:
        device_motorB.run(0 - speed * 10)

    if Button.LEFT_MINUS in buttons:
        device_motorB.run(speed * 10)

    if Button.LEFT in buttons:
        if Button.CENTER in buttons:
            if Button.RIGHT in buttons:
                print("Exiting program...")
                break
            else:
                if speed == 100 and Button.CENTER in buttons:
                    speed = 50
                    wait(250)
                    buttons = device_remote.buttons.pressed()
                if speed == 50 and Button.CENTER in buttons:
                    speed = 100
                    wait(250)
                print(f"Speed is now {speed}.")
        else:
            device_motorB.stop()

    if Button.RIGHT_PLUS in buttons:
        device_motorA.run(speed * 10)

    if Button.RIGHT_MINUS in buttons: 
        device_motorA.run(0 - speed * 10)

    if Button.RIGHT in buttons:
        if Button.CENTER in buttons:
            if parking == 0 and Button.CENTER in buttons:
                parking = 1
                device_hub.light.on(Color.RED)
                wait(250)
            buttons = device_remote.buttons.pressed()
            if parking == 1 and Button.CENTER in buttons:
                parking = 0
                device_hub.light.on(Color.GREEN)
                wait(250)
            print(f"Parking mode is now {parking}.")
        else:
            device_motorA.stop()

    if Button.CENTER in buttons:
        if light == 0 and Button.CENTER in buttons:
            device_light.on(100)
            device_remote.light.on(Color.WHITE)
            light = 1
            wait(250)
        buttons = device_remote.buttons.pressed()
        if light == 1 and Button.CENTER in buttons:
            device_light.off()
            device_remote.light.off()
            light = 0
            wait(250)
        print(f"Light is now {light}.")

    # Do not move by default.

    if not Button.RIGHT in buttons:
        if not Button.RIGHT_MINUS in buttons:
            if not Button.RIGHT_PLUS in buttons:
                device_motorA.stop()

    if not Button.LEFT in buttons:
        if not Button.LEFT_MINUS in buttons:
            if not Button.LEFT_PLUS in buttons:
                device_motorB.stop()

    # Parking mode code below.

    if device_cds.distance() <= 40 and parking == 1:
        if not Button.RIGHT_PLUS in buttons:
            if not Button.LEFT_PLUS in buttons:
                device_motorA.stop()
                device_motorB.stop()