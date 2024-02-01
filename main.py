import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    frame = cap.read()

    cv2.imshow("frame", frame)

    blue = frame[:, :, :1]
    green = frame[:, :, 1:2]
    red = frame[:, :, 2:]

    b_mean = np.mean(blue)
    g_mean = np.mean(green)
    r_mean = np.mean(red)

    if b_mean > g_mean and b_mean > r_mean:
        print("blue")
    elif g_mean > b_mean and g_mean > r_mean:
        print("green")
    else:
        print("red")

    if cv2.waitKey(0) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

