# RemoteRover
# Version 4.0b3 - main menu
# By SonicGamer_Episode55

# No configs here!

from pybricks.hubs import MoveHub
from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Button, Color, Port, Stop
from pybricks.tools import wait, StopWatch
from pybricks import version

device_hub = MoveHub()
device_cds = ColorDistanceSensor(Port.C)
device_hub.light.on(Color.CYAN)

print("RemoteRover 4.0b3 - by SonicGamer_Episode55")
print("Menu controls:")
print("Drive mode: Press the button.")
print("Flashlight mode: Press the button,")
print("while having the hand near the back sensor.")
print("WARNING: The remote is required for the drive mode.")
print(f"Firmware version: {version}")

device_hub.system.set_stop_button(None)

while True:
    if device_hub.button.pressed() and device_cds.distance() <= 10:
        print("Flashlight mode selected!")
        import remoterover_flashlight

        device_hub.system.set_stop_button(Button.CENTER)
        break
        
    
    if device_hub.button.pressed() and device_cds.distance() > 10:
        print("Drive mode selected!")
        import remoterover_drivemode

        device_hub.system.set_stop_button(Button.CENTER)
        break

print("Program finished. Shutting down...")
device_hub.system.shutdown()
