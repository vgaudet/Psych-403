"""
Created on Wed Dec  7 13:18:35 2022

@author: vernon

go/no go task
"""

import numpy as np
from psychopy import core, gui, visual, event, monitors
import json, os, time, csv
import random as rand

main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'data')
if not os.path.exists(data_dir):
   os.makedirs(data_dir)

exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi')}
my_dlg = gui.DlgFromDict(dictionary=exp_info, 
                         title= 'subject info', 
                         order = ['subject_nr', 'age', 'handedness' ])
filename = (str(exp_info['subject_nr']) + 'go_no-go' +'_outputFile.csv')

nblocks= 2
ntrials= 5
ntotal= nblocks * ntrials

stim_dur= 1
fix_dur= 0.5

tr_block = [0]*ntotal
tr_trial = [0]*ntotal
tr_order = [0]*ntotal
tr_resp = [0]*ntotal
sub_resp = [0]*ntotal
sub_acc = [0]*ntotal
sub_RT = [0]*ntotal

# 0 is no-go, 1 is infrequent go, 2 is frequent go
for trial in range(ntotal):
    go = rand.randint(0,6)
    if go >= 2:
        go = 2
    if go in (1,2):
        tr_resp[trial] = 1
    else:
        tr_resp[trial] = 0
    tr_order[trial] = go

#index 0 is stim type, index 1 is correct response
trials = list(zip(tr_order, tr_resp))


mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920,1080])
win = visual.Window(monitor=mon, size = (800, 800)) #define a window
tr_text = visual.TextStim(win)
tr_stim = visual.Rect(win, size=(1,1))
fix = visual.TextStim(win, text= '+', color='red')


tr_text.text = 'Go/No-Go Task.\nPress any key to continue!'
tr_text.draw()
win.flip()
keys = event.waitKeys()
if keys:
    if 'escape' in keys:
        win.close() 
        
tr_current= 0
tr_timer = core.CountdownTimer()
sub_timer = core.Clock()
for block in range(nblocks):
    tr_text.text = 'Block %i.\nPress any key to begin!' % (block+1)
    tr_text.draw()
    win.flip()
    
    keys = event.waitKeys()
    if keys:
            if 'escape' in keys:
                win.close() 
                
    for trial in range(ntrials):
        tr_block[tr_current] = block+1
        tr_trial[tr_current] = trial+1
        
        tr_timer.add(fix_dur)
        while tr_timer.getTime() > 0:
            fix.draw()
            win.flip()
            
        if trials[tr_current][0] == 0: # no go
            tr_stim.color = 'green'
        elif trials[tr_current][0] == 1: # infrequent go
            tr_stim.color = 'orange'
        elif trials[tr_current][0] == 2: # go
            tr_stim.color = 'blue'
        
        
        tr_timer.add(stim_dur)
        sub_timer.reset()
        event.clearEvents()
        count = 0
        while tr_timer.getTime() > 0:
            tr_stim.draw()
            win.flip()
            
            keys = event.getKeys(keyList=['space', 'escape'])
            count= 0
            if keys:
                count= count + 1
                if count == 1:
                    sub_resp[tr_current] = 1
                    sub_RT[tr_current] = sub_timer.getTime()

                if 'escape' in keys:
                    win.close() 
                
        
        if sub_resp[tr_current] == trials[tr_current][1]:
            sub_acc[tr_current] = 1
        
        tr_current = tr_current + 1

win.close()

print(tr_block, ' Blocks')
print(tr_trial, ' Trials Numbers')
print(tr_order, ' Stims')
print(tr_resp, ' Correct Responses')
print(sub_resp, ' Subject Responses')
print(sub_acc, ' Subject Accuracy')
print(sub_RT, ' Subject RT')

