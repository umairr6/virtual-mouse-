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
        if abs(ix - tx) < 25 and abs(iy - ty) < 25:
            if self.can_perform_action():
                pyautogui.click()
                return "LEFT CLICK"

        # Index + middle finger: right click
        if abs(ix - mx) < 30 and abs(iy - my) < 30:
            if self.can_perform_action():
                pyautogui.rightClick()
                return "RIGHT CLICK"

        # Index and middle fingers raised: scroll
        _, index_joint_y = points[6]
        _, middle_joint_y = points[10]

        index_up = iy < index_joint_y
        middle_up = my < middle_joint_y

        if index_up and middle_up:
            if self.prev_scroll_y is not None:
                diff = self.prev_scroll_y - iy

                if abs(diff) > 8:
                    pyautogui.scroll(int(diff * 2))
                    self.prev_scroll_y = iy
                    return "SCROLL"

            self.prev_scroll_y = iy
        else:
            self.prev_scroll_y = None

        return "MOVE"
