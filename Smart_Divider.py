# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:24:57 2019

@author: Shamika
"""
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
import serial #Serial imported for Serial communication
import time #Required to use delay functions


def road_area_detection(img_name) :


    #for i in range(8):
    #    img_name = "traffic" + str(i) + ".jpg"
        
    #READ THE IMAGE AND CORRECT ITS COLOUR
    img = cv2.imread(img_name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    
    #CREATE A COPY OF THE IMAGE AND BLUR IT
    img_copy = img.copy()
    blurred_img = cv2.bilateralFilter(img_copy,10,120,50)
    
    
    #TO FIND THRESHOLD VALUES FOR EDGE DETECTION, CALCULATE MEADIAN OF BLUR IMG
    median_val = np.median(blurred_img)
    
    
    #CALCULATE THRESHOLDS AND TUNE IT ACCORDING TO BRIGHTNESS OF PHOTO
    lower_thresh = max(0,0.7*median_val)
    upper_thresh = min(255,0.7*median_val)
    
    #CALCULATE EDGES IN THE PHOTO BY MODIFYING UPPER THRESHOLD
    edges = cv2.Canny(blurred_img,lower_thresh,upper_thresh+10)
    
    #READ THE EDGES IMAGE AS GRAYSCALE
    edges_copy = edges.copy()
    image,contours,hierarchy = cv2.findContours(edges_copy,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_TC89_L1)
    
    #CREATE A BLACK BACKGROUND OVER WHICH THE DETECTED CONTOURS CAN BE PLOTTED
    contour_img = np.zeros(image.shape, np.uint8)
    
    
    for i in range(len(contours)):
            cv2.drawContours(contour_img,contours,i,255,-1)
            cv2.drawContours(contour_img,contours,i,255,4)    
    
    fig = plt.figure()
    plt.imshow(contour_img, cmap='gray')
    
    
    #Global thresholding for image array
    ret,gray_img = cv2.threshold(contour_img,150,255,cv2.THRESH_BINARY)
    
    #Calculating white space
    gray_img = 1* (gray_img == 255)
    m,n = gray_img.shape
    
    #USE SUM TO CALCULATE ROAD AREA
    road_area = (100-(gray_img.sum()/ (m*n))*100)
    print("")
    print("{} % road visible".format(road_area))
    
    return road_area;



def main(argv) :

    ArduinoSerial = serial.Serial('COM1',9600);
    print (ArduinoSerial.port);
    if (ArduinoSerial.isOpen == False):
                print("going to open")
        
                ArduinoSerial.open()
                time.sleep(2)
        
    
    for i in range(11):
        img_name = "traffic" + str(i) + ".jpg"
        print("")
        print (img_name)
        ra = road_area_detection(img_name);
        time.sleep(2)

        # Experimentally set threshold to 67
        if (ra<=67.0):
            time.sleep(2)
            ArduinoSerial.write(b'A'); 
            #print("im inside zero")
           # time.sleep(1)
        if (ra>67.0):
            time.sleep(2)
            #print("im inside true")
            ArduinoSerial.write(b'B');
           # time.sleep(1);
        
        #ArduinoSerial.close()



if __name__ == '__main__':
    main(sys.argv)
    


