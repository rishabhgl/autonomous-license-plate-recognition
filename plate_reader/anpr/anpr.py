import cv2 
import pytesseract
import numpy as np 
import imutils


class PlateReader():
    def __init__(self, minR = 4, maxR = 5, debug = False):

        # minR and maxR indicate the minimum and maximum aspect ratios acceptable for an image to be a license plate
        # The debug variable indicates whether the program is in debug mode.

        self.minR = minR
        self.maxR = maxR
        self.debug = debug

    def debug_imshow(self, title, image):
        
        if self.debug == True:
            cv2.imshow(title, image)
            cv2.waitKey(0)
