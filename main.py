import cv2
import sys
import os

def detect(image):
    #read original picture >> img0
    print(image)
    img0 = cv2.imread('' + image)
    cv2.namedWindow('original', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('original', img0)
    k = cv2.waitKey()
    if k == 27:
        exit()

    #convert to grayscale >> img1
    img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('grayscale', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('grayscale', img1)
    k = cv2.waitKey()
    if k == 27:
        exit()
 
    #add blur to grayscale >> img2
    img2 = cv2.medianBlur(img1, 15)
    cv2.namedWindow('blur', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('blur', img2)
    k = cv2.waitKey()
    if k == 27:
        exit()

    #binary threshold to filter noise >> img3
    ret, img3 = cv2.threshold(img2, 100, 255, 0)
    cv2.namedWindow('bin_thresh', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('bin_thresh', img3)

root = "img"
for path, subdirs, files in os.walk(root):
    for name in files:
        detect(name)

cv2.waitKey()
exit()