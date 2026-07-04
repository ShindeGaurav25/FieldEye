"""
drone.py

Controls the drone operations.

Developer : Gaurav Shinde
Project : FieldEye
"""

import time


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

    def fly_to_waypoint(self, waypoint_number):
        print(f"Flying to Waypoint {waypoint_number}...")
        time.sleep(2)
        print("✓ Arrived")

    def return_home(self):
        print("\nReturning Home...")
        time.sleep(2)
        print("✓ Home Reached")

    def land(self):
        if self.flying:
            print("Landing...")
            self.flying = False
        else:
            print("Drone already on ground")