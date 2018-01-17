import numpy as np
import cv2
from myclass import *

_sam = myClass()
cap = cv2.VideoCapture('video/video4-4.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2(history = 10, detectShadows=True)
# h = fgbg.getHistory()
# print(h)

count = 0

while(1):
    # count += 1
    # if (count == 40):
    #     break
    ret, frame = cap.read()

    if (ret == False):
        break

    fgmask = fgbg.apply(frame)
    ret, fgmask = cv2.threshold(fgmask,127,255,cv2.THRESH_BINARY)  #remove shadow
    bb_img = _sam.exContours(fgmask,frame)
    # print(len(contours))

    
    # fgmask = _sam.takeSample(fgmask, 100)
    
    cv2.imshow('frame', frame)
    cv2.imshow('fgmask', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
    # cv2.waitKey()            
    
cap.release()
cv2.destroyAllWindows()
