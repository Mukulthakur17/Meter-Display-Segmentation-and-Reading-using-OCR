import os
import cv2
import numpy as np
import pytesseract

img_path = "1623404193_0.jpg"
#img_path = "1622603162_0.jpg"
#img_path = "1623482945_0.jpg"

img = cv2.imread(img_path)
imgArr = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
roi_lower = np.array([30, 25, 110])
roi_upper = np.array( [75, 255, 255])
mask = cv2.inRange(imgArr, roi_lower, roi_upper)

# Bitwise-AND mask and original image
imgArr = cv2.bitwise_and(img,img, mask= mask)


# Find contours
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

 
# getting bounding boxes having a minimum area
# this large area is surely to contain the output values
digits = dict() 
for (i, c) in enumerate(contours):
  if cv2.contourArea(c)>8000:

    (x, y, w, h) = cv2.boundingRect(c)
    roi = img[y:y + h, x:x + w]
    digits[i] = roi
    break


cv2.imwrite('snap.jpg', digits[i])
cv2.imshow('Win',digits[i])

if cv2.waitKey(-1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

# we just need the numbers
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
custom_config = r'--oem 3 --psm 7 outbase digits'
num = pytesseract.image_to_string(digits[i], config=custom_config)
print(num)