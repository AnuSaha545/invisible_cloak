import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Camera not opened")
    exit()

print("Camera opened")
print("Stand still. Capturing background in 5 seconds...")

time.sleep(5)   # wait so camera auto-adjusts

ret, back = cap.read()

if ret:
    cv2.imwrite("image.jpg", back)
    print("image.jpg saved successfully")
else:
    print("Failed to capture image")

cap.release()
cv2.destroyAllWindows()
