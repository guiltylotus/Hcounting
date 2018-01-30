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


    def getPos(self):
        return(self.x, self.y, self.w, self.h)

    def updatePos(self, _x, _y, _w, _h):
        self.x = _x
        self.y = _y
        self.x = _w
        self.y = _h
        self.track.append((_x,_y))

    def getCentroid(self):
        return(self.cx, self.cy)

    def getID():
        return self.id

        
        