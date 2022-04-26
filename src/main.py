import threading
from imageProcessing import *


# Create a thread with function as parameter to run
def runThread(func):
    thread = threading.Thread(target=func)
    thread.start()

