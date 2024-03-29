# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:18:35 2022
Author: Gaudet, Vernon
403FIN_P_CBgo_nogo.py

This program is a Color blindness Go/No-go task. Participants will be presented with colored tiles: blue, red, yellow and green over 3 blocks of 20 trials. 
Tiles are preceded by a fixation cross. Participants will be instructed to respond to  yellow and blue tiles but to
withold responding to green or red. The majority of trials will present yellow and blue tiles (20% blue, 60% yellow). This is to habituate responding. 
Red and  green tile presentations are meant to evoke incorrect responses inferring failure to inhibit responses or failure in color perception (10% chance each). 
This is experiment is meant to assess color blindness as those with blue-green color blindness have trouble differentiating red 
from yellow and/or blue from green. Those with color blindness should take longer to respond correctly or fail more often than controls.
Participants will be prompted for information then shown instructions, then the trials will begin. Participants will make a key press to begin the experiment 
and to start each block.


"""
#=====================
#IMPORT MODULES
#=====================
import numpy as np
from psychopy import core, gui, visual, event, monitors
import json, os, time, csv
import random as rand
import pandas as pd
from datetime import datetime 

#=====================
#PATH SETTINGS
#=====================
# get current working directory and make a data folder within
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'data')
if not os.path.exists(data_dir):
   os.makedirs(data_dir)
   
#=====================
#COLLECT PARTICIPANT INFO
#=====================
# Collect subject number, age and handedness and create dialog box
exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi')}
my_dlg = gui.DlgFromDict(dictionary=exp_info, 
                         title= 'subject info', 
                         order = ['subject_nr', 'age', 'handedness' ]) # fixed order
# get and stringify current date
date = datetime.now()
exp_info['date'] = str(date.day) + str(date.month) + str(date.year)
# make filename from subject number, age, current date and handedness
filename = (str(exp_info['subject_nr'])+ '-' +str(exp_info['age'])+ (str(exp_info['handedness'][0]).upper()) + exp_info['date'])
#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
nblocks= 3 # total blocks
ntrials= 20 # trials per block
ntotal= nblocks * ntrials # total trials
stim_dur= 1 # stimulus duration
fix_dur= 0.5 # fixation cross duration

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
# initialize all lists to 0 for each trial
tr_block = [0]*ntotal # block
tr_trial = [0]*ntotal # trial
tr_color = [0]*ntotal # actual stim color
tr_order = [0]*ntotal # color order (coded 0, 1 ,2)
tr_resp = [0]*ntotal # correct response
sub_resp = [0]*ntotal # subject response
sub_acc = [0]*ntotal # subject accuracy
sub_RT = [0]*ntotal # subject response time

#=====================
#PREPARE CONDITION LISTS
#=====================
# create go/ no-go trial order
# COLOR CODES: green = 0, red = 1, blue = 2, yellow = 3
# gets random integer of 0 to 7 (8 values)
# 0 or 1  is directly stored, 2 to 9 are converted to (2,3) = 2 or (4 to 9) = 3
# currently set to 80% go. 90% no go. 10% green, 10% red, 20% blue, 80% yellow
for trial in range(ntotal):
    go = rand.randint(0,9) # random integer from 0 to 9
    if go < 2: # if 0 or 1 then no go
        tr_order[trial] = go # green or red
        tr_resp[trial] = 0
    
    #if 2 or above then go either 2 or 3
    if go in range(2,3): 
        tr_resp[trial] = 1
        tr_order[trial] = 2 # blue
    if go in range(4,9):
        tr_resp[trial] = 1
        tr_order[trial] = 3 # yellow


#index 0 is stim type, index 1 is correct response
trials = list(zip(tr_order, tr_resp)) # zip to assemble all trials

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
# monitor and window
mon = monitors.Monitor('myMonitor', width=35.56, distance=60) # monitor
mon.setSizePix([1920,1080]) # 1920x1080p
win = visual.Window(monitor=mon, size = (800, 800)) # window

# stimuli
tr_text = visual.TextStim(win) # initialize text
tr_stim = visual.Rect(win, size=(1,1)) # intitialize trial stimuli
fix = visual.TextStim(win, text= '+', color='red') # define fixation cross

#=====================
#START EXPERIMENT
#=====================
# Intro text
tr_text.text = 'Welcome to the Color Blindness Go/No-Go Task!\n\n Press SPACE to respond as fast as possible to YELLOW or BLUE squares.\n\nDo NOT respond to GREEN or RED squares.\n\n Press ESCAPE at any time to stop the experiment.\n...\nPress any key to continue!'
tr_text.height = 0.05 # text size
tr_text.draw() # draw text
win.flip() # show text

# wait for key to continue or escape to quit
keys = event.waitKeys()
if keys:
    if 'escape' in keys:
        win.close() 

#=====================
#BLOCK SEQUENCE
#=====================        
tr_current= 0 # total trial counter
tr_timer = core.CountdownTimer() # initialize trial countdown timer
sub_timer = core.Clock() # intitialize subject RT timer

# block loop
for block in range(nblocks):
    tr_text.text = 'Block %i.\n\n Press SPACE to respond as fast as possible to YELLOW or BLUE squares.\n\nDo NOT respond to GREEN or RED squares.\n\n...\nPress any key to begin!' % (block+1) # block text
    tr_text.draw() # draw 
    win.flip() # show
    
    # wait for key to continue or escape to quit
    keys = event.waitKeys()
    if keys:
            if 'escape' in keys:
                win.close() 
    #=====================
    #TRIAL SEQUENCE
    #=====================
    # trial loop            
    for trial in range(ntrials):
        # record trial and block number
        tr_block[tr_current] = block+1 
        tr_trial[tr_current] = trial+1
        
        # fixation cross
        tr_timer.add(fix_dur) # add fixation time to timer
        while tr_timer.getTime() > 0:
            fix.draw() # draw
            win.flip() # show
            
        # set stim color to pre-coded colors and add actual color to trial record
        if trials[tr_current][0] == 0: # no go (green)
            tr_stim.color = 'green'
            tr_color[tr_current] = 'green'
        elif trials[tr_current][0] == 1: # no go (red)
            tr_stim.color = 'red'
            tr_color[tr_current] = 'red'
        elif trials[tr_current][0] == 2: # go (blue)
            tr_stim.color = 'blue'
            tr_color[tr_current] = 'blue'
        elif trials[tr_current][0] == 3: # go (yellow)
            tr_stim.color = 'yellow'
            tr_color[tr_current] = 'yellow'
        
        # stimulus
        tr_timer.add(stim_dur) # add stimulus duration to timer
        sub_timer.reset() # reset subject RT clock
        event.clearEvents() # clear keypresses
        count = 0 # initialize key counter to 0
        while tr_timer.getTime() > 0:
            tr_stim.draw() # draw
            win.flip() # show
            
            # get response
            keys = event.getKeys(keyList=['space', 'escape']) # only accept space or escape as keypresses
            if keys:
                count= count + 1 # track total key presses
                # if escape is pressed, quit
                if 'escape' in keys:
                    win.close() 
                # on first key press, record response and record response time for current trial
                if count == 1:
                    sub_resp[tr_current] = 1
                    sub_RT[tr_current] = sub_timer.getTime()

        # compare subject response to answer key, if matches then accuracy is 1 (correct)
        if sub_resp[tr_current] == trials[tr_current][1]:
            sub_acc[tr_current] = 1
        
        tr_current = tr_current + 1 # track overall current trial number
        
#======================
# END OF EXPERIMENT
#======================  
win.close() # close window

# put collection lists in dict for saving
tr_data = {
 "Block Number": tr_block, 
 "Trial Number": tr_trial, 
 "Response": sub_resp,
 "Correct Response": tr_resp,
 "Color Code": tr_order,
 "Color": tr_color,   
 "Accuracy": sub_acc, 
 "Response Time": sub_RT
}
# save data dict to csv
df = pd.DataFrame(data=tr_data)
df.to_csv(os.path.join(data_dir, filename+ '.csv'), sep=',', index=False) # save to data directory as filename

#save data dict to json in data directory as filename
with open(data_dir +'/'+ filename + '.json', 'w') as outfile: 
        json.dump(tr_data, outfile)
