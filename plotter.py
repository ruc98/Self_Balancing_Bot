import serial
import re
import time
import matplotlib.pyplot as plt
import numpy as np
from drawnow import *
from drawnow import drawnow

ser =serial.Serial('/dev/cu.usbmodem1411',9600,timeout=None)
x=0
y=0
i=0
accelX=[]
accelY=[]
accelZ=[]

plt.ion()
cnt=0


def makeFig():
    plt.title('Sensor Data')   #Set the title
    plt.grid(True)
    plt.ylabel('Axis Acceleration')
    plt.plot(accelX,'ro-',label='Raw X Acceleration')
    plt.legend(loc='upper left')
    plt2=plt.twinx()         #create a new object of plt2
    plt.plot(accelY,'b^-',label='Raw Y Acceleration')
    plt2.legend(loc='center right')
    plt3 = plt.twinx()
    plt.plot(accelZ, 'go-', label='Raw Z Acceleration')
    plt.legend(loc='upper right')
    plt.pause(.000001) 
    
    
while 1:
    i+=1
    try:
        a=ser.readline()
        c=a.decode('ASCII')
        #time.sleep(0.01)
    except ser.SerialTimeoutException:
        print('Data could not be read')
        time.sleep(1)
    data=c.split()
    print(data)

    if(i<3):
        continue
    else:
        xAxis=int(data[0])
        yAxis=int(data[1])
        zAxis=int(data[2])
        accelX.append(xAxis)
        accelY.append(yAxis)
        accelZ.append(zAxis)
        drawnow(makeFig)
        plt.pause(.0000001)
        cnt+=1
        
        if(cnt>50):
            accelX.pop(0)
            accelY.pop(0)
            accelZ.pop(0)
            