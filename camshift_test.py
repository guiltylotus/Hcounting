import numpy as np
import cv2 as cv
import time

cap = cv.VideoCapture('video/slow.mp4')
# take first frame of the video
ret,frame = cap.read()

def click_line(event, x, y, flags, param):
    
    global line
    check_click = False

    if event == cv.EVENT_LBUTTONDOWN:
        check_click = True
        line.append(x)
        line.append(y)

    elif event == cv.EVENT_LBUTTONUP:
        check_click = False
        line.append(x)
        line.append(y)



# setup initial location of window
line = []
cv.namedWindow('frame')
cv.setMouseCallback('frame', click_line)

while(True): 
    cv.imshow("frame", frame)

    time.sleep(0.05)
    k = cv.waitKey(1) & 0xFF

    if k == ord('q'):
        break
    elif k == ord('r'):
        line = []
    elif k == ord('p'):
        print(line)
        x,y,u,v = line  # simply hardcoded the values
        w = abs(x - u)
        h = abs(y - v)
        track_window = (y,x,w,h)
        cv.rectangle(frame,(x,y),(u,v),(0,0,255),1, lineType=cv.LINE_AA)




# set up the ROI for tracking
roi = frame[y:y+h, x:x+w]
hsv_roi =  cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))  #constant
roi_hist = cv.calcHist([hsv_roi],[0],mask,[16],[0,180])
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )
while(1):
    ret ,frame = cap.read()
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        # apply meanshift to get the new location
        ret, track_window = cv.CamShift(dst, track_window, term_crit)
        # Draw it on image
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv.polylines(frame,[pts],True, 255,2)
        cv.imshow('img2',img2)
        cv.imshow('roi', mask)
        k = cv.waitKey(60) & 0xff

        if k == 27:
            break
        else:
            cv.imwrite(chr(k)+".jpg",img2)
    else:
        break
cv.destroyAllWindows()
cap.release()