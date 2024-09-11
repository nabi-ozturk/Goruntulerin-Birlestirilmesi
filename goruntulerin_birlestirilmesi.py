import cv2
import numpy as np

# resmi içe aktar
img = cv2.imread("dog-7514202_640.jpg")
cv2.imshow("Orijinal", img)

# yatay
hor = np.hstack((img,img))
cv2.imshow("Horizontal", hor)

# dikey
ver = np.vstack((img,img))
cv2.imshow("Vertical", ver)




























