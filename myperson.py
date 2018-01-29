import cv2
import numpy as np 
import time 

class Person():

    def __init__ (self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.track = []

    def getPos(self):
        return(self.x, self.y)

    def updatePos(self, _x, _y):
        self.x = _x
        self.y = _y
        self.track.append((_x,_y))

    def getID():
        return self.id

        
        