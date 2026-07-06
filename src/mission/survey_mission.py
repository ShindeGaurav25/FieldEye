"""
survey_mission.py

Survey Mission Module
Developer : Gaurav Shinde
Project : FieldEye
"""

from src.mission.waypoint import Waypoint


class SurveyMission:

    def __init__(self):
        self.waypoints = []

    def generate_waypoints(self):
        self.waypoints.append(Waypoint(18.5204, 73.8567, 20))
        self.waypoints.append(Waypoint(18.5208, 73.8571, 20))
        self.waypoints.append(Waypoint(18.5212, 73.8576, 20))

        print("Survey waypoints generated.")

    def show_waypoints(self):

        print("\nSurvey Mission")

        for index, waypoint in enumerate(self.waypoints, start=1):

            print(f"\nWaypoint {index}")

            waypoint.display()

    def execute_mission(self, drone, camera, gps, lidar):

        print("\n======================================")
        print("FIELD EYE SURVEY MISSION")
        print("======================================")

        total_waypoints = len(self.waypoints)

        for index, waypoint in enumerate(self.waypoints, start=1):

            print("\n--------------------------------------")
            print(f"Waypoint {index}/{total_waypoints}")

            drone.fly_to_waypoint(index)

            print("📷 Capturing RGB Image...")
            camera.capture()

            print("📍 Reading GPS...")
            gps.update()

            print("📡 Scanning LiDAR...")
            lidar.scan()

            progress = (index / total_waypoints) * 100

            print(f"Mission Progress : {progress:.0f}%")

        drone.return_home()