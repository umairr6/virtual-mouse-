
import time
import pyautogui


class GestureController:
    def __init__(self, action_delay=0.5):
        self.last_action_time = 0
        self.action_delay = action_delay
        self.prev_scroll_y = None

    def can_perform_action(self):
        current_time = time.time()

        if current_time - self.last_action_time > self.action_delay:
            self.last_action_time = current_time
            return True

        return False

    def handle_gestures(self, landmarks):
        if not landmarks:
            self.prev_scroll_y = None
            return "NO HAND"

        points = {item[0]: (item[1], item[2]) for item in landmarks}

        ix, iy = points[8]
        tx, ty = points[4]
        mx, my = points[12]

        # Thumb + index finger: left click
        
