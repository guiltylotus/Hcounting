import numpy as np
import cv2
from sample import *

_sam = Sample()
cap = cv2.VideoCapture('video/video1.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True)

count = 0

while(1):
    # count += 1
    # if (count == 40):
    #     break
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, fgmask = cv2.threshold(fgmask,127,255,cv2.THRESH_BINARY)  #remove shadow
    fgmask, contours, hierarchy = cv2.findContours(fgmask,1,2)
    # print(len(contours))

    if (len(contours) != 0):
        cnt = contours[0]
        # print(cnt)
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(fgmask,[box],0,(0,0,255),2)
    
    # fgmask = _sam.takeSample(fgmask, 100)
    
    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
    # cv2.waitKey()            
    
cap.release()
cv2.destroyAllWindows()
