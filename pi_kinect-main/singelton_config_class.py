# Singleton Borg pattern

import json
class config: 
  
    # state shared by each instance 
    __shared_state = dict() 
  
    # constructor method 
    def __init__(self): 
  
        self.__dict__ = self.__shared_state 
        self.MOVING_FORWARD = False
        self.MOVING_BACKWARD = False
        self.MOVING_LEFT = False
        self.MOVE_RIGHT = False
        self.STOPPED = False

    def __str__(self): 
  
        return json.dumps({'STOPPED' : self.STOPPED, 'MOVING_BACKWARD': self.MOVING_BACKWARD})

if "__main__" == __name__:
    config_values = config()
    print(config_values)
