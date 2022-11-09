# -*- coding: utf-8 -*-
"""
Gaudet, Vernon

Assignment 6: Level 4: PsychoPy - Showing windows and stimuli
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

# Dictionary with session == 1
exp_info = {'session': 1, 'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':''}

# Show message then wait 3 seconds before presentation
print("All variables have been created! Now ready to show the dialog box!")
time.sleep(3)

# Create dialog box from dictionary with specified order
my_dlg = gui.DlgFromDict(dictionary=exp_info, title= 'subject info', fixed= ['session'], 
                         order = ['session', 'subject_nr', 'age', 'gender', 'handedness' ]  )

date = datetime.now() # Current date
exp_info['date'] = (str(date.day) + str(date.month) + str(date.year)) 
    
# Create a unique filename  from subject number, session and date
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '_'  + str(exp_info['session']) + '.csv'

print(filename)
sub_dir = os.path.join(main_dir,'sub_info',filename)

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

#you will need to change this for every new monitor on which you run your experiment
#your own monitor width and pixel resolution will probably be different from mine
#give your monitor a name, define width and distance
mon = monitors.Monitor('myMonitor', width = 116.84, distance = 100) 
#use x,y coordinates to specify the pixel resolution of your monitor

mon.setSizePix([1920,1080])
win = visual.Window(monitor=mon, size=(800, 800), units= 'pix', color=[-1,-1,-1] )

# Messages
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
#-present start message text
#-allow participant to begin experiment with button press

my_text.text = start_msg #define the text
my_text.draw()
win.flip() #show
event.waitKeys() #wait for keypress

#=====================
#BLOCK SEQUENCE
#=====================
for block in range (blocks): #-for loop for nBlocks *
    
    #-present block start message
    my_text.text = block_msg # Block message
    my_text.draw()
    win.flip()
    event.waitKeys() # Wait for keypress
    rand.shuffle(pics) #-randomize order of trials here *
    #-reset response time clock here
    #=====================
    #TRIAL SEQUENCE
    #=====================    
 #   '''
    for trial in range(trials): #-for loop for nTrials *
        #-set stimuli and stimulus properties for the current trial

        my_image.image = os.path.join(image_dir, pics[trial])
        my_image.size = stimheight, stimwidth
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...

        # Display fixation cross
        cross.draw()
        win.flip()
        core.wait(stimdur)  #wait for stimulus duration
        
        # Display image
        my_image.draw()
        win.flip()
        core.wait(stimdur) #wait for stimulus duration
        
        # Display end trial text
        my_text.text = end_trial_msg + ' ' + str(trial + 1) #define the text and trial #
        my_text.draw()
        win.flip()
        core.wait(stimdur) #wait for stimulus duration
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#        '''

        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment

win.close()
