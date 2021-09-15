import sys
import time
from singelton_config_class import config
config_values = config()

import os

#IF Any enviroment variables needed to be used
#from dotenv import load_dotenv
#load_dotenv()

#VARIABLE1 = os.getenv('VARIABLE1')
#VARIABLE2 = os.getenv('VARIABLE2')

#config_values.VARIABLE1 = VARIABLE1
#config_values.VARIABLE2 = VARIABLE2


import threading
from control_code import CLASS_NAME
from kinect_navigation_class import KINECT_NAVIGATION_CLASS

x= None
while True:
    # Do other things in the meantime here...
    try:
        if x == None or x.is_alive() == False:
            define_class_name = CLASS_NAME()
            secont_class_name = KINECT_NAVIGATION_CLASS()
            x = threading.Thread(target=define_class_name.navigate, args=(config_values,))
            print("starting the x thread")
            x.start()
            
            print("==================+++++++=====================++++++++++++=+=================+=+=+=++=+=+=+=+=++=++=+=++=++==+=+==+=++=")
            
            y = threading.Thread(target=define_class_name.hub_control, args=(config_values,))
            print("starting the y thread")
            y.start()
            break
            

    except KeyboardInterrupt:
        print("exception occured-------------------------------",sys.exc_info()[0])
        quit()
    time.sleep(5)
