# -*- coding: utf-8 -*-
"""
Gaudet, Vernon

Assignment 6: Level 3 - PsychoPy 101

Stimulus excercises. AS6 code with alterations to shorten program and removed comments
that are not relevant to the stimulus exercises 1 and 2 only.
"""

#=====================
#IMPORT MODULES
#=====================
import numpy as np
from psychopy import core, gui, visual, event, monitors
import json, os, time
import random as rand
from datetime import datetime

#=====================
#PATH SETTINGS
#=====================
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'data')
image_dir = os.path.join(main_dir,'images')

if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")
if not os.path.isdir(data_dir):
    raise Exception("Could not find the path!")
ims_dir = sorted(os.listdir(image_dir))
#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================

trials = 10 
blocks = 2
stim = "face"
ext = ".jpg"
pics = []

#stim height and width changed to 400*400
stimheight = 400 
stimwidth = 400

# stimulus and fixation cross duration 1 second
stimdur= 1
crossdur= 1

# Text presets
startmessage = "Beginning experiment..."
betweenmsg = "Wait for next image."

#=====================
#PREPARE CONDITION LISTS
#=====================

for trial in range(trials):
    image = stim + "{:02d}".format(trial+1) + ext
    pics.append(image)

for pic in pics:
    if pic not in ims_dir:
        raise Exception("Image not found. The image lists do not match up!")
    else:
        print(pic, "was found!")
    
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================

mon = monitors.Monitor('myMonitor', width=46, distance=60) 
mon.setSizePix([1920,1080])
win = visual.Window(monitor=mon, size=(800, 800), units= 'pix', color=[-1,-1,-1], fullscr = True, ) # changed to fullscreen

# take window size x and y , divide each by four to get midway point of quadrant in pixels
imgcoorx = (win.size[0] / 4)
imgcoory = (win.size[1] / 4)

start_msg = 'Welcome to my experiment!\n...\nPress any key to continue.'
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial"

# Create fixation cross
cross = visual.TextStim(win, '+')
cross.color = 'red'
cross.bold = True

my_image = visual.ImageStim(win) # Initialize image
my_text = visual.TextStim(win) # Initialize text

#=====================
#START EXPERIMENT
#=====================
my_text.text = start_msg 
my_text.draw()
win.flip()
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================

for block in range (blocks):
    
    # Display block text
    my_text.text = block_msg 
    my_text.draw()
    win.flip()
    event.waitKeys() 
    rand.shuffle(pics) 
    
    for trial in range(trials): 
        my_image.image = os.path.join(image_dir, pics[trial])
        my_image.size = stimheight, stimwidth
               
        # get randomly assigned -1 or 1 to multiply with x or y (imgcoorx/y) to get random quadrant
        x = rand.sample([-1, 1], k = 1)
        y = rand.sample([-1, 1], k = 1)
        my_image.pos = x[0]*imgcoorx, y[0]*imgcoory # Note: image position is in pixels from the center of the window
       
        # Display fixation cross
        cross.draw()
        win.flip()
        core.wait(stimdur) #wait for stimulus duration

        # Display image
        my_image.draw()
        win.flip()
        core.wait(stimdur) #wait for stimulus duration
        
        # Display end trial text
        my_text.text = end_trial_msg + ' ' + str(trial + 1) #define the text and trial #
        my_text.draw()
        win.flip()
        core.wait(stimdur) #wait for stimulus duration

#======================
# END OF EXPERIMENT
#======================  

win.close()
