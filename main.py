import numpy as np
import cv2
from mss import mss
import pygetwindow as gw
import time

# Specify the title of the window you want to capture
window_title = 'BlueStacks App Player'

# Global variables for frame data, fps calculation, and termination flag
frame = None
fps = 0
frame_count = 0
last_frame_time = time.time()
last_fps_display_time = time.time()  # Time when the FPS was last displayed
terminate = False  # Termination flag
window_check_interval = 60  # Check window size every 60 frames

with mss() as sct:
    window_check_counter = 0
    while not terminate:
        # Update capture region only at intervals
        if window_check_counter % window_check_interval == 0:
            windows = gw.getWindowsWithTitle(window_title)
            if windows:
                window = windows[0]
                mon = {"top": window.top, "left": window.left, "width": window.width, "height": window.height}
            else:
                print("Window not found. Please open the window.")
                time.sleep(1)
                continue
            window_check_counter = 0

        img = sct.grab(mon)
        frame = np.array(img)
        frame_count += 1
        window_check_counter += 1

        # FPS calculation
        current_time = time.time()
        frame_time = current_time - last_frame_time
        last_frame_time = current_time
        fps = 1 / frame_time if frame_time > 0 else 0

        # Display the frame
        if frame is not None:
            cv2.imshow('Live Stream', frame)

        # Update FPS display once per second
        if current_time - last_fps_display_time >= 1:
            print(f"FPS: {fps:.2f}", end='\r')
            last_fps_display_time = current_time

        # Check for 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            terminate = True

    cv2.destroyAllWindows()
