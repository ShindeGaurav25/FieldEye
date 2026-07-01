from src.drone.drone import Drone
from src.camera.camera import Camera
from src.gps.gps import GPS
from src.lidar.lidar import LiDAR


def main():

    drone = Drone()

    camera = Camera()

    gps = GPS()

    lidar = LiDAR()

    drone.connect()

    drone.arm()

    drone.takeoff()

    camera.start()

    camera.capture()

    gps.update()

    lidar.scan()

    drone.land()

    camera.stop()


if __name__ == "__main__":
    main()