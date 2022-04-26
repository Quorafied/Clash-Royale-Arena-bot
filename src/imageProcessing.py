# Import necessary libraries.
from pipes import Template
import cv2 as cv
import numpy as np
import time
import threading

# Import PIL sub modules for image processing.
from PIL import Image
from PIL import ImageGrab
from PIL import ImageOps

import mss



# Create imageProcessing class with constructor and image processing variables.
class imageProcessing():
    def __init__(self):
        self.image = None
        self.image_copy = None
        self.image_gray = None
        self.image_threshold = None
        self.image_canny = None
        self.image_contours = None

        self.templates = ["head.jpg", "dog.jpg", "goblin.jpg"]
        self.template = None
        self.template_gray = None

    def findImage(self):
        max_loc, max_val = self.Template_Match(self.image_gray, self.template)
        if max_val > 0.8:
            print("We found the image!")
            # Put a rectangle around the image.
            cv.rectangle(self.image_copy, max_loc, (max_loc[0] + self.template.shape[1], max_loc[1] + self.template.shape[0]), (0, 0, 255), 2)

        else:
            print("We didn't find the image.")

        

    def screenshot(self, left=0, top=0, width=1400, height=900):
        # Get the image from the screen.
        with mss.mss() as sct:
            # Get the size of the screen.
            monitor = sct.grab({"top": top, "left": left, "width": width, "height": height})

            # Get the image from the screen and convert to the right format.
            img = np.array(monitor)
            img = cv.cvtColor(img, cv.IMREAD_COLOR)
            return img

    # Perform template matching on the image.
    def Template_Match(self, image, template):
        # Get the size of the template.
        #w, h = template.shape[::-1]

        # Perform match template on the image.
        res = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)

        _, max_val, _, max_loc = cv.minMaxLoc(res)
        # Return the coordinates of the template.
        return (max_loc, max_val)

    def resizeImage(self, image, percentage):
        scale_percent = percentage
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resizedImage = cv.resize(image, dim, interpolation = cv.INTER_AREA)
        return resizedImage

# Test the imageProcessing class.
if __name__ == "__main__":
    print("Testing imageProcessing class.")
    # Create an instance of the imageProcessing class.
    imageProcessing = imageProcessing()
    imageProcessing.image = imageProcessing.screenshot()
    imageProcessing.image_copy = imageProcessing.screenshot()
    imageProcessing.image_gray = cv.cvtColor(imageProcessing.image, cv.COLOR_BGR2GRAY)
    imageProcessing.template = cv.imread(imageProcessing.templates[2], 0)
    
    def grabAndFind():
        # clear image
        imageProcessing.image = imageProcessing.screenshot()
        imageProcessing.image_copy = imageProcessing.screenshot()

        imageProcessing.image_gray = cv.cvtColor(imageProcessing.image, cv.COLOR_BGR2GRAY)
        imageProcessing.findImage()

    

    while True:
        grabAndFind()

        # show image
        cv.imshow("resimage", imageProcessing.image_copy)
        
        # wait for key press
        key = cv.waitKey(1)
        # if 'q' is pressed, exit program
        if key == ord('q'):
            break
        
    


    