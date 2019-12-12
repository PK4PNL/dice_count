import cv2
img=cv2.imread("1.jpg")
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("image", img)
cv2.waitKey()
