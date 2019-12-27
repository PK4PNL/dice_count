import cv2
import sys
import os
from os import listdir
from os.path import isfile, join
import numpy



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
    print("3")
    img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('grayscale', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('grayscale', img1)
    k = cv2.waitKey()
    if k == 27:
        exit()
 
    #add blur to grayscale >> img2
    print("2")
    img2 = cv2.medianBlur(img1, 15)
    cv2.namedWindow('blur', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('blur', img2)
    k = cv2.waitKey()
    if k == 27:
        exit()

    #binary threshold to filter noise >> img3
    print("1")
    ret, img3 = cv2.threshold(img2, 100, 255, 0)
    cv2.namedWindow('bin_thresh', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('bin_thresh', img3)

mypath='img/'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images[n] = detect( join(mypath,onlyfiles[n]) )

cv2.waitKey()
exit()