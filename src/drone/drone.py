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
        print("🔗 Connecting to Pixhawk...")
        time.sleep(1)
        self.connected = True
        print("✅ Connected")

    def arm(self):
        if self.connected:
            print("🔓 Arming Drone...")
            time.sleep(1)
            self.armed = True
            print("✅ Drone Armed")
        else:
            print("❌ Connect Drone First")

    def takeoff(self):
        if self.armed:
            print("🚀 Taking Off...")
            time.sleep(2)
            self.flying = True
            print("✅ Takeoff Complete")
        else:
            print("❌ Arm Drone First")

    def fly_to_waypoint(self, waypoint_number):
        print(f"\n✈ Flying to Waypoint {waypoint_number}...")
        time.sleep(2)
        print("✅ Arrived")

    def return_home(self):
        print("\n🏠 Returning Home...")
        time.sleep(2)
        print("✅ Home Reached")

    def land(self):
        if self.flying:
            print("\n🛬 Landing...")
            time.sleep(2)
            self.flying = False
            print("✅ Drone Landed")
        else:
            print("Drone already on ground")