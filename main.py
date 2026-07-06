import time

from src.drone.drone import Drone
from src.camera.camera import Camera
from src.gps.gps import GPS
from src.lidar.lidar import LiDAR
from src.mission.survey_mission import SurveyMission


def main():

    print("=" * 50)
    print("FIELD EYE")
    print("=" * 50)

    start_time = time.time()

    drone = Drone()
    camera = Camera()
    gps = GPS()
    lidar = LiDAR()

    mission = SurveyMission()

    mission.generate_waypoints()
    mission.show_waypoints()

    drone.connect()
    drone.arm()
    drone.takeoff()

    camera.start()

    mission.execute_mission(
        drone,
        camera,
        gps,
        lidar
    )

    drone.land()
    camera.stop()

    end_time = time.time()

    print("\n======================================")
    print("MISSION SUMMARY")
    print("======================================")
    print("Mission Status : SUCCESS")
    print(f"Total Waypoints : {len(mission.waypoints)}")
    print(f"Mission Time : {end_time-start_time:.2f} seconds")
    print(f"Images Captured : {len(mission.waypoints)}")
    print(f"GPS Points : {len(mission.waypoints)}")
    print(f"LiDAR Scans : {len(mission.waypoints)}")
    print("======================================")


if __name__ == "__main__":
    main()