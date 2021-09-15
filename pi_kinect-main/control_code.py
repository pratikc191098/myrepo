import os
import time

import freenect
import cv2
import numpy as np
from functions import *

import RPi.GPIO as GPIO
from time import sleep
import time
#import keyboard
#import readchar

motorpin_left = 12  # board 32
motorpin_right = 13  # board 33

# Motor1 pins
relay_1 = 5  # board 29
relay_2 = 6  # board 31
relay_3 = 17  # board 11
relay_4 = 26  # board 37

# Motor2 pins
relay_5 = 18  # board 12
relay_6 = 16  # board 36
relay_7 = 24  # board 18
relay_8 = 21  # board 40

GPIO.setwarnings(False)  # disable warnings
GPIO.setmode(GPIO.BCM)  # set pin numbering system
GPIO.setup(motorpin_left, GPIO.OUT)
GPIO.setup(motorpin_right, GPIO.OUT)

# Motor 1
GPIO.setup(relay_1, GPIO.OUT)
GPIO.setup(relay_2, GPIO.OUT)
GPIO.setup(relay_3, GPIO.OUT)
GPIO.setup(relay_4, GPIO.OUT)

# Motor 2
GPIO.setup(relay_5, GPIO.OUT)
GPIO.setup(relay_6, GPIO.OUT)
GPIO.setup(relay_7, GPIO.OUT)
GPIO.setup(relay_8, GPIO.OUT)


pwm_left = GPIO.PWM(motorpin_left, 4000)
# create PWM instance with frequency
pwm_right = GPIO.PWM(motorpin_right, 4000)
pwm_left.start(0)  # start PWM of required Duty Cycle
pwm_right.start(0)  # pi_pwm.ChangeDutyCycle(70)
speed_value = 41
stop_speed = 0

motor_direction_speed = 0.2



def reverse():
    print("reverse")
    # pwm_left.ChangeDutyCycle(stop_speed)
    # pwm_right.ChangeDutyCycle(stop_speed)

    # time.sleep(motor_direction_speed)

    GPIO.output(relay_1, GPIO.LOW)
    GPIO.output(relay_2, GPIO.LOW)
    GPIO.output(relay_3, GPIO.LOW)
    GPIO.output(relay_4, GPIO.LOW)

    GPIO.output(relay_5, GPIO.HIGH)
    GPIO.output(relay_6, GPIO.HIGH)
    GPIO.output(relay_7, GPIO.HIGH)
    GPIO.output(relay_8, GPIO.HIGH)

    time.sleep(motor_direction_speed)

    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)


def left():
    print("left")
    # pwm_left.ChangeDutyCycle(stop_speed)
    # pwm_right.ChangeDutyCycle(stop_speed)

    # time.sleep(motor_direction_speed)

    GPIO.output(relay_1, GPIO.LOW)
    GPIO.output(relay_2, GPIO.LOW)
    GPIO.output(relay_3, GPIO.LOW)
    GPIO.output(relay_4, GPIO.LOW)

    GPIO.output(relay_5, GPIO.LOW)
    GPIO.output(relay_6, GPIO.LOW)
    GPIO.output(relay_7, GPIO.LOW)
    GPIO.output(relay_8, GPIO.LOW)

    time.sleep(motor_direction_speed)

    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)

def forward():
    print("forward")

    # pwm_left.ChangeDutyCycle(stop_speed)
    # pwm_right.ChangeDutyCycle(stop_speed)

    # time.sleep(motor_direction_speed)

    GPIO.output(relay_1, GPIO.HIGH)
    GPIO.output(relay_2, GPIO.HIGH)
    GPIO.output(relay_3, GPIO.HIGH)
    GPIO.output(relay_4, GPIO.HIGH)

    GPIO.output(relay_5, GPIO.LOW)
    GPIO.output(relay_6, GPIO.LOW)
    GPIO.output(relay_7, GPIO.LOW)
    GPIO.output(relay_8, GPIO.LOW)

    time.sleep(motor_direction_speed)

    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)


def right():
    print("right")
    # pwm_left.ChangeDutyCycle(stop_speed)
    # pwm_right.ChangeDutyCycle(stop_speed)

    # time.sleep(motor_direction_speed)

    GPIO.output(relay_1, GPIO.HIGH)
    GPIO.output(relay_2, GPIO.HIGH)
    GPIO.output(relay_3, GPIO.HIGH)
    GPIO.output(relay_4, GPIO.HIGH)

    GPIO.output(relay_5, GPIO.HIGH)
    GPIO.output(relay_6, GPIO.HIGH)
    GPIO.output(relay_7, GPIO.HIGH)
    GPIO.output(relay_8, GPIO.HIGH)

    time.sleep(motor_direction_speed)

    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)


def stop():
    print("stop")
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)


def nothing(x):
    pass


# cv2.namedWindow('edge')
cv2.namedWindow('Video')
cv2.moveWindow('Video', 5, 5)
cv2.namedWindow('Navig', cv2.WINDOW_AUTOSIZE)
cv2.resizeWindow('Navig', 400, 100)
cv2.moveWindow('Navig', 700, 5)
# cv2.namedWindow('Fin')
# cv2.namedWindow('Win')
kernel = np.ones((5, 5), np.uint8)


print('Press \'b\' in window to stop')
cv2.createTrackbar('val1', 'Video', 37, 1000, nothing)
cv2.createTrackbar('val2', 'Video', 43, 1000, nothing)
cv2.createTrackbar('bin', 'Video', 20, 50, nothing)
cv2.createTrackbar('erode', 'Video', 4, 10, nothing)  # after plenty of testing
imn = cv2.imread('blank.bmp')
#cv2.createTrackbar('dilate', 'edge',0,10,nothing)


def pretty_depth(depth):
    np.clip(depth, 0, 2**10 - 1, depth)
    depth >>= 2
    depth = depth.astype(np.uint8)
    return depth


class CLASS_NAME:
    def __init__(self):
        self.variable_name_1 = None
        self.variable_name_2 = None

    def navigate(self, config_values):
        print(config_values)
        while True:
            #print("=========Kinect loop function 1 running-----------------------------")
            try:
                imn = cv2.imread('blank.bmp')
                cv2.imshow('Navig', imn)
                flag120 = [1, 1, 1, 1]
                flag140 = [1, 1, 1, 1]
                f14 = 0
                f12 = 0
                f10 = 0
                f8 = 0
        # get kinect input___________________________2_______________________________________________
                dst = pretty_depth(freenect.sync_get_depth()
                                   [0])  # input from kinect

        # rectangular border (improved edge detection + closed contours)___________________________
                cv2.rectangle(dst, (0, 0), (640, 480), (40, 100, 0), 2)

        # image binning (for distinct edges)________________________________________________________
                binn = cv2.getTrackbarPos('bin', 'Video')
                e = cv2.getTrackbarPos('erode', 'Video')
                dst = (dst/binn)*binn
                dst = cv2.erode(dst, kernel, iterations=e)

        # Video detection___________________________________________________________________________
                v1 = 37
                v2 = 43
                v1 = cv2.getTrackbarPos('val1', 'Video')
                v2 = cv2.getTrackbarPos('val2', 'Video')
                edges = cv2.Canny(dst, v1, v2)

        # finding contours__________________________________________________________________________
                contours, hierarchy = cv2.findContours(
                    edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
                cv2.drawContours(dst, contours, -1, (0, 0, 255), -1)

        # boundingRect approach_______________________________________________________________________
                cv2.createTrackbar('epsilon', 'Video', 1, 100,
                                   nothing)  # for approxPolyDP
                ep = cv2.getTrackbarPos('epsilon', 'Video')

        # defined points approach (to check: runtime)________________________________________________
                cv2.createTrackbar('spacing', 'Video', 30,
                                   100, nothing)  # for approxPolyDP
                spac = cv2.getTrackbarPos('spacing', 'Video')
                (rows, cols) = dst.shape  # 480 rows and 640 cols
                # print cols

                for i in range(rows/spac):  # note the presence of colon
                    for j in range(cols/spac):
                        cv2.circle(dst, (spac*j, spac*i), 1, (0, 255, 0), 1)
                        if (dst[spac*i, spac*j] == 80):
                            f8 = 1
                            cv2.putText(dst, "0", (spac*j, spac*i),
                                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 200, 20), 2)
                            cv2.putText(dst, "Collision Alert!", (30, 30),
                                        cv2.FONT_HERSHEY_TRIPLEX, 1, (2), 1)
                            imn = cv2.imread("Collision Alert.bmp")
                            cv2.imshow('Navig', imn)
                            print("MOVE BACK")
                            config_values.STOPPED = True
                            config_values.MOVING_FORWARD = False
                            config_values.MOVING_BACKWARD = False
                            config_values.MOVING_LEFT = False
                            config_values.MOVE_RIGHT = False

                        if (dst[spac*i, spac*j] == 100):
                            f10 = 1
                            cv2.putText(dst, "1", (spac*j, spac*i),
                                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 200, 20), 2)
                            cv2.putText(dst, "Very Close proximity. Reverse",
                                        (30, 60), cv2.FONT_HERSHEY_TRIPLEX, 1, (2), 1)
                            config_values.STOPPED = False
                            config_values.MOVING_FORWARD = False
                            config_values.MOVING_BACKWARD = True
                            config_values.MOVING_LEFT = False
                            config_values.MOVE_RIGHT = False
                            if(f8 == 0):
                                config_values.STOPPED = False
                                config_values.MOVING_FORWARD = False
                                config_values.MOVING_BACKWARD = True
                                config_values.MOVING_LEFT = False
                                config_values.MOVE_RIGHT = False
                                imn = cv2.imread("VCP Reverse.bmp")
                                cv2.imshow('Navig', imn)
                        if (dst[spac*i, spac*j] == 120):
                            f12 = 1
                            cv2.putText(dst, "2", (spac*j, spac*i),
                                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 200, 20), 2)
                            flag120 = RegionCheck(spac*j, flag120)
                            if(f8 == 0 and f10 == 0):
                                imgshow(flag120, 120, imn, 'Navig')
                                #print("flag120 - :",flag120)

                                # for list_values in flag120:
                                # if list_values==0:
                                try:
                                    index = flag120.index(0)
                                except:
                                    pass
                                # print("index_value",index)
                                # My codes

                                # back
                                if index == 1:
                                    config_values.STOPPED = False
                                    config_values.MOVING_FORWARD = False
                                    config_values.MOVING_BACKWARD = True
                                    config_values.MOVING_LEFT = False
                                    config_values.MOVE_RIGHT = False

                                    # left
                                if index == 2:
                                    config_values.STOPPED = False
                                    config_values.MOVING_FORWARD = False
                                    config_values.MOVING_BACKWARD = False
                                    config_values.MOVING_LEFT = True
                                    config_values.MOVE_RIGHT = False
                                # Right
                                if index == 0:
                                    config_values.STOPPED = False
                                    config_values.MOVING_FORWARD = False
                                    config_values.MOVING_BACKWARD = False
                                    config_values.MOVING_LEFT = False
                                    config_values.MOVE_RIGHT = True

                        if (dst[spac*i, spac*j] == 140):
                            f14 = 1
                            cv2.putText(dst, "3", (spac*j, spac*i),
                                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 200, 20), 1)
                            flag140 = RegionCheck(spac*j, flag140)
                            if(f8 == 0 and f10 == 0 and f12 == 0):
                                #print("flag140 - :",flag140)
                                imgshow(flag140, 140, imn, 'Navig')

                                try:
                                    index = flag140.index(0)
                                except:
                                    pass

                                # back
                                if index == 1:
                                    config_values.STOPPED = False
                                    config_values.MOVING_FORWARD = False
                                    config_values.MOVING_BACKWARD = True
                                    config_values.MOVING_LEFT = False
                                    config_values.MOVE_RIGHT = False

                                    # left
                                if index == 2:
                                    config_values.STOPPED = False
                                    config_values.MOVING_FORWARD = False
                                    config_values.MOVING_BACKWARD = False
                                    config_values.MOVING_LEFT = True
                                    config_values.MOVE_RIGHT = False
                                # Right
                                if index == 0:
                                    config_values.STOPPED = False
                                    config_values.MOVING_FORWARD = False
                                    config_values.MOVING_BACKWARD = False
                                    config_values.MOVING_LEFT = False
                                    config_values.MOVE_RIGHT = True

                        if (dst[spac*i, spac*j] == 160):
                            cv2.putText(dst, "4", (spac*j, spac*i),
                                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 200, 20), 1)
                        if (dst[spac*i, spac*j] == 180):
                            cv2.putText(dst, "5", (spac*j, spac*i),
                                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 200, 20), 1)
                        if (dst[spac*i, spac*j] == 200):
                            config_values.MOVING_FORWARD = True
                            cv2.putText(dst, "6", (spac*j, spac*i),
                                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 200, 20), 1)
                        if (dst[spac*i, spac*j] == 220):
                            config_values.MOVING_FORWARD = True
                            cv2.putText(dst, "7", (spac*j, spac*i),
                                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 200, 20), 1)

        # imshow outputs______________________________________________________________________
                if(flag120[1:3] == [1, 1] and f12 == 1):
                    # print flag, "FWD"
                    cv2.putText(dst, " frwd", (325, 90),
                                cv2.FONT_HERSHEY_DUPLEX, 1, (2), 1)
                elif(flag120[2:4] == [1, 1] and f12 == 1):
                    # print flag, "RIGHT"
                    cv2.putText(dst, " right", (325, 90),
                                cv2.FONT_HERSHEY_DUPLEX, 1, (2), 1)
                elif(flag120[0:2] == [1, 1] and f12 == 1):
                    # print flag, "LEFT"
                    cv2.putText(dst, " left", (325, 90),
                                cv2.FONT_HERSHEY_DUPLEX, 1, (2), 1)
                elif(f12 == 1):
                    # print flag, "BACK"
                    cv2.putText(dst, " back", (325, 90),
                                cv2.FONT_HERSHEY_DUPLEX, 1, (2), 1)
                cv2.line(dst, (130, 0), (130, 480), (0), 1)
                cv2.line(dst, (320, 0), (320, 480), (0), 1)
                cv2.line(dst, (510, 0), (510, 480), (0), 1)
                cv2.imshow('Video', dst)

                if(cv2.waitKey(1) & 0xFF == ord('b')):
                    break

            except KeyboardInterrupt:
                print('Hello user you have pressed ctrl-c button.')
                quit()

    def hub_control(self, config_values):
        try:
            while True:
                # print("config_values",config_values)
                # time.sleep(0.02)
                if config_values.STOPPED == True:
                    print(
                        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx------------------Robot Stopped------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    stop()
                    continue
                elif config_values.MOVING_FORWARD == True:
                    print(
                        "Robot Moving Forward///////////////////////////////////////////////////////////////////////////////////////")
                    forward()
                elif config_values.MOVING_BACKWARD == True:
                    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Robot Moving Backward temporary stopped***********************")
                    reverse()
                elif config_values.MOVING_LEFT == True:
                    print(
                        "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Robot Moving Left")
                    left()
                elif config_values.MOVE_RIGHT == True:
                    print(
                        "Robot Moving Right>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    right()
        except KeyboardInterrupt:
            #config_values.STOPPED = True
            print("Hub control code stopped")
            quit()
