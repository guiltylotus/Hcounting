import numpy as np
import cv2
import time
from myclass import *

_sam = myClass()
cap = cv2.VideoCapture('video/TownCentreXVID.avi')
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
kernel = np.ones((3,3), np.uint8)
kernel11 = np.ones((11,11), np.uint8)
# h = fgbg.getVarThreshold()
# print(h)

count = 0

while(1):
    ret, frame = cap.read()

    if (ret == False):
        break

    fgmask = fgbg.apply(frame)
    fgmask = np.array(fgmask)

    # fgmask[fgmask < 130] = 0
    ret, fgmask = cv2.threshold(fgmask,130,255,cv2.THRESH_BINARY)  #remove shadow
    # thresh = cv2.adaptiveThreshold(fgmask, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 1)
    
    
    # fgmask = cv2.erode(fgmask,kernel,iterations = 1)
    # fgmask = cv2.dilate(fgmask,kernel5,iterations = 2)

    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    # thresh = cv2.dilate(thresh, kernel, iterations=2)
    fgmask = cv2.morphologyEx(fgmask , cv2.MORPH_CLOSE, kernel, iterations=2)
    
    fgmask = cv2.morphologyEx(fgmask , cv2.MORPH_CLOSE, kernel11, iterations=2)
    bb_img = _sam.exContours(fgmask,frame)
    # print(len(contours))
    

    
    # fgmask = _sam.takeSample(fgmask, 100)
    
    cv2.imshow('frame', frame)
    cv2.imshow('fgmask', fgmask)
    time.sleep(0.05)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
    # cv2.waitKey()            
    
cap.release()
cv2.destroyAllWindows()
