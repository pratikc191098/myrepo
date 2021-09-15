import RPi.GPIO as GPIO
from time import sleep
import time
#import keyboard
import readchar

motorpin_left = 32
motorpin_right = 33

#Motor1 pins
relay_1 = 29 
relay_2 = 31
relay_3 = 11
relay_4 = 37

#Motor2 pins
relay_5 = 12
relay_6 = 36
relay_7 = 18 #38
relay_8 = 40

GPIO.setwarnings(False)         #disable warnings
GPIO.setmode(GPIO.BOARD)        #set pin numbering system
GPIO.setup(motorpin_left,GPIO.OUT)
GPIO.setup(motorpin_right,GPIO.OUT)

#Motor 1
GPIO.setup(relay_1,GPIO.OUT)
GPIO.setup(relay_2,GPIO.OUT)
GPIO.setup(relay_3,GPIO.OUT)
GPIO.setup(relay_4,GPIO.OUT)

#Motor 2
GPIO.setup(relay_5,GPIO.OUT)
GPIO.setup(relay_6,GPIO.OUT)
GPIO.setup(relay_7,GPIO.OUT)
GPIO.setup(relay_8,GPIO.OUT)


pwm_left = GPIO.PWM(motorpin_left,4000)
pwm_right = GPIO.PWM(motorpin_right,4000)#create PWM instance with frequency
pwm_left.start(0)#start PWM of required Duty Cycle 
pwm_right.start(0)#pi_pwm.ChangeDutyCycle(70)
speed_value=42
stop_speed=0

def reverse():
    print("reverse")

    
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    
    time.sleep(1)
    
    GPIO.output(relay_1, GPIO.LOW) 
    GPIO.output(relay_2, GPIO.LOW)
    GPIO.output(relay_3, GPIO.LOW) 
    GPIO.output(relay_4, GPIO.LOW)
    
    
    GPIO.output(relay_5, GPIO.HIGH) 
    GPIO.output(relay_6, GPIO.HIGH)
    GPIO.output(relay_7, GPIO.HIGH) 
    GPIO.output(relay_8, GPIO.HIGH)
    
    time.sleep(1)
    
    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)


def right():
    print("right")
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    
    time.sleep(1)
    
    GPIO.output(relay_1, GPIO.LOW) 
    GPIO.output(relay_2, GPIO.LOW)
    GPIO.output(relay_3, GPIO.LOW) 
    GPIO.output(relay_4, GPIO.LOW)
    
    
    
    GPIO.output(relay_5, GPIO.LOW) 
    GPIO.output(relay_6, GPIO.LOW)
    GPIO.output(relay_7, GPIO.LOW) 
    GPIO.output(relay_8, GPIO.LOW)
    
    time.sleep(1)
    
    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)
    
    

def forward():
    print("forward")
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    
    time.sleep(1)
    
    GPIO.output(relay_1, GPIO.HIGH) 
    GPIO.output(relay_2, GPIO.HIGH)
    GPIO.output(relay_3, GPIO.HIGH)
    GPIO.output(relay_4, GPIO.HIGH)

    
    GPIO.output(relay_5, GPIO.LOW) 
    GPIO.output(relay_6, GPIO.LOW)
    GPIO.output(relay_7, GPIO.LOW) 
    GPIO.output(relay_8, GPIO.LOW)
    
    time.sleep(1)
    
    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)

def left():
    print("left")

    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    
    time.sleep(1)
    
    GPIO.output(relay_1, GPIO.HIGH) 
    GPIO.output(relay_2, GPIO.HIGH)
    GPIO.output(relay_3, GPIO.HIGH)
    GPIO.output(relay_4, GPIO.HIGH)

    
    GPIO.output(relay_5, GPIO.HIGH) 
    GPIO.output(relay_6, GPIO.HIGH)
    GPIO.output(relay_7, GPIO.HIGH) 
    GPIO.output(relay_8, GPIO.HIGH)
    
    time.sleep(1)
    
    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)


def stop():
    print("stop")
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    #GPIO.cleanup()
    #GPIO.output(relay_1, GPIO.LOW) #Active le contrôle du GPIO
    #GPIO.output(relay_2, GPIO.LOW)
    

if __name__ == "__main__":
    try:
        while True:
            print("you can enter: up, down, left, right, 1,2,3")
            key = readchar.readkey()
                    
                    
            if(key == None):
                print('stopped')
                continue
                    
            if (key == '\x1b\x5b\x41'): #forward
                print("forward")
                forward()
            if (key == '\x1b\x5b\x42'):#backward
                print("backward")
                reverse()
            if (key == '\x1b\x5b\x44'): #left
                print("left")
                left()
            if (key == '\x1b\x5b\x43'): #right
                print("right")
                right()
            if (key == '1'): #right
                print("breaked")
                quit()
            if (key == '2'): #right
                print("breaked")
                stop()
                
            if (key == '3'): #right
                print("testing relay")
                for i in range(1,8):
                    print("testing relay", i)
                    #GPIO.output(int("relay_"+str(i)), GPIO.HIGH)
                    time.sleep(2)
                    #GPIO.output(int("relay_"+str(i)), GPIO.LOW)
 
    except KeyboardInterrupt:
        print("*************************ended***************************")
