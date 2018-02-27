import cv2
import numpy as np 
import time 

class Person():

    def __init__ (self, id, x, y, w, h, cx, cy):
        self.id = id
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.track = [(cx,cy)]
        self.cy = cy
        self.cx = cx
        self.Pcross = False  # True if cross the line
        self.stt = None  # True = in / False = out
        self.max_age = 5
        self.age = 0
        self.alive = True  # False if cross-line and out range


    def getPos(self):
        return(self.x, self.y, self.w, self.h)

    def updatePos(self, _x, _y, _w, _h):
        self.x = _x
        self.y = _y
        self.w = _w
        self.h = _h
        

    def getCentroid(self):
        return(self.cx, self.cy)

    def updateCentroid(self, _cx, _cy):
        self.cx = _cx
        self.cy = _cy
        self.track.append((_cx,_cy))

    def getID(self):
        return self.id

    def getPcross(self):
        return self.Pcross

    def checkStt(self, _x):
        if (len(self.track) < 2):
            return True

        if (self.track[-2][1] <= _x and self.track[-1][1] > _x):
            self.Pcross = True
            self.stt = True
        elif (self.track[-2][1] >= _x and self.track[-1][1] < _x):
            self.Pcross = True
            self.stt = False
    
        return self.Pcross

    def getStt(self):
        return self.stt

    #check if point in tracking zone
    def checkInrange(self, _x, _y):
        check = False
        
        if (_x <= self.track[-1][1] and self.track[-1][1] <= _y):
            check = True
        
        return check

    def getTrack(self):
        return self.track

    def getAlive(self):
        return self.alive

    def checkAlive(self, _x, _y):
        
        self.age +=1
        if (self.age > self.max_age and not self.checkInrange(_x,_y)):
            self.alive = False
        
        if (not self.alive):
            return False
        
        # bug old person out of range (create a new object)
        # if (len(self.track) > 2):
        #     if (_x <= self.track[-2][1] and self.track[-1][1] < _x):
        #         self.alive = False
        #     elif (_y < self.track[-1][1] and self.track[-2][1] <= _y) :
        #         self.alive = False
                

        if (self.Pcross and not self.checkInrange(_x,_y)):
            self.alive = False

        return self.alive        
        



        
        