import cv2
import numpy as np

img = cv2.imread('./roi.jpg')

# img(y, x)
ball = img[280:340, 330:390]
img[280:340, 100:160] = ball

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
