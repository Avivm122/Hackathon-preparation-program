'''
A class for the camera.
The methods of the class are the function called within cv2.
'''
import cv2
import numpy as np

class cam():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
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

            
    def Capture(self):
        ret, self.frame = self.cap.read()

    def HSVImage(self):
        self.Capture()
        self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

    def MaskImage(self):
        self.HSVImage()
        self.mask = cv2.inRange(self.hsv, self.lower_color, self.upper_color)
    
    def ResImage(self):
        self.MaskImage()
        self.res = cv2.bitwise_and(self.frame,self.frame,mask=self.mask)
    
    def ShowFrame(self):
        self.Capture()
        cv2.imshow('frame',self.frame)

    def ShowHSV(self):
        self.Capture()
        self.HSVImage()
        cv2.imshow('HSV',self.hsv)      

    def ShowMask(self):
        self.Capture()
        self.HSVImage()
        self.MaskImage()
        cv2.imshow('Mask',self.mask)

    def ShowRes(self):
        self.Capture()
        self.HSVImage()
        self.MaskImage()
        self.ResImage()
        cv2.imshow('Res',self.res)

    def Show_HSV_Mask_Res(self):
        self.Capture()
        self.ShowHSVAll()
        self.ShowMaskAll()
        self.ShowResAll()

    #Show all special methods begin
    '''For a faster process ive created an ShowSomethingAll
       The diffrence is not taking another frame each time.
       Shorter process time and same frame process.'''
    def ShowFrameAll(self):
        self.Capture()
        cv2.imshow('frame',self.frame)

    def ShowHSVAll(self):
        self.HSVImage()
        cv2.imshow('HSV',self.hsv)

    def ShowMaskAll(self):
        self.MaskImage()
        cv2.imshow('Mask',self.mask)

    def ShowResAll(self):
        self.ResImage()
        cv2.imshow('Res',self.res)

    #Show all special methods end

    def ShowAll(self):
        self.ShowFrameAll()
        self.ShowHSVAll()
        self.ShowMaskAll()
        self.ShowResAll()

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()



if __name__ == '__main__':
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    cam = cam(lower_blue,upper_blue)
    while True:
        cam.ShowAll()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
