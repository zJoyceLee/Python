import cv2
import numpy as np

img = cv2.imread('./2.jpg')
taskImg = img.copy()

# part1 = img[175:620, 60:170]
# cv2 .imshow('Part1', part1)
# part2 = img[175:620, 170:255]
# cv2.imshow('Part2', part2)
# part3 = img[175:620, 255:385]
# cv2.imshow('Part3', part3)
# part4 = img[175:620, 385:500]
# cv2.imshow('Part4', part4)
# part5 = img[175:620, 500:580]
# cv2.imshow('Part5', part5)
# part6 = img[175:620, 580:680]
# cv2.imshow('Part6', part6)
# part7 = img[175:620, 680:800]
# cv2.imshow('Part7', part7)
# part8 = img[175:620, 800:900]
# cv2.imshow('Part8', part8)

#1, 2, 3, 4, 5, 6, 7, 8
#5, 1, 8, 3, 6, 4, 7, 2
taskImg[175:620, 60:140] = img[175:620, 500:580]
taskImg[175:620, 140:250] = img[175:620, 60:170]
taskImg[175:620, 250:350] = img[175:620, 800:900]
taskImg[175:620, 350:480] = img[175:620, 255:385]
taskImg[175:620, 480:580] = img[175:620, 580:680]
taskImg[175:620, 580:695] = img[175:620, 385:500]
taskImg[175:620, 695:815] = img[175:620, 680:800]
taskImg[175:620, 815:900] = img[175:620, 170:255]

cv2.imshow('taskImg', taskImg)


cv2.waitKey(0)
cv2.destroyAllWindows()
