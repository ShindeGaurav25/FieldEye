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