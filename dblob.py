import cv2
import numpy as np
from myclass import *

_method = myClass()

img = cv2.imread('video/1.PNG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# line = []
clone = img.copy()

# img = cv2.bitwise_not(img)
# cv2.imshow("gray", img)
# cv2.waitKey(0)
def click_line(event, x, y, flags, param):

    global line
    check_click = False

    if event == cv2.EVENT_LBUTTONDOWN:
        check_click = True
        line.append((x,y))

    elif event == cv2.EVENT_LBUTTONUP:
        check_click = False
        line.append((x,y))

        

#contour
img, contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawContours(img, contours, -1, (128,255,0), 3)
if (len(contours) != 0):
    for cnt in contours:       
        #rectangle
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(128,255,0),2)

#mouse click
cv2.namedWindow('image')
line = cv2.setMouseCallback("image", _method.click_line)


#centroid
# connectivity = 4
# num_labels ,output, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity, cv2.CV_32S) 

# num_labels = num_labels - 1
# centroids = centroids[1:]
# size = stats[1:, 4]
# centroids = np.array(centroids, dtype= float)
# print(stats)

while(1):
    cv2.imshow("image", img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print(line)
    elif k == ord('r'):
        img = clone.copy()
        line = []
        

# cv2.waitKey(0)


cv2.destroyAllWindows()