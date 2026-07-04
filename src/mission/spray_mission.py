def execute_mission(self, drone, camera, gps, lidar):

    print("\nMission Started")

    for index, waypoint in enumerate(self.waypoints, start=1):

        print("\n----------------------------------------")

        drone.fly_to_waypoint(index)

        camera.capture()

        gps.update()

        lidar.scan()

    drone.return_home()