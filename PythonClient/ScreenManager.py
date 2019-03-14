import mss
from PIL import Image
import numpy as np


class ScreenManager:
    #Handles taking pictures
    __sct = None
    #The picture
    __currentCap = None

    def __init__(self):
        self.__sct = mss.mss()

    #Takes a picture of Monitor #1
    def capture(self):
        self.__currentCap = self.__sct.grab(self.__sct.monitors[1])

    #Returns PIL image of current "frame"
    def getCap(self):
        return Image.frombytes("RGB", self.__currentCap.size, self.__currentCap.bgra, "raw", "BGRX")

    def getCurrentCap(self):
        return self.__currentCap

    #OpenCV likes Numpy arrays, and it's faster than PIL
    def getAsNP(self):
        return np.array(self.__currentCap)
