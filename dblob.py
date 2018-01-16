import cv2
import numpy as np

img = cv2.imread('video/1.PNG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)


img = cv2.bitwise_not(img)
cv2.imshow("gray", img)
cv2.waitKey(0)

#blob detect
# detector = cv2.SimpleBlobDetector_create()
# keypoints = detector.detect(img)
# print(keypoints)

# img_with_keypoint = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#contour
# img, contours, hierarchy = cv2.findContours(img,1,2)
# # print(len(contours))
# # print(contours)

# if (len(contours) != 0):
#     for cnt in contours:
#     # print(cnt)
#         rect = cv2.minAreaRect(cnt)
#         box = cv2.boxPoints(rect)
#         box = np.int0(box)
#         cv2.drawContours(img,[box],0,(0, 0, 255),2)



#centroid
connectivity = 4
num_labels ,output, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity, cv2.CV_32S) 

num_labels = num_labels - 1
centroids = centroids[1:]
size = stats[1:, 4]
centroids = np.array(centroids, dtype= float)
print(centroids)

# cv2.imshow("keypoints", img_with_keypoint)
cv2.imshow("keypoints", img)
cv2.waitKey(0)