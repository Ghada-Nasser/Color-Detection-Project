import cv2
import numpy as np 

mycam = cv2.VideoCapture(0)

lowhueval = 0 
lowsatval = 0
lowvalval = 0 

highhueval = 0 
highsatval = 0
highvalval = 0 

box = 50
xpos=ypos=0
def gethuelow (val):
    global lowhueval
    lowhueval = val

def gethuehigh (val):
    global highhueval
    highhueval = val

def getsatlow (val):
    global lowsatval
    lowsatval = val

def getsathigh (val):
    global highsatval
    highsatval = val


def getvallow (val):
    global lowvalval
    lowvalval = val

def getvalhigh (val):
    global highvalval
    highvalval = val

cv2.namedWindow('Trackers')

cv2.createTrackbar('LowHue', 'Trackers', 0, 180, gethuelow)
cv2.createTrackbar('HighHue', 'Trackers', 0, 180, gethuehigh)
cv2.createTrackbar('SatLow', 'Trackers', 0, 255, getsatlow)
cv2.createTrackbar('SatHigh', 'Trackers', 0, 255, getsathigh)
cv2.createTrackbar('ValLow', 'Trackers', 0, 255, getvallow)
cv2.createTrackbar('ValHigh', 'Trackers', 0, 255, getvalhigh)


while True:
    ignore, frame = mycam.read()
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('MymainFrame', frame)

    low = np.array([lowhueval, lowsatval, lowvalval])
    high = np.array([highhueval, highsatval, highvalval])

    mymask = cv2.inRange(hsvFrame, low, high)
    coloredmask = cv2.bitwise_and(frame, frame , mask=mymask)

    contours, ignoe2 = cv2.findContours(mymask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for x in contours:
        area = cv2.contourArea(x)
        if area > box:
            cv2.drawContours(frame, [x],-1,(0,255,0),3)
            xpos, ypos, h, w = cv2.boundingRect(x)
            cv2.rectangle(frame, (xpos, ypos), (int(xpos+w), int(ypos+h)), (255,0,0),3)

    cv2.imshow('MymainFrame', frame)
    cv2.moveWindow('MymainFrame',1080-(xpos),ypos)

    if cv2.waitKey(1) & 0xff == ord('s'):
        break
mycam.release()