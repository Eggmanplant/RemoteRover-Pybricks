# RemoteRover
# Version 4.0.1 - main menu
# By Eggmanplant

# No configs here!

from pybricks.hubs import MoveHub
from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Button, Color, Port, Stop
from pybricks.tools import wait, StopWatch
from pybricks import version

device_hub = MoveHub()
device_cds = ColorDistanceSensor(Port.C)
device_hub.light.on(Color.CYAN)

print("RemoteRover 4.0.1 - by Eggmanplant")
print()
print("Controls:")
print("Drive mode: Press the button.")
print("Flashlight mode: Press the button,")
print("while having your hand near the sensor.")
print("The remote is needed for the drive mode.")
print()
print(f"Firmware version: {version}")
print()

device_hub.system.set_stop_button(None)

while True:
    if device_hub.button.pressed() and device_cds.distance() <= 10:
        print("Flashlight mode selected!")
        print()
        import flashlight
        device_hub.system.set_stop_button(Button.CENTER)
        break
        
    if device_hub.button.pressed() and device_cds.distance() > 10:
        print("Drive mode selected!")
        print()
        import drive
        device_hub.system.set_stop_button(Button.CENTER)
        break

print()
print("Program finished. Shutting down...")
device_hub.system.shutdown()
