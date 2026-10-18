import cv2
import pyautogui
import time
from hand_tracking import HandTracker
from utils import map_value

pyautogui.FAILSAFE = False

screen_w, screen_h = pyautogui.size()

cap = cv2.VideoCapture(0)
tracker = HandTracker()

last_action_time = 0
ACTION_DELAY = 0.5

prev_scroll_y = None

# ---------- SMOOTHING ----------
SMOOTHING = 7
prev_mouse_x, prev_mouse_y = 0, 0

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    frame = tracker.find_hands(frame)
    lm = tracker.get_landmarks(frame)

    if lm:
        # ---------- INDEX FINGER (MOVE) ----------
        _, ix, iy = lm[8]
        target_x = map_value(ix, 0, w, 0, screen_w)
        target_y = map_value(iy, 0, h, 0, screen_h)

        # Smooth movement
        curr_x = prev_mouse_x + (target_x - prev_mouse_x) / SMOOTHING
        curr_y = prev_mouse_y + (target_y - prev_mouse_y) / SMOOTHING

        pyautogui.moveTo(curr_x, curr_y)

        prev_mouse_x, prev_mouse_y = curr_x, curr_y

        # ---------- THUMB + INDEX (LEFT CLICK) ----------
        _, tx, ty = lm[4]
        if abs(ix - tx) < 25 and abs(iy - ty) < 25:
            if time.time() - last_action_time > ACTION_DELAY:
                pyautogui.click()
                last_action_time = time.time()
                cv2.putText(frame, "LEFT CLICK", (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 0, 255), 2)

        # ---------- INDEX + MIDDLE (RIGHT CLICK) ----------
        _, mx, my = lm[12]
        if abs(ix - mx) < 30 and abs(iy - my) < 30:
            if time.time() - last_action_time > ACTION_DELAY:
                pyautogui.rightClick()
                last_action_time = time.time()
                cv2.putText(frame, "RIGHT CLICK", (20, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 0, 0), 2)

        # ---------- SCROLL ----------
        _, idx_joint_x, idx_joint_y = lm[6]
        _, mid_joint_x, mid_joint_y = lm[10]

        index_up = iy < idx_joint_y
        middle_up = my < mid_joint_y

        if index_up and middle_up:
            if prev_scroll_y is not None:
                diff = prev_scroll_y - iy
                if abs(diff) > 8:
                    pyautogui.scroll(int(diff * 2))
                    cv2.putText(frame, "SCROLL", (20, 120),
                                cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 255, 0), 2)
            prev_scroll_y = iy
        else:
            prev_scroll_y = None

        # ---------- VISUALS ----------
        cv2.circle(frame, (ix, iy), 8, (0, 255, 0), cv2.FILLED)
        cv2.circle(frame, (tx, ty), 8, (255, 0, 0), cv2.FILLED)
        cv2.circle(frame, (mx, my), 8, (0, 0, 255), cv2.FILLED)

    cv2.imshow("Smooth Virtual Hand Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
