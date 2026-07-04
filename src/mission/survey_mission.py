"""
survey_mission.py

Survey Mission Module
"""

from src.mission.waypoint import Waypoint


class SurveyMission:

    def __init__(self):
        self.waypoints = []

    def generate_waypoints(self):

        self.waypoints.append(
            Waypoint(18.5204, 73.8567, 20)
        )

        self.waypoints.append(
            Waypoint(18.5208, 73.8571, 20)
        )

        self.waypoints.append(
            Waypoint(18.5212, 73.8576, 20)
        )

        print("Survey waypoints generated.")

    def show_waypoints(self):

        print("\nSurvey Mission")

        for i, wp in enumerate(self.waypoints):

            print(f"\nWaypoint {i+1}")

            wp.display()

    def execute_mission(self, drone, camera, gps, lidar):

        print("\nMission Started")

        for index, waypoint in enumerate(self.waypoints, start=1):

            print("\n----------------------------------------")

            drone.fly_to_waypoint(index)

            camera.capture()

            gps.update()

            lidar.scan()

        drone.return_home()