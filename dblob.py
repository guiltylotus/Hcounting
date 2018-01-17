import cv2
import numpy as np

img = cv2.imread('video/f1.PNG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)


# img = cv2.bitwise_not(img)
cv2.imshow("gray", img)
cv2.waitKey(0)


#contour
img, contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# print(len(contours))
# print(contours)

# cv2.drawContours(img, contours, -1, (128,255,0), 3)
if (len(contours) != 0):
    # print(len(contours))
    for cnt in contours:
        #rotate
        # print(cnt)
        # rect = cv2.minAreaRect(cnt)
        # box = cv2.boxPoints(rect)
        # box = np.int0(box)
        # cv2.drawContours(img,[box],0,(128,255,0),2)
        
        #rectangle
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(128,255,0),2)



#centroid
# connectivity = 4
# num_labels ,output, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity, cv2.CV_32S) 

# num_labels = num_labels - 1
# centroids = centroids[1:]
# size = stats[1:, 4]
# centroids = np.array(centroids, dtype= float)
# print(stats)


cv2.imshow("keypoints", img)
cv2.waitKey(0)