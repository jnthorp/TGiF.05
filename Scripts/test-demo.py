#!/usr/bin/env python
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
#psychopy.useVersion('3.2.4')


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
from psychopy import parallel

BIO = True
def stamp_next_flip(on_or_offset):
    #stamp_df.loc[stamp_idx,'true_{:s}'.format(on_or_offset)] = clock.getTime()
    if 'event' in on_or_offset:
        if 'on' in on_or_offset:
            event_onstamps.append(clock.getTime())

    else:
        if 'on' in on_or_offset:
            onstamps.append(clock.getTime())
        
        elif 'off' in on_or_offset:
            offstamps.append(clock.getTime())

def stamp_onoffset(on_or_offset,BIO=False,SHOCK=False):
    win.callOnFlip(stamp_next_flip,on_or_offset)
    
    if BIO:
        if 'on' in on_or_offset:
            port.setPin(2,1)
            
        elif 'off' in on_or_offset:
            port.setPin(2,0)

if BIO:
    port = parallel.ParallelPort(address=0xEFF8)
    port.setData(0)

onstamps = []
offstamps = []

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'test-demo'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
#filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
filename = os.path.dirname(_thisDir) + os.sep + u'Data/%s/%s_%s_%s' % (expInfo['participant'], expInfo['participant'], expName, expInfo['date'])

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
    monitor='testMonitor', color='black', colorSpace='rgb',
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
expDir = os.path.dirname(os.getcwd())
beach_scene_1 = os.path.join(expDir,'Stimuli','conditioning','beach_scene-1.png') #pre-conditioning beach scene
beach_scene_2 = os.path.join(expDir,'Stimuli','conditioning','beach_scene-2.png') #pre-conditioning beach scene
beach_sound = os.path.join(expDir, 'Stimuli', 'conditioning','beach_sounds','*') #directory with the alternative beach scenes
camp_scene_1 = os.path.join(expDir,'Stimuli','conditioning','camp_scene-1.png') #pre-conditioning camp scene
camp_scene_2 = os.path.join(expDir,'Stimuli','conditioning','camp_scene-2.png') #pre-conditioning camp scene
camp_sound = os.path.join(expDir, 'Stimuli', 'conditioning','camp_sounds','*') #directory with the alternative camp scenes

items_all_path = os.path.join(expDir,'Lists','test_demo_items.csv')
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
    ori=0, pos=(0, 0.05), size=(0.33, 0.33),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
object_rating = visual.RatingScale(win=win, name='object_rating', marker='triangle', size=1.0, pos=[0.0, -0.85], low=1, high=2,  respKeys=['num_1','num_2'], labels=['New', 'Old'], scale='', singleClick=True, disappear=True)

# Initialize components for Routine "trial_confidence_routine"
trial_confidence_routineClock = core.Clock()
confidence_object = visual.ImageStim(
    win=win,
    name='object_object', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.05), size=(0.33, 0.33),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
confidence_rating = visual.RatingScale(win=win, name='confidence_rating', marker='triangle', size=1.0, pos=[0.0, -0.85], low=1, high=3,  respKeys=['num_1','num_2','num_3'], labels=['Guess', 'Low', 'High'], scale='', singleClick=True, disappear=True)

# Initialize components for Routine "trial_scene_routine"
trial_scene_routineClock = core.Clock()
trial_scene_beach_1 = visual.ImageStim(
    win=win,
    name='trial_scene_beach_1', 
    image='sin', mask=None,
    ori=0, pos=(-0.4, 0.25), size=(0.48, 0.48),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trial_scene_beach_2 = visual.ImageStim(
    win=win,
    name='trial_scene_beach_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.4, -0.25), size=(0.48, 0.48),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
trial_scene_camp_1 = visual.ImageStim(
    win=win,
    name='trial_scene_camp_1', 
    image='sin', mask=None,
    ori=0, pos=(0.4, 0.25), size=(0.48, 0.48),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
trial_scene_camp_2 = visual.ImageStim(
    win=win,
    name='trial_scene_camp_2', 
    image='sin', mask=None,
    ori=0, pos=(0.4, -0.25), size=(0.48, 0.48),
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
    ori=0, pos=[0,0.05], size=(0.33, 0.33),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "trial_source_routine"
trial_source_routineClock = core.Clock()
trial_source_scene = visual.ImageStim(
    win=win,
    name='trial_source_scene', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.05), size=(0.85, 0.85),
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
    ori=0, pos=[0,0.05], size=(0.33, 0.33),
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
    ori=0, pos=(0, 0.05), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
scene_rating = visual.RatingScale(win=win, name='scene_rating', marker='triangle', size=1.0, pos=[0.0, -0.85], low=1, high=2, respKeys=['num_1','num_2'], labels=['Old', 'New'], scale='', singleClick=True, disappear=True)

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
stims = pd.read_csv(items_all_path)

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
objects_loop = data.TrialHandler(nReps=len(stims.path), method='sequential', 
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
    #trial_context = stims.shocked_context[trial]
    #trial_scene = scene_order[int(trial_context-1)]
    item_pos = (0,0.05)
    
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
    stamp_onoffset('onset',BIO=BIO,SHOCK=False)
    time.sleep(0.05)

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
    # the Routine "trial_object_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_confidence_routine"-------
    # update component parameters for each repeat
    confidence_object.setImage(trial_item)
    confidence_rating.reset()
    time.sleep(0.05)

    # keep track of which components have finished
    trial_confidence_routineComponents = [confidence_object, confidence_rating]
    for thisComponent in trial_confidence_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_confidence_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial_confidence_routine"-------
    while continueRoutine:
        # get current time
        t = trial_confidence_routineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_confidence_routineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *confidence_object* updates
        if confidence_object.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            confidence_object.frameNStart = frameN  # exact frame index
            confidence_object.tStart = t  # local t and not account for scr refresh
            confidence_object.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confidence_object, 'tStartRefresh')  # time at next scr refresh
            confidence_object.setAutoDraw(True)
        # *confidence_rating* updates
        if confidence_rating.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            confidence_rating.frameNStart = frameN  # exact frame index
            confidence_rating.tStart = t  # local t and not account for scr refresh
            confidence_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confidence_rating, 'tStartRefresh')  # time at next scr refresh
            confidence_rating.setAutoDraw(True)
        continueRoutine &= confidence_rating.noResponse  # a response ends the trial
        #if rating_no_force_end.status == FINISHED and object.status==FINISHED:
        #    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_confidence_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    stamp_onoffset('offset',BIO=BIO,SHOCK=False)
    # -------Ending Routine "trial_confidence_routine"-------
    for thisComponent in trial_confidence_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    objects_loop.addData('confidence_object.started', confidence_object.tStartRefresh)
    objects_loop.addData('confidence_object.stopped', confidence_object.tStopRefresh)
    # store data for objects_loop (TrialHandler)
    objects_loop.addData('confidence_rating.response', confidence_rating.getRating())
    objects_loop.addData('confidence_rating.rt', confidence_rating.getRT())
    objects_loop.addData('confidence_rating.started', confidence_rating.tStart)
    objects_loop.addData('confidence_rating.stopped', confidence_rating.tStop)
    if rating == 1:
        trial_jitter_time = 6
    else:
        trial_jitter_time = 2
    # the Routine "trial_confidence_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    

    # ------Prepare to start Routine "trial_scene_routine"-------
    # update component parameters for each repeat
    
    mouse.setPos((0,0.05))
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
        if rating == 1:
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
                    if gotValidClick:
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
        rating = 1
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
    if rating == 1:
        continueRoutine = False
    
    mouse.setPos((0,0.05))
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
        if rating == 1:
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

# save item stimuli
stims["onsets"] = onstamps
stims["offsets"] = offstamps
onstamps = list()
offstamps = list()

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
