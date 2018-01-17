import cv2
import numpy as np 
import sys
import time

def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1) #residual frame
  d2 = cv2.absdiff(t1, t0)
  cv2.imshow('d1', d1)
  cv2.imshow('d2', d2)
  cv2.waitKey(0)
#   print(d1)
  return cv2.bitwise_and(d1, d2)

cap = cv2.VideoCapture('video/video4-4.mp4')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()  #mixture of gaussian BS

# region = (521, 78, 1123, 632)
ret, frame = cap.read()
# if not ret:
#     print "Cannot capture frame!"
#     sys.exit()
# kernel = np.ones((5, 5), np.uint8)
t_minus = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
while ret:
    ret, frame = cap.read()
    if ret:
        # frame = frame[region[1]:region[1]+ region[3], region[0]:region[0]+region[2]]
        fgmask = diffImg(t_minus, t, t_plus)
        cv2.imshow('fgmask', fgmask)
        cv2.imshow('t', t) 
        cv2.imshow('t_plus', t_plus)
        # fgmask = cv2.absdiff(firstFrame, cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))
        # Read next image
        t_minus = t
        t = t_plus
        t_plus = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        thresh = cv2.adaptiveThreshold(fgmask, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 2)
        # ret2, thresh = cv2.threshold(fgmask, 75, 255, cv2.THRESH_BINARY)
        thresh = cv2.bitwise_not(thresh)
        thresh = cv2.dilate(thresh, None, iterations=2)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w*h > 30000:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1, lineType=cv2.LINE_AA)
        # print frame.shape

        # cv2.imshow("frame", frame)
        # cv2.imshow("mask", thresh)
        
        # time.sleep(0.05)
        # k = cv2.waitKey(1)
        # if k & 0xFF == ord('q'):
        #     cv2.waitKey(0)
        #     # box  = cv2.selectROI('area', frame)
        #     # print box
        # elif k == 27:
        #     break
        #     # break
        
        cv2.waitKey(0)
            
            
cap.release()
# out.release()
cv2.destroyAllWindows()


