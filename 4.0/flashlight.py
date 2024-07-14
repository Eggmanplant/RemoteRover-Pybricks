# RemoteRover
# Version 4.0 - flashlight mode
# By SonicGamer_Episode55

# Configuration

# Default light brightness: Supported values: 0 to 2:
# Default: 0
light = 0

# Power off when the hand is away:
# Default: 1
poweroff = 1

# Code begins here:

from pybricks.hubs import MoveHub
from pybricks.pupdevices import Light, ColorDistanceSensor
from pybricks.parameters import Button, Color, Port, Stop
from pybricks.tools import wait

device_hub = MoveHub()

if light == 0:
    device_hub.light.off()
if light == 1:
    device_hub.light.on(Color.GRAY)
if light == 2:
    device_hub.light.on(Color.WHITE)

device_hub.system.set_stop_button(None)
device_light = Light(Port.D)
device_cds = ColorDistanceSensor(Port.C)

print("Finished loading the flashlight mode!")
print("Press the center button,")
print("to switch the light mode.")

if not poweroff == 0:
    print("When you take your hand away,")
    print("the device will power off.")

print("")

while True:
    if device_hub.button.pressed():
        if light == 0 and device_hub.button.pressed():
            device_light.on(50)
            device_hub.light.on(Color.GRAY)
            light = 1
            wait(250)

        if light == 1 and device_hub.button.pressed():
            device_light.on(100)
            device_hub.light.on(Color.WHITE)
            light = 2
            wait(250)

        if light == 2 and device_hub.button.pressed():
            device_light.off()
            device_hub.light.off()
            light = 0
            wait(250)

        print(f"Light brightness is now {light}.")

    if device_cds.distance() > 10 and poweroff == 1:
        print("Exiting program...")
        break
