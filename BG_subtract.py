import numpy as np
import cv2
from sample import *

_sam = Sample()
cap = cv2.VideoCapture('video/video3.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True)

count = 0

while(1):
    # count += 1
    # if (count == 40):
    #     break
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask.ShadowThreshold()
    
    # fgmask = _sam.takeSample(fgmask, 100)
    
    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
            break
    
    # cv2.waitKey()            
    
cap.release()
cv2.destroyAllWindows()
