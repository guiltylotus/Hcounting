import cv2
import numpy as np 
import sys
import time
import myperson
from myclass import *

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1) #residual frame
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)


def click_line(event, x, y, flags, param):
    
    global line
    check_click = False

    if event == cv2.EVENT_LBUTTONDOWN:
        check_click = True
        line.append((x,y))

    elif event == cv2.EVENT_LBUTTONUP:
        check_click = False
        line.append((x,y))

#read
cap = cv2.VideoCapture('video/y1.mp4')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()  #mixture of gaussian BS


ret, frame = cap.read()

#init
first_frame = cap.read()[1]
t_minus = cv2.cvtColor(first_frame, cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(first_frame, cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(first_frame, cv2.COLOR_RGB2GRAY)
line = []
person_list = []
id = 0
fcount = 0
clone = first_frame.copy()
kernel = np.ones((3,3), np.uint8)
kernel11 = np.ones((11,11), np.uint8)
areaTH = 2000
_method = myClass()


#mouse capture
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', click_line)

#setup a visual gate
while(True): 
    cv2.imshow("frame", first_frame)
    
    time.sleep(0.05)
    k = cv2.waitKey(1) & 0xFF

    if k == ord('q'):
        break
    elif k == ord('r'):
        line = []
        first_frame = clone.copy()
    elif k == ord('p'):
        print(line)
        cv2.line(first_frame,line[0],line[1],(0,0,255),5)


#main
while ret:
    ret, frame = cap.read()
    fcount += 1

    if ret:
        # frame = frame[region[1]:region[1]+ region[3], region[0]:region[0]+region[2]]
        fgmask = diffImg(t_minus, t, t_plus)
        
        t_minus = t
        t = t_plus
        t_plus = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        thresh = cv2.adaptiveThreshold(fgmask, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 2)
        # ret2, thresh = cv2.threshold(fgmask, 75, 255, cv2.THRESH_BINARY)
        thresh = cv2.bitwise_not(thresh)
        
        # thresh = cv2.erode(thresh, kernel, iterations = 1)
        # thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        thresh = cv2.dilate(thresh, kernel, iterations=2)
        # thresh = cv2.morphologyEx(thresh , cv2.MORPH_CLOSE, kernel11)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            area = cv2.contourArea(contour)
            x, y, w, h = cv2.boundingRect(contour)
            cv2.drawContours(frame, contour, -1, (0,255,0), 3, 8)
            print("area ", area)
            if area > areaTH:
                # M = cv2.moments(contour)
                # cx = int(M['m10']/M['m00'])
                # cy = int(M['m01']/M['m00'])
                cx,cy = _method.calCentroid(x,y,w,h)
                
                cv2.circle(frame, (cx,cy), 5, (0,0,255), -1)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1, lineType=cv2.LINE_AA)
                
                """ check new person"""
                new = True

                for p in person_list:
                    px, py = p.getCentroid()
                    if (abs(x - px) <= w and abs(y - py) <= h):
                        new = False
                        break
                
                if new:
                    id += 1
                    print("id ", id)
                    p = myperson.Person(id, x, y, w, h, cx, cy)
                    person_list.append(p)
                    print("person pos new", p.getPos())

        """ Track person in list by Meanshift"""
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   #convert to hsv
        mask = cv2.inRange(frame, np.array((0., 60., 32.)), np.array((180., 255., 255.))) 

        print(len(person_list))
        for p in person_list:
            x, y, w, h = p.getPos()
            print("person pos old", p.getPos())
            track_window = (x,y,w,h)
            hsv_roi = hsv[y:y+h, x:x+w]
            mask_roi = mask[y:y+h, x:x+w]

            hist = cv2.calcHist([hsv_roi], [0], mask_roi, [16], [0, 180] ) #histogram of hsv_roi
            cv2.normalize(hist,hist,0,255, cv2.NORM_MINMAX)
            hist = hist.reshape(-1)

            prob = cv2.calcBackProject([hsv], [0], hist, [0, 180], 1)
            prob &= mask
            term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
            track_box, track_window = cv2.CamShift(prob, track_window, term_crit)

            _x, _y, _w, _h = track_window
            p.updatePos(_x, _y, _w, _h)


            # cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0, 0), 1, lineType=cv2.LINE_AA)
            # cv2.rectangle(frame, (_x, _y), (_x + _w, _y + _h), (0, 0, 255), 1, lineType=cv2.LINE_AA)

        


        # cv2.circle(frame, (cx,cy), 5, (0,0,255), -1)

        cv2.line(frame,line[0],line[1],(0,0,255),5)
        cv2.imshow("frame", frame)
        cv2.imshow("mask", thresh)
        
        time.sleep(0.05)
        # k = cv2.waitKey(1)
        # if k & 0xFF == ord('q'):
        #     cv2.waitKey(0)

        # elif k == 27:
        #     break
     
        cv2.waitKey(0)
            
            
cap.release()
cv2.destroyAllWindows()


