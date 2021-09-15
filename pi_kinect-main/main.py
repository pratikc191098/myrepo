import freenect
import cv2
import numpy as np
from functions import *

print('Press \'b\' in window to stop')

def pretty_depth(depth):
	np.clip(depth, 0, 2**10 - 1, depth)
	depth >>= 2
	depth = depth.astype(np.uint8)
	return depth
while 1:
    try:
        print("displaying values")
        distance = pretty_depth(freenect.sync_get_depth()[0])
        orig = freenect.sync_get_video()[1] #When web camera is connected index is 1 else 0 
        cv2.imshow('RGB',orig)
        cv2.imshow('Disp', distance)
        if(cv2.waitKey(10) & 0xFF == ord('b')):
            break
    except KeyboardInterrupt:
        print('Hello user you have pressed ctrl-c button.')
        quit()
