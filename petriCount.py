# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 14:15:44 2018

@author: adams
"""

import cv2
import numpy as np

blue = [(87,114,99),(130,134,107)] # lower and upper 
green = [(0,240,0),(10,255,10)]
yellow = [(0,240,250),(10,255,255)]
dot_colors = [blue]

img = cv2.imread('./images/dots2.jpg')   
# apply medianBlur to smooth image before threshholding
blur= cv2.medianBlur(img, 7) # smooth image by 7x7 pixels, may need to adjust a bit

for lower, upper in dot_colors:
    output = img.copy()
    # apply threshhold color to white (255,255, 255) and the rest to black(0,0,0)
    mask = cv2.inRange(blur,lower,upper) 

    circles = cv2.HoughCircles(mask,cv2.HOUGH_GRADIENT,1,20,param1=20,param2=8,
                               minRadius=0,maxRadius=60)    
    index = 0
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, 
            #   then draw a rectangle corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (255, 0, 255), 2)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (255, 0, 255), -1)

            index = index + 1
            print (str(index) + " : " + str(r) + ", (x,y) = " + str(x) + ', ' + str(y))
        print('No. of circles detected = {}'.format(index))