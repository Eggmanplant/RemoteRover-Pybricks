from pybricks.hubs import MoveHub
from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Button, Color, Port, Stop
from pybricks.tools import wait, StopWatch
from pybricks import version

hub = MoveHub()
cds = ColorDistanceSensor(Port.C)
hub.light.on(Color.CYAN)
emergency = 0

# RemoteRover 4.0 beta 1 - main menu
print("RemoteRover 4.0 beta 1 - main menu - by SonicGamer_Episode55")
print(f"Firmware version: {version}")

hub.system.set_stop_button(None)

while True:
    if hub.button.pressed() and cds.distance() <= 40:
        print("Flashlight selected!")
        import remoterover_flashlight

        hub.system.set_stop_button(Button.CENTER)
        emergency = 1
        break
        
    
    if hub.button.pressed() and cds.distance() > 40:
        print("Drive mode selected!")
        import remoterover_drivemode

        hub.system.set_stop_button(Button.CENTER)
        emergency = 1
        break

print("Program finished. Shutting down...")
hub.system.shutdown()


