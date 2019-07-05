# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 22:01:25 2019

@author: Lusijay
"""
# Function - To find the running average over the background
def run_avg(image, aWeight):
    global bg
    # initialize the background
    if bg is None:
        bg = image.copy().astype("float")
        return

    # compute weighted average, accumulate it and update the background
    cv2.accumulateWeighted(image, bg, aWeight)