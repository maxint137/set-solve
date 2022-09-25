"""To see check if X-system is operational"""
import cv2
import numpy as np



IMG_NAME = './data/set_5296.jpg'

img = cv2.imread(IMG_NAME,1)
cv2.imshow(IMG_NAME,img)



print("Press any key to quit")
cv2.waitKey(0)

