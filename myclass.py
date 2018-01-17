import numpy as np 
import cv2

class myClass():

    #sampling
    def takeSample(self,frame, rate):
        h,w = np.shape(frame)

        for i in range(h):
            for j in range(w):
                if (frame[i,j] != 0):
                    r = np.random.randint(100)
                    # print(r)
                    if (r >= rate):
                        frame[i,j] = 0
                
        return frame

    #extract contours
    def exContours(self, img, orImg):
        #input : frame 
        
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
                cv2.rectangle(orImg,(x,y),(x+w,y+h),(128,255,0),2, lineType=cv2.LINE_AA)

        return orImg
        #output: frame + bb

