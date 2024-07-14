from pybricks.hubs import MoveHub
from pybricks.pupdevices import Light, ColorDistanceSensor
from pybricks.parameters import Button, Color, Port, Stop
from pybricks.tools import wait

hub = MoveHub()
hub.light.off()
hub.system.set_stop_button(None)
lighton = 0
light = Light(Port.D)
cds = ColorDistanceSensor(Port.C)

# RemoteRover 4.0 beta 2 - flashlight mode

print("Finished loading flashlight mode!")

while True:
    if hub.button.pressed():
        if lighton == 2 and hub.button.pressed():
            light.off()
            hub.light.off()
            lighton = 0
            wait(250)
        if lighton == 0 and hub.button.pressed():
            light.on(50)
            hub.light.on(Color.GRAY)
            lighton = 1
            wait(250)
        if lighton == 1 and hub.button.pressed():
            light.on(100)
            hub.light.on(Color.WHITE)
            lighton = 2
            wait(250)
        print(f"Light brightness is now {lighton}.")
    if cds.distance() > 10:
        print("Exiting program...")
        break
