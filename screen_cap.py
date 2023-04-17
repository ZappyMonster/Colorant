import numpy as np
import threading
from mss import mss
from PIL import Image
import time

class ScreenCapture:
    def __init__(self, x, y, xfov, yfov):
        self.x, self.y, self.xfov, self.yfov = x, y, xfov, yfov
        self.screen = np.zeros((yfov, xfov, 3), np.uint8)
        self.pillow_image = None
        self.lock = threading.Lock()
        self.frame_count = 0
        self.start_time = time.time()
        self.capturethread()

    def capturethread(self):
        capture_thread = threading.Thread(target=self.capture, daemon=True)
        capture_thread.start()

    def capture(self):
        while True:
            with mss() as sct, self.lock:
                monitor = sct.monitors[0]
                top, left = monitor["top"] + self.y, monitor["left"] + self.x
                monitor = {"top": self.y, "left": self.x, "width": self.xfov, "height": self.yfov, "monitor": 0}
                self.pillow_image = sct.grab(monitor)
                self.screen = np.array(self.pillow_image)
                self.fps()

    def fps(self):
        self.frame_count += 1
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= 1:
            fps = self.frame_count / elapsed_time
            print(f" FPS: {fps:.0f}", end="\r")
            self.frame_count = 0
            self.start_time = time.time()

    def get_screen(self):
        with self.lock:
            return self.screen
