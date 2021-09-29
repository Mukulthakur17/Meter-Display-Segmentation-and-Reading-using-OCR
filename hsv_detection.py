import cv2
import numpy as np

def nothing(x):
    pass
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while(True):
    #img_path = "1623404193_0.jpg"
    #img_path = "1622603162_0.jpg"
    img_path = "1623482945_0.jpg"


    frames = cv2.imread(img_path)
    hsv = cv2.cvtColor(frames, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("LH", "Tracking")
    ls = cv2.getTrackbarPos("LS", "Tracking")
    lv = cv2.getTrackbarPos("LV", "Tracking")
    uh = cv2.getTrackbarPos("UH", "Tracking")
    us = cv2.getTrackbarPos("US", "Tracking")
    uv = cv2.getTrackbarPos("UV", "Tracking")

    Lb = np.array([lh, ls, lv])
    Ub = np.array([uh, us, uv])

    mask_C = cv2.inRange(hsv, Lb, Ub)

    Result = cv2.bitwise_and(frames, frames, mask = mask_C)

    cv2.imshow("Recording", frames)
    cv2.imshow("Mask", mask_C)
    cv2.imshow("Result", Result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()