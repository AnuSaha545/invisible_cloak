# Invisibility Cloak using OpenCV

A real-time computer vision project that implements an invisibility cloak effect by detecting red color in a live video stream and replacing it with a previously captured background image using OpenCV.

---

##  Technologies Used

- Python 3
- OpenCV (cv2)
- NumPy

---

##  Key Features

- Real-time webcam video processing  
- HSV-based color detection for better accuracy  
- Background replacement using image masking  
- Works completely offline  
- Clean and minimal project setup  
- Easy to understand and modify  

---

##  How It Works

1. A clean background image is captured with no subject present.
2. Live video frames are read from the webcam.
3. Each frame is converted from BGR to HSV color space.
4. A predefined HSV range is used to detect red color.
5. A binary mask is created to isolate the red regions.
6. Bitwise operations replace the detected region with background pixels.
7. The final output is displayed in real time.
