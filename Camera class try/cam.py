'''
A class for the camera.
The methods of the class are the function called within cv2.
'''
import cv2
import numpy as np

class cam():
    def __init__(self):
        self.lower_color = None
        self.upper_color = None
        self.frame = None
        self.hsv = None
        self.mask = None
        self.res = None
        
    def __init__(self,lower_color,upper_color):
        self.cap = cv2.VideoCapture(0)
        self.lower_color = lower_color
        self.upper_color = upper_color
        self.frame = None
        self.hsv = None
        self.mask = None
        self.res = None
            

    def LiveCapture(self):
        while True:
            self.frame = cap.read()

    def Capture(self):
        self.frame = cap.read()

    '''def ColorToHSV(self,b):
        color = np.unit8(b)
        hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
        return hsv_color'''

    def HSVImage(self):
        self.frame = Capture(self)
        self.hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        return hsv

    def HSVImage(self,frame):
        self.hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        return hsv

    def MaskImage(self):
        self.hsv = HSVImage(self)
        mask = cv2.inRange(hsv, self.lower_color, self.upper_color)
        return mask
    
    def MaskImage(self,hsv):
        self.mask = cv2.inRange(hsv, self.lower_color, self.upper_color)
        return mask

    def ResImage(self):
        self.mask = MaskImage(self)
        res = cv2.bitwise_and(frame,frame, mask=mask)
        return res

    def ResImage(self,frame):
        self.hsv = HSVImage(self,frame)
        self.mask = MaskImage(self,hsv)
        res = cv2.bitwise_and(frame,frame, mask=mask)
        return res

    
    @property
    def ShowFrame(self):
        Capture(self)
        cv2.imshow('frame',self.frame)

    def ShowFrame(self,frame):
        cv2.imshow('frame',frame)

    def ShowHSV(self):
        frame = Capture(self)
        hsv = HSVImage(self,frame)
        cv2.imshow('frame',frame)

    def ShowHSV(self,frame):
        hsv = HSVImage(self,frame)
        cv2.imshow('HSV',hsv)

    def ShowHSV(self,hsv):
        cv2.imshow('HSV',hsv)

    def ShowMask(self):
        frame = Capture(self)
        hsv = HSVImage(self,frame)
        mask = MaskImage(self,hsv)
        cv2.imshow('Mask',mask)

    def ShowMask(self,frame):
        hsv = HSVImage(self,frame)
        mask = MaskImage(self,hsv)
        cv2.imshow('Mask',mask)

    def ShowMask(self,hsv):
        mask = MaskImage(self,hsv)
        cv2.imshow('Mask',mask)

    def ShowMask(self,mask):
        cv2.imshow('Mask',mask)

    def ShowRes(self):
        frame = Capture(self)
        hsv = HSVImage(self,frame)
        mask = MaskImage(self,hsv)
        res = ResImage(self,frame)
        cv2.imshow('Res',res)

    def ShowAll(self):
        ShowFrame(self)
        ShowHSV(self)
        ShowMask(self)
        ShowRes(self)

    def ShowAll(self,frame):
        ShowFrame(self,frame)
        ShowHSV(self,frame)
        ShowMask(self.frame)
        ShowRes(self,frame)

    def Show_HSV_Mask_Res(self):
        ShowHSV(self)
        ShowMask(self)
        ShowRes(self)

    def Show_HSV_Mask_Res(self,frame):
        ShowHSV(self,frame)
        ShowMask(self,frame)
        ShowRes(self,frame)
