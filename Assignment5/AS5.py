# -*- coding: utf-8 -*-
"""
Gaudet, Vernon

Assignment 5: Level 3 - PsychoPy 101
"""

#=====================
#IMPORT MODULES
#=====================
import numpy as np
from psychopy import core, gui, visual, event
import json, os, time
import random as rand

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
#-define the directory where you will save your data
#-if you will be presenting images, define the image directory
#-check that these directories exist

#main directory, image directory and data directory
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'data')
image_dir = os.path.join(main_dir,'images')

# Check directory exist
if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")
if not os.path.isdir(data_dir):
    raise Exception("Could not find the path!")

# Sorted list of images in the image directory
ims_dir = sorted(os.listdir(image_dir))


#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, 
    #handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================

#-number of trials and blocks *
# 2 blocks of 10 trials
trials = 10 
blocks = 2
#-stimulus names (and stimulus extensions, if images) *
stim = "face"
ext = ".jpg"
pics = []
#-stimulus properties like size, orientation, location, duration *
# 200 x 200 image size, 1 second stimulus presentation, 1 second cross presentation
stimheight = 200
stimwidth = 200
stimdur= 1
crossdur= 1
#-start message text *
startmessage = "Beginning experiment..."
betweenmsg = "Wait for next image."

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
#-create counterbalanced list of all conditions *
# Only one condition, variance is the order of presented images and each block is randomized already

# Automated image list name creation
for trial in range(trials):
    # format to have leading zeroes (face + number + .jpg), then append to image list
    image = stim + "{:02d}".format(trial+1) + ext
    pics.append(image)

# check if each image is in the directory and print status
for pic in pics:
    if pic not in ims_dir:
        raise Exception("Image not found. The image lists do not match up!")
    else:
        print(pic, "was found!")
    
#=====================
#PREPARE DATA COLLECTION LISTS
#=====================

key = [] #-create an empty list for correct responses (e.g., "on this trial, a response of X is #correct") *
response = []  #-create an empty list for participant responses (e.g., "on this trial, response was a #X") *
accuracy = [] #-create an empty list for response accuracy collection (e.g., "was participant #correct?")
rtlist = [] #-create an empty list for response time collection *
orderSID= [] #-create an empty list for recording the order of stimulus identities *
orderSP = [] #-create an empty list for recording the order of stimulus properties *


#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
for block in range (blocks): #-for loop for nBlocks *
    
    #-present block start message
    rand.shuffle(pics) #-randomize order of trials here *
    #-reset response time clock here
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(trials): #-for loop for nTrials *
        break
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment