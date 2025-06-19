import cv2
import numpy as np
import mss
import pyautogui

zoom = 3.0
size = 100
offset = (50, -350)

with mss.mss() as sct:
    while True:
        mouse_x, mouse_y = pyautogui.position()
        half_size = size // 2
        monitor = {
            "top": mouse_y - half_size,
            "left": mouse_x - half_size,
            "width": size,
            "height": size
        }

        img = np.array(sct.grab(monitor))
        zoomed = cv2.resize(img, (int(size * zoom), int(size * zoom)), interpolation=cv2.INTER_NEAREST)
        cv2.imshow("Zoom Window", zoomed)
        cv2.moveWindow("Zoom Window", mouse_x + offset[0], mouse_y + offset[1])

        if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to quit
            break

    cv2.destroyAllWindows()