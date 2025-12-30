import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
back = cv2.imread('./image.jpg')

if back is None:
    print("ERROR: image.jpg not found or failed to load")
    cap.release()
    cv2.destroyAllWindows()
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_red = np.array([0, 120, 120])
    u_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, l_red, u_red)

    part1 = cv2.bitwise_and(back, back, mask=mask)

    mask_inv = cv2.bitwise_not(mask)
    part2 = cv2.bitwise_and(frame, frame, mask=mask_inv)

    final = part1 + part2

    cv2.imshow("output", final)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
