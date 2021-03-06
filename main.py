import cv2
# import sys
# import os
from os import listdir
from os.path import isfile, join
import numpy as np

def detect(image):
    # read original picture >> img0
    print("filename: ", image)
    img0 = cv2.imread('' + image)
    """
    cv2.namedWindow('original', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('original', img0)
    k = cv2.waitKey()
    if k == 27:
        exit()
    """
    # convert to grayscale >> img1
    img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    """
    cv2.namedWindow('grayscale', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('grayscale', img1)
    k = cv2.waitKey()
    if k == 27:
        exit()
    """
    # add blur to grayscale >> img2
    img2 = cv2.medianBlur(img1, 19)
    """
    cv2.namedWindow('blur', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('blur', img2)
    k = cv2.waitKey()
    if k == 27:
        exit()
    """
    # binary threshold to filter noise >> img3
    ret, img3 = cv2.threshold(img2, 100, 255, 0)
    # optional: Gaussian adaptive threshold algorythm
    #img3 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 63, 5) 

    # Read image
    im = img3
    
    # Setup SimpleBlobDetector parameters. source: https://www.learnopencv.com/blob-detection-using-opencv-python-c/
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 10
    params.maxThreshold = 200

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 100

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.2

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.87
        
    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.01

    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs.
    keypoints = detector.detect(im)
    dots = len(keypoints)
    print("keypoints: ", dots)

    if dots > 0:
        
        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
        # the size of the circle corresponds to the size of blob

        im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Write number of blobs to image
        position = (10,50)
        cv2.putText(
            im_with_keypoints, #numpy array on which text is written
            str(dots), #text
            position, #position at which writing has to start
            cv2.FONT_HERSHEY_COMPLEX, #font family
            1, #font size
            (0, 0, 255), #font color
            3) #font stroke
        
        # Show blobs
        cv2.imshow("Keypoints", im_with_keypoints)

    else:
        print("No dots found, inverting")
        img4 = cv2.bitwise_not(img3)
        
        # Setup SimpleBlobDetector parameters.
        params = cv2.SimpleBlobDetector_Params()

        # Change thresholds
        params.minThreshold = 10
        params.maxThreshold = 200

        # Filter by Color
        params.blobColor = 0

        # Filter by Area.
        params.filterByArea = True
        params.minArea = 100

        # Filter by Circularity
        params.filterByCircularity = True
        params.minCircularity = 0.2

        # Filter by Convexity
        params.filterByConvexity = True
        params.minConvexity = 0.87
            
        # Filter by Inertia
        params.filterByInertia = True
        params.minInertiaRatio = 0.01

        # Create a detector with the parameters
        detector = cv2.SimpleBlobDetector_create(params)

        # Detect blobs.
        keypoints = detector.detect(img4)
        dots = len(keypoints)
        print("keypoints: ", dots)

        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
        # the size of the circle corresponds to the size of blob

        im_with_keypoints = cv2.drawKeypoints(img4, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Write number of blobs to image
        position = (10,50)
        cv2.putText(
            im_with_keypoints, #numpy array on which text is written
            str(dots), #text
            position, #position at which writing has to start
            cv2.FONT_HERSHEY_COMPLEX, #font family
            1, #font size
            (0, 0, 255), #font color
            3) #font stroke
        
        # Show blobs
        cv2.imshow("Keypoints", im_with_keypoints)

    k = cv2.waitKey()
    if k == 27:
        exit()

    

mypath='img/' # subfolder name with image files
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ] # list of filenames
images = np.empty(len(onlyfiles), dtype=object) # list of relative path of files (subfolder + filename)
for n in range(0, len(onlyfiles)):
  images[n] = detect( join(mypath,onlyfiles[n]) )

cv2.waitKey()
exit()