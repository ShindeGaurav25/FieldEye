"""
drone.py

Controls the drone operations.

Developer : Gaurav Shinde
Project : FieldEye
"""


class Drone:
    """
    Drone Control Class
    """

    def __init__(self):
        self.connected = False
        self.armed = False
        self.flying = False

    def connect(self):
        print("Connecting to Pixhawk...")
        self.connected = True

    def arm(self):
        if self.connected:
            print("Drone Armed")
            self.armed = True
        else:
            print("Connect Drone First")

    def takeoff(self):
        if self.armed:
            print("Taking Off...")
            self.flying = True
        else:
            print("Arm Drone First")

    def land(self):
        if self.flying:
            print("Landing...")
            self.flying = False
        else:
            print("Drone already on ground")