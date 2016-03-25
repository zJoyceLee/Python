import numpy as np
import cv2

# read an image-----------------------------------------------------------------
# ('name.xxx',flag)->flag:1 0 -1
img=cv2.imread('1.jpg',1)

# display an image--------------------------------------------------------------
cv2.imshow('image',img)
# waitKey()->keyboard binding function
cv2.waitKey(0)
# simply destroys all the windows we created
cv2.destroyAllWindows()
