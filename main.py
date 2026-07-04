from src.drone.drone import Drone
from src.camera.camera import Camera
from src.gps.gps import GPS
from src.lidar.lidar import LiDAR
from src.mission.survey_mission import SurveyMission


def main():

    print("=" * 50)
    print("FIELD EYE")
    print("=" * 50)

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

    print("\nMission Completed Successfully")


if __name__ == "__main__":
    main()