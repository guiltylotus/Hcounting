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
        self.track = []
        self.cy = cy
        self.cx = cx
        self.alive = True
        self.stt = None  # True = in / False = out
        self.max_age = 5


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

    def getAlive(self):
        return self.alive

    def checkAlive(self, _x):
        if (len(self.track) < 2):
            return True

        if (self.track[-2][1] <= _x and self.track[-1][1] > _x):
            self.alive = False
            self.stt = True
        elif (self.track[-2][1] >= _x and self.track[-1][1] < _x):
            self.alive = False
            self.stt = False
    
        return self.alive

    def getStt(self):
        return self.stt


        
        