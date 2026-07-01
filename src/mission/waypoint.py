"""
waypoint.py

Represents one GPS waypoint.
"""


class Waypoint:

    def __init__(self, latitude, longitude, altitude):

        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def display(self):

        print(f"Latitude : {self.latitude}")
        print(f"Longitude: {self.longitude}")
        print(f"Altitude : {self.altitude} m")