﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Sun Feb 16 15:12:56 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('3.2.4')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jnthorp/Documents/TGIF/Protocol/test_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "init_routine"
init_routineClock = core.Clock()
####################

# import libraries
import random, xlrd, time, pickle, csv, pandas as pd, os #xlsxwriter and timer, pickle to save variables
import numpy as np
import glob

# import libraries and specify SCR port address
#from psychopy import parallel
import time

#randomize the seed
random.seed()

#stimulus file
#expDir = os.path.join('/Users','jnthorp','Documents','TGIF')
#expDir = os.path.join('/Users','john','Library','Mobile Documents','com~apple~CloudDocs','Documents','TGIF')
expDir = os.getcwd()
beach_scene_1 = os.path.join(expDir,'Stimuli','conditioning','beach_scene-1.jpg') #pre-conditioning beach scene
beach_scene_2 = os.path.join(expDir,'Stimuli','conditioning','beach_scene-2.jpg') #pre-conditioning beach scene
beach_sound = os.path.join(expDir, 'Stimuli', 'conditioning','beach_sounds','*') #directory with the alternative beach scenes
camp_scene_1 = os.path.join(expDir,'Stimuli','conditioning','camp_scene-1.jpg') #pre-conditioning camp scene
camp_scene_2 = os.path.join(expDir,'Stimuli','conditioning','camp_scene-2.jpg') #pre-conditioning camp scene
camp_sound = os.path.join(expDir, 'Stimuli', 'conditioning','camp_sounds','*') #directory with the alternative camp scenes

items_all_path = os.path.join(expDir,'Lists','stim_list.csv')
scenes_all_path = os.path.join(expDir,'Lists','conditioning_scenes.csv') #csv with all the conditioning stims compiled by initialize_conditioning_stims.py
counterbalance_path = os.path.join(expDir,'Lists','counterbalance.csv') #csv with subject-level counterbalance data


# Initialize components for Routine "wait_routine"
wait_routineClock = core.Clock()
wait_text = visual.TextStim(win=win, name='wait_text',
    text='The experiment will start in a moment.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
wait_key = keyboard.Keyboard()

# Initialize components for Routine "trial_init_routine"
trial_init_routineClock = core.Clock()
trials = 288
trial = 0
trial_jitter_time = 2

# Initialize components for Routine "trial_jitter_routine"
trial_jitter_routineClock = core.Clock()
trial_jitter_cross = visual.TextStim(win=win, name='trial_jitter_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_object_routine"
trial_object_routineClock = core.Clock()
object_object = visual.ImageStim(
    win=win,
    name='object_object', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
object_rating = visual.RatingScale(win=win, name='object_rating', marker='triangle', size=1.0, pos=[0.0, -0.85], low=1, high=3, labels=['Old', 'Similar', 'New'], scale='', singleClick=True, disappear=True)

# Initialize components for Routine "trial_scene_routine"
trial_scene_routineClock = core.Clock()
trial_scene_beach_1 = visual.ImageStim(
    win=win,
    name='trial_scene_beach_1', 
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0.25), size=(0.7, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trial_scene_beach_2 = visual.ImageStim(
    win=win,
    name='trial_scene_beach_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.4, -0.25), size=(0.7, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
trial_scene_camp_1 = visual.ImageStim(
    win=win,
    name='trial_scene_camp_1', 
    image='sin', mask=None,
    ori=0, pos=(0.4, 0.25), size=(0.7, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
trial_scene_camp_2 = visual.ImageStim(
    win=win,
    name='trial_scene_camp_2', 
    image='sin', mask=None,
    ori=0, pos=(0.4, -0.25), size=(0.7, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
trial_scene_pos = event.Mouse(win=win)
x, y = [None, None]
trial_scene_pos.mouseClock = core.Clock()
trial_scene_object = visual.ImageStim(
    win=win,
    name='trial_scene_object', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "trial_source_routine"
trial_source_routineClock = core.Clock()
trial_source_scene = visual.ImageStim(
    win=win,
    name='trial_source_scene', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.05), size=(1.36, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trial_source_pos = event.Mouse(win=win)
x, y = [None, None]
trial_source_pos.mouseClock = core.Clock()
trial_source_object = visual.ImageStim(
    win=win,
    name='trial_source_object', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "blank_screen"
blank_screenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "scene_init_routine"
scene_init_routineClock = core.Clock()
num_scenes = 96
scene = 0

# Initialize components for Routine "scene_jitter_routine"
scene_jitter_routineClock = core.Clock()
scene_jitter_cross = visual.TextStim(win=win, name='scene_jitter_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "scene_scene_routine"
scene_scene_routineClock = core.Clock()
scene_image = visual.ImageStim(
    win=win,
    name='scene_image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.05), size=(1.36, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
scene_rating = visual.RatingScale(win=win, name='scene_rating', marker='triangle', size=1.0, pos=[0.0, -0.85], low=1, high=2, labels=['Old', 'New'], scale='', disappear=True)

# Initialize components for Routine "end_screen"
end_screenClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text='Thank you for your participation in the experiment.',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "init_routine"-------
# update component parameters for each repeat

#access the xls stimulus file
items_all = pd.read_csv(items_all_path) #read in all the item stims
scenes_all = pd.read_csv(scenes_all_path) #read in all the scene stims
counterbalance = pd.read_csv(counterbalance_path) #read in the counterbalance csv

#############
##Generate subject-specific stim list
#############
random.seed()

subj_num = int(expInfo['participant'])
subj_idx = counterbalance.subject == subj_num #index subj_num within the counterbalance df
dataDir = os.path.join(expDir, 'Data', str(subj_num)) #location of the data directory for this subject

#read in list of items shown to subject
subj_stims_path = os.path.join(dataDir,'pre-conditioning_stims.csv')
subj_stims = pd.read_csv(subj_stims_path)

random.seed()

old_stims = subj_stims[subj_stims.group == int(counterbalance.old[subj_idx])].reset_index(drop=True)
old_similar_stims = subj_stims[subj_stims.group == int(counterbalance.similar[subj_idx])].sort_values(by = 'item').reset_index(drop=True)
new_items = np.unique(items_all.item[(items_all.group == int(counterbalance.new[subj_idx]))])

similar_stim_items = old_similar_stims[['item','object']]
all_similar_stims = items_all[items_all.group == int(counterbalance.similar[subj_idx])]

new_similar_stims = all_similar_stims[~all_similar_stims.index.isin(pd.merge(items_all, similar_stim_items)['Unnamed: 0'])].reset_index(drop = True)
new_similar_stims = new_similar_stims.sort_values('item').reset_index(drop = True)
similar_stims = old_similar_stims.assign(filename = new_similar_stims['filename'].tolist(), object = new_similar_stims['object'].tolist()).reset_index(drop = True)

#Randomize which exemplar of each item is shown to the participant
new_stim_indices = pd.DataFrame(list(zip(new_items,
                               np.random.randint(2, size = len(new_items)) + 1)),
                      columns = ['item','object'])

new_stims = items_all[items_all.index.isin(pd.merge(items_all, new_stim_indices)['Unnamed: 0'])].reset_index(drop = True)
#new_stims['context'] = np.repeat([1,2,1,2], int(len(new_stims)/4))

stims = old_stims.append([similar_stims, new_stims]).reset_index(drop = True).drop('iti',axis = 1)
stims = stims.sample(frac=1).reset_index(drop = True)

scenes = pd.read_csv(scenes_all_path)
scenes['old'] = scenes.group == int(counterbalance.conditioning[subj_idx])
scenes = scenes.sample(frac=1).reset_index(drop = True)

mouse = psychopy.event.Mouse()
mouse.setVisible(0)
# keep track of which components have finished
init_routineComponents = []
for thisComponent in init_routineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
init_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "init_routine"-------
while continueRoutine:
    # get current time
    t = init_routineClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=init_routineClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    keys = event.getKeys()
    for key in keys:
        if '5' and 'z' in key:
            core.quit()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in init_routineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "init_routine"-------
for thisComponent in init_routineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "init_routine" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wait_routine"-------
# update component parameters for each repeat
wait_key.keys = []
wait_key.rt = []
# keep track of which components have finished
wait_routineComponents = [wait_text, wait_key]
for thisComponent in wait_routineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wait_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "wait_routine"-------
while continueRoutine:
    # get current time
    t = wait_routineClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wait_routineClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait_text* updates
    if wait_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_text.frameNStart = frameN  # exact frame index
        wait_text.tStart = t  # local t and not account for scr refresh
        wait_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_text, 'tStartRefresh')  # time at next scr refresh
        wait_text.setAutoDraw(True)
    
    # *wait_key* updates
    waitOnFlip = False
    if wait_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        wait_key.frameNStart = frameN  # exact frame index
        wait_key.tStart = t  # local t and not account for scr refresh
        wait_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_key, 'tStartRefresh')  # time at next scr refresh
        wait_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(wait_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(wait_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if wait_key.status == STARTED and not waitOnFlip:
        theseKeys = wait_key.getKeys(keyList=['s'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            wait_key.keys = theseKeys.name  # just the last key pressed
            wait_key.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_routineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait_routine"-------
for thisComponent in wait_routineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('wait_text.started', wait_text.tStartRefresh)
thisExp.addData('wait_text.stopped', wait_text.tStopRefresh)
# check responses
if wait_key.keys in ['', [], None]:  # No response was made
    wait_key.keys = None
thisExp.addData('wait_key.keys',wait_key.keys)
if wait_key.keys != None:  # we had a response
    thisExp.addData('wait_key.rt', wait_key.rt)
thisExp.addData('wait_key.started', wait_key.tStartRefresh)
thisExp.addData('wait_key.stopped', wait_key.tStopRefresh)
thisExp.nextEntry()
#win.callOnFlip(sendTrigger, code=0)
win.flip()
# the Routine "wait_routine" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
objects_loop = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='objects_loop')
thisExp.addLoop(objects_loop)  # add the loop to the experiment
thisObjects_loop = objects_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisObjects_loop.rgb)
if thisObjects_loop != None:
    for paramName in thisObjects_loop:
        exec('{} = thisObjects_loop[paramName]'.format(paramName))

for thisObjects_loop in objects_loop:
    currentLoop = objects_loop
    # abbreviate parameter names if possible (e.g. rgb = thisObjects_loop.rgb)
    if thisObjects_loop != None:
        for paramName in thisObjects_loop:
            exec('{} = thisObjects_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_init_routine"-------
    # update component parameters for each repeat
    #assigning the enc item
    trial_iti = 2
    trial_item = stims.path[trial]
    trial_context = stims.context[trial]
    #trial_scene = scene_order[int(trial_context-1)]
    item_pos = (0,0)
    #log enc information to data file
    #thisExp.addData('image_item', image_item2[enc_order2[enc_trial2]])
    #thisExp.addData('emotion_item', emotion_item2[enc_order2[enc_trial2]])
    #thisExp.addData('old_new', old_new2[enc_order2[enc_trial2]])
    #thisExp.addData('size_item', size_item2[enc_order2[enc_trial2]])
    #thisExp.addData('enc_trial', enc_trial2)
    #thisExp.nextEntry()
    
    #increment the current enc item counter
    trial = trial + 1
    
    
    # keep track of which components have finished
    trial_init_routineComponents = []
    for thisComponent in trial_init_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_init_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_init_routine"-------
    while continueRoutine:
        # get current time
        t = trial_init_routineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_init_routineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        keys = event.getKeys()
        for key in keys:
            if 'f12' in key:
                core.quit()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_init_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_init_routine"-------
    for thisComponent in trial_init_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #current_arrow_trial
    #arrow_trial = 0
    # the Routine "trial_init_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_jitter_routine"-------
    # update component parameters for each repeat
    #win.callOnFlip(sendTrigger, code=1)
    #win.flip()
    # keep track of which components have finished
    trial_jitter_routineComponents = [trial_jitter_cross]
    for thisComponent in trial_jitter_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_jitter_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_jitter_routine"-------
    while continueRoutine:
        # get current time
        t = trial_jitter_routineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_jitter_routineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_jitter_cross* updates
        if trial_jitter_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_jitter_cross.frameNStart = frameN  # exact frame index
            trial_jitter_cross.tStart = t  # local t and not account for scr refresh
            trial_jitter_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_jitter_cross, 'tStartRefresh')  # time at next scr refresh
            trial_jitter_cross.setAutoDraw(True)
        if trial_jitter_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_jitter_cross.tStartRefresh + trial_jitter_time-frameTolerance:
                # keep track of stop time/frame for later
                trial_jitter_cross.tStop = t  # not accounting for scr refresh
                trial_jitter_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_jitter_cross, 'tStopRefresh')  # time at next scr refresh
                trial_jitter_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_jitter_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_jitter_routine"-------
    for thisComponent in trial_jitter_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    objects_loop.addData('trial_jitter_cross.started', trial_jitter_cross.tStartRefresh)
    objects_loop.addData('trial_jitter_cross.stopped', trial_jitter_cross.tStopRefresh)
    # the Routine "trial_jitter_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_object_routine"-------
    # update component parameters for each repeat
    object_object.setImage(trial_item)
    object_rating.reset()
    #background_sound = sound.Sound(trial_sound)
    #background_sound.play()
    
    #win.callOnFlip(sendTrigger, code=1)
    #win.flip()
    # keep track of which components have finished
    trial_object_routineComponents = [object_object, object_rating]
    for thisComponent in trial_object_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_object_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_object_routine"-------
    while continueRoutine:
        # get current time
        t = trial_object_routineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_object_routineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *object_object* updates
        if object_object.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            object_object.frameNStart = frameN  # exact frame index
            object_object.tStart = t  # local t and not account for scr refresh
            object_object.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(object_object, 'tStartRefresh')  # time at next scr refresh
            object_object.setAutoDraw(True)
        # *object_rating* updates
        if object_rating.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            object_rating.frameNStart = frameN  # exact frame index
            object_rating.tStart = t  # local t and not account for scr refresh
            object_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(object_rating, 'tStartRefresh')  # time at next scr refresh
            object_rating.setAutoDraw(True)
        continueRoutine &= object_rating.noResponse  # a response ends the trial
        #if rating_no_force_end.status == FINISHED and object.status==FINISHED:
        #    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_object_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_object_routine"-------
    for thisComponent in trial_object_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    objects_loop.addData('object_object.started', object_object.tStartRefresh)
    objects_loop.addData('object_object.stopped', object_object.tStopRefresh)
    # store data for objects_loop (TrialHandler)
    objects_loop.addData('object_rating.response', object_rating.getRating())
    objects_loop.addData('object_rating.rt', object_rating.getRT())
    objects_loop.addData('object_rating.started', object_rating.tStart)
    objects_loop.addData('object_rating.stopped', object_rating.tStop)
    rating = object_rating.getRating()
    if rating == 3:
        trial_jitter_time = 6
    else:
        trial_jitter_time = 2
    # the Routine "trial_object_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_scene_routine"-------
    # update component parameters for each repeat
    
    mouse.setPos((0,0))
    trial_scene_beach_1.setImage(beach_scene_1)
    trial_scene_beach_2.setImage(beach_scene_2)
    trial_scene_camp_1.setImage(camp_scene_1)
    trial_scene_camp_2.setImage(camp_scene_2)
    # setup some python lists for storing info about the trial_scene_pos
    trial_scene_pos.clicked_image = []
    gotValidClick = False  # until a click is received
    trial_scene_object.setImage(trial_item)
    # keep track of which components have finished
    trial_scene_routineComponents = [trial_scene_beach_1, trial_scene_beach_2, trial_scene_camp_1, trial_scene_camp_2, trial_scene_pos, trial_scene_object]
    for thisComponent in trial_scene_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_scene_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_scene_routine"-------
    while continueRoutine:
        # get current time
        t = trial_scene_routineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_scene_routineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if rating == 3:
            continueRoutine = False
        
        item_pos = mouse.getPos()
        
        # *trial_scene_beach_1* updates
        if trial_scene_beach_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_scene_beach_1.frameNStart = frameN  # exact frame index
            trial_scene_beach_1.tStart = t  # local t and not account for scr refresh
            trial_scene_beach_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_scene_beach_1, 'tStartRefresh')  # time at next scr refresh
            trial_scene_beach_1.setAutoDraw(True)
        
        # *trial_scene_beach_2* updates
        if trial_scene_beach_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_scene_beach_2.frameNStart = frameN  # exact frame index
            trial_scene_beach_2.tStart = t  # local t and not account for scr refresh
            trial_scene_beach_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_scene_beach_2, 'tStartRefresh')  # time at next scr refresh
            trial_scene_beach_2.setAutoDraw(True)
        
        # *trial_scene_camp_1* updates
        if trial_scene_camp_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_scene_camp_1.frameNStart = frameN  # exact frame index
            trial_scene_camp_1.tStart = t  # local t and not account for scr refresh
            trial_scene_camp_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_scene_camp_1, 'tStartRefresh')  # time at next scr refresh
            trial_scene_camp_1.setAutoDraw(True)
        
        # *trial_scene_camp_2* updates
        if trial_scene_camp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_scene_camp_2.frameNStart = frameN  # exact frame index
            trial_scene_camp_2.tStart = t  # local t and not account for scr refresh
            trial_scene_camp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_scene_camp_2, 'tStartRefresh')  # time at next scr refresh
            trial_scene_camp_2.setAutoDraw(True)
        # *trial_scene_pos* updates
        if trial_scene_pos.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_scene_pos.frameNStart = frameN  # exact frame index
            trial_scene_pos.tStart = t  # local t and not account for scr refresh
            trial_scene_pos.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_scene_pos, 'tStartRefresh')  # time at next scr refresh
            trial_scene_pos.status = STARTED
            trial_scene_pos.mouseClock.reset()
            prevButtonState = trial_scene_pos.getPressed()  # if button is down already this ISN'T a new click
        if trial_scene_pos.status == STARTED:  # only update if started and not finished!
            buttons = trial_scene_pos.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [trial_scene_beach_1, trial_scene_beach_2, trial_scene_camp_1, trial_scene_camp_2]:
                        if obj.contains(trial_scene_pos):
                            gotValidClick = True
                            trial_scene_pos.clicked_image.append(obj.image)
                    # abort routine on response
                    continueRoutine = False
        
        # *trial_scene_object* updates
        if trial_scene_object.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_scene_object.frameNStart = frameN  # exact frame index
            trial_scene_object.tStart = t  # local t and not account for scr refresh
            trial_scene_object.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_scene_object, 'tStartRefresh')  # time at next scr refresh
            trial_scene_object.setAutoDraw(True)
        if trial_scene_object.status == STARTED:  # only update if drawing
            trial_scene_object.setPos(item_pos, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_scene_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_scene_routine"-------
    for thisComponent in trial_scene_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if len(trial_scene_pos.clicked_image):
        trial_scene = trial_scene_pos.clicked_image[-1]
    else:
        rating = 3
        trial_scene = beach_scene_1
    
    objects_loop.addData('trial_scene_beach_1.started', trial_scene_beach_1.tStartRefresh)
    objects_loop.addData('trial_scene_beach_1.stopped', trial_scene_beach_1.tStopRefresh)
    objects_loop.addData('trial_scene_beach_2.started', trial_scene_beach_2.tStartRefresh)
    objects_loop.addData('trial_scene_beach_2.stopped', trial_scene_beach_2.tStopRefresh)
    objects_loop.addData('trial_scene_camp_1.started', trial_scene_camp_1.tStartRefresh)
    objects_loop.addData('trial_scene_camp_1.stopped', trial_scene_camp_1.tStopRefresh)
    objects_loop.addData('trial_scene_camp_2.started', trial_scene_camp_2.tStartRefresh)
    objects_loop.addData('trial_scene_camp_2.stopped', trial_scene_camp_2.tStopRefresh)
    # store data for objects_loop (TrialHandler)
    x, y = trial_scene_pos.getPos()
    buttons = trial_scene_pos.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [trial_scene_beach_1, trial_scene_beach_2, trial_scene_camp_1, trial_scene_camp_2]:
            if obj.contains(trial_scene_pos):
                gotValidClick = True
                trial_scene_pos.clicked_image.append(obj.image)
    objects_loop.addData('trial_scene_pos.x', x)
    objects_loop.addData('trial_scene_pos.y', y)
    objects_loop.addData('trial_scene_pos.leftButton', buttons[0])
    objects_loop.addData('trial_scene_pos.midButton', buttons[1])
    objects_loop.addData('trial_scene_pos.rightButton', buttons[2])
    if len(trial_scene_pos.clicked_image):
        objects_loop.addData('trial_scene_pos.clicked_image', trial_scene_pos.clicked_image[0])
    objects_loop.addData('trial_scene_pos.started', trial_scene_pos.tStart)
    objects_loop.addData('trial_scene_pos.stopped', trial_scene_pos.tStop)
    objects_loop.addData('trial_scene_object.started', trial_scene_object.tStartRefresh)
    objects_loop.addData('trial_scene_object.stopped', trial_scene_object.tStopRefresh)
    # the Routine "trial_scene_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_source_routine"-------
    # update component parameters for each repeat
    if rating == 3:
        continueRoutine = False
    
    mouse.setPos((0,0))
    trial_source_scene.setImage(trial_scene)
    # setup some python lists for storing info about the trial_source_pos
    gotValidClick = False  # until a click is received
    trial_source_object.setImage(trial_item)
    # keep track of which components have finished
    trial_source_routineComponents = [trial_source_scene, trial_source_pos, trial_source_object]
    for thisComponent in trial_source_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_source_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_source_routine"-------
    while continueRoutine:
        # get current time
        t = trial_source_routineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_source_routineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if rating == 3:
            continueRoutine = False
        
        item_pos = mouse.getPos()
        
        
        
        
        # *trial_source_scene* updates
        if trial_source_scene.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_source_scene.frameNStart = frameN  # exact frame index
            trial_source_scene.tStart = t  # local t and not account for scr refresh
            trial_source_scene.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_source_scene, 'tStartRefresh')  # time at next scr refresh
            trial_source_scene.setAutoDraw(True)
        # *trial_source_pos* updates
        if trial_source_pos.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_source_pos.frameNStart = frameN  # exact frame index
            trial_source_pos.tStart = t  # local t and not account for scr refresh
            trial_source_pos.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_source_pos, 'tStartRefresh')  # time at next scr refresh
            trial_source_pos.status = STARTED
            prevButtonState = trial_source_pos.getPressed()  # if button is down already this ISN'T a new click
        if trial_source_pos.status == STARTED:  # only update if started and not finished!
            buttons = trial_source_pos.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # abort routine on response
                    continueRoutine = False
        
        # *trial_source_object* updates
        if trial_source_object.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_source_object.frameNStart = frameN  # exact frame index
            trial_source_object.tStart = t  # local t and not account for scr refresh
            trial_source_object.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_source_object, 'tStartRefresh')  # time at next scr refresh
            trial_source_object.setAutoDraw(True)
        if trial_source_object.status == STARTED:  # only update if drawing
            trial_source_object.setPos(item_pos, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_source_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_source_routine"-------
    for thisComponent in trial_source_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    objects_loop.addData('trial_source_scene.started', trial_source_scene.tStartRefresh)
    objects_loop.addData('trial_source_scene.stopped', trial_source_scene.tStopRefresh)
    # store data for objects_loop (TrialHandler)
    x, y = trial_source_pos.getPos()
    buttons = trial_source_pos.getPressed()
    objects_loop.addData('trial_source_pos.x', x)
    objects_loop.addData('trial_source_pos.y', y)
    objects_loop.addData('trial_source_pos.leftButton', buttons[0])
    objects_loop.addData('trial_source_pos.midButton', buttons[1])
    objects_loop.addData('trial_source_pos.rightButton', buttons[2])
    objects_loop.addData('trial_source_pos.started', trial_source_pos.tStart)
    objects_loop.addData('trial_source_pos.stopped', trial_source_pos.tStop)
    objects_loop.addData('trial_source_object.started', trial_source_object.tStartRefresh)
    objects_loop.addData('trial_source_object.stopped', trial_source_object.tStopRefresh)
    # the Routine "trial_source_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'objects_loop'


# ------Prepare to start Routine "blank_screen"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
#win.callOnFlip(sendTrigger, code=4)
#win.flip()
# keep track of which components have finished
blank_screenComponents = [text_blank, key_resp]
for thisComponent in blank_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blank_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "blank_screen"-------
while continueRoutine:
    # get current time
    t = blank_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blank_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_blank* updates
    if text_blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_blank.frameNStart = frameN  # exact frame index
        text_blank.tStart = t  # local t and not account for scr refresh
        text_blank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_blank, 'tStartRefresh')  # time at next scr refresh
        text_blank.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['s'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank_screen"-------
for thisComponent in blank_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_blank.started', text_blank.tStartRefresh)
thisExp.addData('text_blank.stopped', text_blank.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "blank_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
scenes_loop = data.TrialHandler(nReps=num_scenes, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='scenes_loop')
thisExp.addLoop(scenes_loop)  # add the loop to the experiment
thisScenes_loop = scenes_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisScenes_loop.rgb)
if thisScenes_loop != None:
    for paramName in thisScenes_loop:
        exec('{} = thisScenes_loop[paramName]'.format(paramName))

for thisScenes_loop in scenes_loop:
    currentLoop = scenes_loop
    # abbreviate parameter names if possible (e.g. rgb = thisScenes_loop.rgb)
    if thisScenes_loop != None:
        for paramName in thisScenes_loop:
            exec('{} = thisScenes_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "scene_init_routine"-------
    # update component parameters for each repeat
    #assigning the enc item
    scene_iti = 2
    scene_scene = scenes.path[scene]
    item_pos = (0,0.1)
    #log enc information to data file
    #thisExp.addData('image_item', image_item2[enc_order2[enc_trial2]])
    #thisExp.addData('emotion_item', emotion_item2[enc_order2[enc_trial2]])
    #thisExp.addData('old_new', old_new2[enc_order2[enc_trial2]])
    #thisExp.addData('size_item', size_item2[enc_order2[enc_trial2]])
    #thisExp.addData('enc_trial', enc_trial2)
    #thisExp.nextEntry()
    
    #increment the current enc item counter
    scene = scene + 1
    
    
    # keep track of which components have finished
    scene_init_routineComponents = []
    for thisComponent in scene_init_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    scene_init_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "scene_init_routine"-------
    while continueRoutine:
        # get current time
        t = scene_init_routineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=scene_init_routineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        keys = event.getKeys()
        for key in keys:
            if 'f12' in key:
                core.quit()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scene_init_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "scene_init_routine"-------
    for thisComponent in scene_init_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #current_arrow_trial
    #arrow_trial = 0
    # the Routine "scene_init_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "scene_jitter_routine"-------
    # update component parameters for each repeat
    #win.callOnFlip(sendTrigger, code=1)
    #win.flip()
    # keep track of which components have finished
    scene_jitter_routineComponents = [scene_jitter_cross]
    for thisComponent in scene_jitter_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    scene_jitter_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "scene_jitter_routine"-------
    while continueRoutine:
        # get current time
        t = scene_jitter_routineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=scene_jitter_routineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *scene_jitter_cross* updates
        if scene_jitter_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scene_jitter_cross.frameNStart = frameN  # exact frame index
            scene_jitter_cross.tStart = t  # local t and not account for scr refresh
            scene_jitter_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scene_jitter_cross, 'tStartRefresh')  # time at next scr refresh
            scene_jitter_cross.setAutoDraw(True)
        if scene_jitter_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > scene_jitter_cross.tStartRefresh + scene_iti-frameTolerance:
                # keep track of stop time/frame for later
                scene_jitter_cross.tStop = t  # not accounting for scr refresh
                scene_jitter_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(scene_jitter_cross, 'tStopRefresh')  # time at next scr refresh
                scene_jitter_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scene_jitter_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "scene_jitter_routine"-------
    for thisComponent in scene_jitter_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    scenes_loop.addData('scene_jitter_cross.started', scene_jitter_cross.tStartRefresh)
    scenes_loop.addData('scene_jitter_cross.stopped', scene_jitter_cross.tStopRefresh)
    # the Routine "scene_jitter_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "scene_scene_routine"-------
    # update component parameters for each repeat
    scene_image.setImage(scene_scene)
    scene_rating.reset()
    #background_sound = sound.Sound(trial_sound)
    #background_sound.play()
    
    #win.callOnFlip(sendTrigger, code=1)
    #win.flip()
    # keep track of which components have finished
    scene_scene_routineComponents = [scene_image, scene_rating]
    for thisComponent in scene_scene_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    scene_scene_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "scene_scene_routine"-------
    while continueRoutine:
        # get current time
        t = scene_scene_routineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=scene_scene_routineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *scene_image* updates
        if scene_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scene_image.frameNStart = frameN  # exact frame index
            scene_image.tStart = t  # local t and not account for scr refresh
            scene_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scene_image, 'tStartRefresh')  # time at next scr refresh
            scene_image.setAutoDraw(True)
        # *scene_rating* updates
        if scene_rating.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            scene_rating.frameNStart = frameN  # exact frame index
            scene_rating.tStart = t  # local t and not account for scr refresh
            scene_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scene_rating, 'tStartRefresh')  # time at next scr refresh
            scene_rating.setAutoDraw(True)
        continueRoutine &= scene_rating.noResponse  # a response ends the trial
        #if rating_no_force_end.status == FINISHED and object.status==FINISHED:
        #    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scene_scene_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "scene_scene_routine"-------
    for thisComponent in scene_scene_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    scenes_loop.addData('scene_image.started', scene_image.tStartRefresh)
    scenes_loop.addData('scene_image.stopped', scene_image.tStopRefresh)
    # store data for scenes_loop (TrialHandler)
    scenes_loop.addData('scene_rating.response', scene_rating.getRating())
    scenes_loop.addData('scene_rating.rt', scene_rating.getRT())
    scenes_loop.addData('scene_rating.started', scene_rating.tStart)
    scenes_loop.addData('scene_rating.stopped', scene_rating.tStop)
    rating = object_rating.getRating()
    # the Routine "scene_scene_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed num_scenes repeats of 'scenes_loop'


# ------Prepare to start Routine "end_screen"-------
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
end_screenComponents = [text_end]
for thisComponent in end_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end_screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if text_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_end.frameNStart = frameN  # exact frame index
        text_end.tStart = t  # local t and not account for scr refresh
        text_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
        text_end.setAutoDraw(True)
    if text_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_end.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            text_end.tStop = t  # not accounting for scr refresh
            text_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_end, 'tStopRefresh')  # time at next scr refresh
            text_end.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_screen"-------
for thisComponent in end_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_end.started', text_end.tStartRefresh)
thisExp.addData('text_end.stopped', text_end.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()