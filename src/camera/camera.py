"""
camera.py

RGB Camera Module
"""


class Camera:

    def __init__(self):
        self.camera_status = False

    def start(self):
        print("Camera Started")
        self.camera_status = True

    def capture(self):
        if self.camera_status:
            print("Capturing Image...")
        else:
            print("Camera Not Started")

    def stop(self):
        print("Camera Stopped")
        self.camera_status = False