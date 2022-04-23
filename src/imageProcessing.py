# Import necessary libraries.
import cv2 as cv
import numpy as np

# Import PIL sub modules for image processing.
from PIL import Image
from PIL import ImageGrab
from PIL import ImageOps

import mss



# Create imageProcessing class with constructor and image processing variables.
class imageProcessing():
    def __init__(self):
        self.image = None
        self.image_gray = None
        self.image_threshold = None
        self.image_canny = None
        self.image_contours = None

    # Get the image from the screen.
    def screenshot(self, left=0, top=0, width=None, height=None):
        # Get the image from the screen.
        with mss.mss() as sct:
            # Get the size of the screen.
            monitor = {"top": top, "left": left, "width": width, "height": height}
            # Get the image from the screen and convert to the right format.
            img = sct.grab(monitor)
            img = np.array(img)

            # Convert the image to grayscale.
            img = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
            return img

    # Perform template matching on the image.
    def Template_Match(self, image, template):
        # Get the size of the template.
        w, h = template.shape[::-1]

        # Perform match template on the image.
        res = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)

        # Return the coordinates of the template.
        return loc

# Test the imageProcessing class.
if __name__ == "__main__":
    print("Testing imageProcessing class.")
    # Create an instance of the imageProcessing class.
    imageProcessing = imageProcessing()
    # Get the image from the screen.
    image = imageProcessing.screenshot()
    # Perform template matching on the image.
        #loc = imageProcessing.Template_Match(image, template)


    