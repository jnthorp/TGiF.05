#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Thu Feb 20 12:30:39 2020
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

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'pre-conditioning_demo'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = os.path.dirname(_thisDir) + os.sep + u'Data/%s/%s_%s_%s' % (expInfo['participant'], expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jnthorp/Documents/TGIF/Protocol/pre-conditioning_demo.py',
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
    fullscr=True, screen=0, 
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
#Begin Experiment

# import libraries
import random, xlrd, time, pickle, csv, pandas as pd, os #xlsxwriter and timer, pickle to save variables
from psychopy.sound import Sound
# import libraries and specify SCR port address
#from psychopy import parallel
import time

#port = parallel.PParallelInpOut32 (address = 0x0378 )
#port = parallel.PParallelDLPortIO (address = 0x0378)

#parallel.setPortAddress(0xEFF8)
#port = parallel.ParallelPort(address = 0xEFF4) #auto-choose one of the above

#parallel.setData(255)  # sets all pins high
#parallel.setData(0)  # sets all pins low

#def send_markers(markers):
#    for trig in markers:
#        parallel.setData(trig)
#        time.sleep(0.010)  # wait for 10 [ms]

#markers = range(4)
#send_markers(markers)

#def sendTrigger(code):
#    parallel.setData(code)
#    core.wait(0.01)
#    parallel.setData(0)

#randomize the seed
random.seed()

#stimulus file
#expDir = os.path.join('/Users','jnthorp','Documents','TGIF')
#expDir = os.path.join('/Users','john','Library','Mobile Documents','com~apple~CloudDocs','Documents','TGIF')
expDir = os.path.dirname(os.getcwd())
data_dir = os.path.join(expDir,'Data')
full_stim_path = os.path.join(expDir, 'Lists', 'pre-conditioning_demo_items.csv')
counterbalance_path = os.path.join(expDir,'Lists','counterbalance.csv')
beach_scene_1 = os.path.join(expDir,'Stimuli','pre-conditioning','beach_scene-1.png')
beach_scene_2 = os.path.join(expDir,'Stimuli','pre-conditioning','beach_scene-2.png')
beach_sound = os.path.join(expDir, 'Stimuli', 'pre-conditioning','beach_sound.wav')
camp_scene_1 = os.path.join(expDir,'Stimuli','pre-conditioning','camp_scene-1.png')
camp_scene_2 = os.path.join(expDir,'Stimuli','pre-conditioning','camp_scene-2.png')
camp_sound = os.path.join(expDir, 'Stimuli', 'pre-conditioning','camp_sound.wav')

#num of items total
num_events = 8
num_trialspevent = 6

num_trials = num_trialspevent*num_events

#access the xls stimulus file
subj_stims = pd.read_csv(full_stim_path)


# Initialize components for Routine "wait_S"
wait_SClock = core.Clock()
text_waitS = visual.TextStim(win=win, name='text_waitS',
    text='The experiment will start in a moment.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_waitS = keyboard.Keyboard()

# Initialize components for Routine "event_init_routine"
event_init_routineClock = core.Clock()
#current_enc_trial
#enc_trial = 0
event_idx = 0

rating = list()
#current_arrow_trial
#arrow_trial = 0


# Initialize components for Routine "event_jitter_routine"
event_jitter_routineClock = core.Clock()
event_jitter_text = visual.TextStim(win=win, name='event_jitter_text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "event_onset_routine"
event_onset_routineClock = core.Clock()
event_onset_scene = visual.ImageStim(
    win=win,
    name='event_onset_scene', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.05), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial_init_routine"
trial_init_routineClock = core.Clock()
trial = 0


# Initialize components for Routine "trial_jitter_routine"
trial_jitter_routineClock = core.Clock()
trial_jitter_scene = visual.ImageStim(
    win=win,
    name='trial_jitter_scene', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.05), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "trial_onset_routine"
trial_onset_routineClock = core.Clock()
trial_onset_scene = visual.ImageStim(
    win=win,
    name='trial_onset_scene', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.05), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
trial_onset_object = visual.ImageStim(
    win=win,
    name='trial_onset_object', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.33,0.33),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trial_onset_rating = visual.RatingScale(win=win, name='trial_onset_rating', size=1.0, pos=[0.0, -0.85], low=1, high=3, respKeys=['num_1','num_2','num_3'], labels=['Unlikely', 'Not Sure', 'Likely'], scale='', singleClick=True, showAccept=False)
 
# Initialize components for Routine "scene_sound_off"
scene_sound_offClock = core.Clock()

# Initialize components for Routine "blank_screen"
blank_screenClock = core.Clock()
text_blank = visual.TextStim(win=win, name='text_blank',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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

# ------Prepare to start Routine "wait_S"-------
# update component parameters for each repeat
key_waitS.keys = []
key_waitS.rt = []
# keep track of which components have finished
wait_SComponents = [text_waitS, key_waitS]
for thisComponent in wait_SComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wait_SClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "wait_S"-------
while continueRoutine:
    # get current time
    t = wait_SClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wait_SClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_waitS* updates
    if text_waitS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_waitS.frameNStart = frameN  # exact frame index
        text_waitS.tStart = t  # local t and not account for scr refresh
        text_waitS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_waitS, 'tStartRefresh')  # time at next scr refresh
        text_waitS.setAutoDraw(True)
    
    # *key_waitS* updates
    waitOnFlip = False
    if key_waitS.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_waitS.frameNStart = frameN  # exact frame index
        key_waitS.tStart = t  # local t and not account for scr refresh
        key_waitS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_waitS, 'tStartRefresh')  # time at next scr refresh
        key_waitS.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_waitS.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_waitS.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_waitS.status == STARTED and not waitOnFlip:
        theseKeys = key_waitS.getKeys(keyList=['s'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_waitS.keys = theseKeys.name  # just the last key pressed
            key_waitS.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_SComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait_S"-------
for thisComponent in wait_SComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_waitS.started', text_waitS.tStartRefresh)
thisExp.addData('text_waitS.stopped', text_waitS.tStopRefresh)
# check responses
if key_waitS.keys in ['', [], None]:  # No response was made
    key_waitS.keys = None
thisExp.addData('key_waitS.keys',key_waitS.keys)
if key_waitS.keys != None:  # we had a response
    thisExp.addData('key_waitS.rt', key_waitS.rt)
thisExp.addData('key_waitS.started', key_waitS.tStartRefresh)
thisExp.addData('key_waitS.stopped', key_waitS.tStopRefresh)
thisExp.nextEntry()
#win.callOnFlip(sendTrigger, code=0)
win.flip()
# the Routine "wait_S" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
events = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='events')
thisExp.addLoop(events)  # add the loop to the experiment
thisEvent = events.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEvent.rgb)
if thisEvent != None:
    for paramName in thisEvent:
        exec('{} = thisEvent[paramName]'.format(paramName))

for thisEvent in events:
    currentLoop = events
    # abbreviate parameter names if possible (e.g. rgb = thisEvent.rgb)
    if thisEvent != None:
        for paramName in thisEvent:
            exec('{} = thisEvent[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "event_init_routine"-------
    # update component parameters for each repeat
    
    #log enc information to data file
    #thisExp.addData('image_item', image_item[enc_order[enc_trial]])
    #thisExp.addData('emotion_item', emotion_item[enc_order[enc_trial]])
    #thisExp.addData('old_new', old_new[enc_order[enc_trial]])
    #thisExp.addData('size_item', size_item[enc_order[enc_trial]])
    #thisExp.addData('enc_trial', enc_trial)
    #thisExp.nextEntry()
    
    #Define the jitter, scene, and sound for the event
    if event_idx == 0:
        event_iei = 4.5
        event_scene = beach_scene_1
        event_sound = beach_sound
        event_idx = event_idx + 1
    else:
        event_iei = 3.3
        event_scene = camp_scene_1
        event_sound = camp_sound
        event_idx = event_idx+1

    # keep track of which components have finished
    event_init_routineComponents = []
    for thisComponent in event_init_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    event_init_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "event_init_routine"-------
    while continueRoutine:
        # get current time
        t = event_init_routineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=event_init_routineClock)
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
        for thisComponent in event_init_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "event_init_routine"-------
    for thisComponent in event_init_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #current_arrow_trial
    #arrow_trial = 0
    
    # the Routine "event_init_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "event_jitter_routine"-------
    # update component parameters for each repeat
    # keep track of which components have finished
    event_jitter_routineComponents = [event_jitter_text]
    for thisComponent in event_jitter_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    event_jitter_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "event_jitter_routine"-------
    while continueRoutine:
        # get current time
        t = event_jitter_routineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=event_jitter_routineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *event_jitter_text* updates
        if event_jitter_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            event_jitter_text.frameNStart = frameN  # exact frame index
            event_jitter_text.tStart = t  # local t and not account for scr refresh
            event_jitter_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(event_jitter_text, 'tStartRefresh')  # time at next scr refresh
            event_jitter_text.setAutoDraw(True)
        if event_jitter_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > event_jitter_text.tStartRefresh + event_iei-frameTolerance:
                # keep track of stop time/frame for later
                event_jitter_text.tStop = t  # not accounting for scr refresh
                event_jitter_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(event_jitter_text, 'tStopRefresh')  # time at next scr refresh
                event_jitter_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in event_jitter_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "event_jitter_routine"-------
    for thisComponent in event_jitter_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    events.addData('event_jitter_text.started', event_jitter_text.tStartRefresh)
    events.addData('event_jitter_text.stopped', event_jitter_text.tStopRefresh)
    # the Routine "event_jitter_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "event_onset_routine"-------
    routineTimer.add(2.5)
    # update component parameters for each repeat
    event_onset_scene.setImage(event_scene)
    background_sound = sound.Sound(event_sound)
    #background_sound.setSound(event_sound)
    background_sound.play()
    
    #win.callOnFlip(sendTrigger, code=1)
    #win.flip()
    mouse = psychopy.event.Mouse()
    mouse.setVisible(0)

    rating_background = visual.RatingScale(win=win, name='rating_background', size=1.0, pos=[0.0, -0.85], low=1, high=3, labels=['Unlikely', 'Not Sure', 'Likely'], scale='', lineColor = 'Black', textColor = 'Black', markerColor = 'Gray')
    rating_background.noResponse = False
    rating_background.setAutoDraw(True)
    # keep track of which components have finished
    event_onset_routineComponents = [event_onset_scene]
    for thisComponent in event_onset_routineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    event_onset_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "event_onset_routine"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = event_onset_routineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=event_onset_routineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *event_onset_scene* updates
        if event_onset_scene.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            event_onset_scene.frameNStart = frameN  # exact frame index
            event_onset_scene.tStart = t  # local t and not account for scr refresh
            event_onset_scene.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(event_onset_scene, 'tStartRefresh')  # time at next scr refresh
            event_onset_scene.setAutoDraw(True)
        if event_onset_scene.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > event_onset_scene.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                event_onset_scene.tStop = t  # not accounting for scr refresh
                event_onset_scene.frameNStop = frameN  # exact frame index
                win.timeOnFlip(event_onset_scene, 'tStopRefresh')  # time at next scr refresh
                event_onset_scene.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in event_onset_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "event_onset_routine"-------
    for thisComponent in event_onset_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    events.addData('event_onset_scene.started', event_onset_scene.tStartRefresh)
    events.addData('event_onset_scene.stopped', event_onset_scene.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_init_routine"-------
        # update component parameters for each repeat
        #assigning the enc item
        #ImageFile2 = image_item2[enc_order2[enc_trial2]]
        #Size2 = size_item2[enc_order2[enc_trial2]]
        trial_iti = subj_stims.iti[trial]
        trial_item = subj_stims.path[trial]
        trial_x = 0
        trial_y = 0.05
        trial_loc = [trial_x,trial_y]
        
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
        trial_jitter_scene.setImage(event_scene)
        #win.callOnFlip(sendTrigger, code=1)
        #win.flip()
        # keep track of which components have finished
        trial_jitter_routineComponents = [trial_jitter_scene]
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
            
            # *trial_jitter_scene* updates
            if trial_jitter_scene.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_jitter_scene.frameNStart = frameN  # exact frame index
                trial_jitter_scene.tStart = t  # local t and not account for scr refresh
                trial_jitter_scene.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_jitter_scene, 'tStartRefresh')  # time at next scr refresh
                trial_jitter_scene.setAutoDraw(True)
            if trial_jitter_scene.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_jitter_scene.tStartRefresh + trial_iti-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_jitter_scene.tStop = t  # not accounting for scr refresh
                    trial_jitter_scene.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trial_jitter_scene, 'tStopRefresh')  # time at next scr refresh
                    trial_jitter_scene.setAutoDraw(False)
            
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
        trials.addData('trial_jitter_scene.started', trial_jitter_scene.tStartRefresh)
        trials.addData('trial_jitter_scene.stopped', trial_jitter_scene.tStopRefresh)
        # the Routine "trial_jitter_routine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial_onset_routine"-------
        # update component parameters for each repeat
        trial_onset_scene.setImage(event_scene)
        trial_onset_object.setPos(trial_loc)
        trial_onset_object.setImage(trial_item)
        trial_onset_rating.reset()
        #win.callOnFlip(sendTrigger, code=1)
        #win.flip()
        # keep track of which components have finished
        trial_onset_routineComponents = [trial_onset_scene, trial_onset_object, trial_onset_rating]
        for thisComponent in trial_onset_routineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_onset_routineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "trial_onset_routine"-------
        while continueRoutine:
            # get current time
            t = trial_onset_routineClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_onset_routineClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trial_onset_scene* updates
            if trial_onset_scene.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_onset_scene.frameNStart = frameN  # exact frame index
                trial_onset_scene.tStart = t  # local t and not account for scr refresh
                trial_onset_scene.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_onset_scene, 'tStartRefresh')  # time at next scr refresh
                trial_onset_scene.setAutoDraw(True)
            
            # *trial_onset_object* updates
            if trial_onset_object.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_onset_object.frameNStart = frameN  # exact frame index
                trial_onset_object.tStart = t  # local t and not account for scr refresh
                trial_onset_object.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_onset_object, 'tStartRefresh')  # time at next scr refresh
                trial_onset_object.setAutoDraw(True)
            if trial_onset_object.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_onset_object.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_onset_object.tStop = t  # not accounting for scr refresh
                    trial_onset_object.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trial_onset_object, 'tStopRefresh')  # time at next scr refresh
                    trial_onset_object.setAutoDraw(False)
            # *trial_onset_rating* updates
            if trial_onset_rating.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                trial_onset_rating.frameNStart = frameN  # exact frame index
                trial_onset_rating.tStart = t  # local t and not account for scr refresh
                trial_onset_rating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_onset_rating, 'tStartRefresh')  # time at next scr refresh
                trial_onset_rating.setAutoDraw(True)
            if trial_onset_rating.status == FINISHED and trial_onset_object.status==FINISHED:
                continueRoutine = False
            if trial_onset_rating.noResponse == False:
                trial_onset_rating.lineColor = 'Gray'
                trial_onset_rating.markerColor = 'Gray'
                trial_onset_rating.setAutoDraw(False)
                trial_onset_rating.draw()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_onset_routineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_onset_routine"-------
        for thisComponent in trial_onset_routineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('trial_onset_scene.started', trial_onset_scene.tStartRefresh)
        trials.addData('trial_onset_scene.stopped', trial_onset_scene.tStopRefresh)
        trials.addData('trial_onset_object.started', trial_onset_object.tStartRefresh)
        trials.addData('trial_onset_object.stopped', trial_onset_object.tStopRefresh)
        # store data for trials (TrialHandler)
        trials.addData('trial_onset_rating.response', trial_onset_rating.getRating())
        trials.addData('trial_onset_rating.rt', trial_onset_rating.getRT())
        trials.addData('trial_onset_rating.started', trial_onset_rating.tStart)
        trials.addData('trial_onset_rating.stopped', trial_onset_rating.tStop)
        rating.append(trial_onset_rating.getRating())
        
        # the Routine "trial_onset_routine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    # ------Prepare to start Routine "scene_sound_off"-------
    # update component parameters for each repeat
    
    background_sound.fadeOut(2000)
    rating_background.setAutoDraw(False)
    #win.callOnFlip(sendTrigger, code=1)
    win.flip()
    
    # keep track of which components have finished
    scene_sound_offComponents = []
    for thisComponent in scene_sound_offComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    scene_sound_offClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "scene_sound_off"-------
    while continueRoutine:
        # get current time
        t = scene_sound_offClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=scene_sound_offClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scene_sound_offComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "scene_sound_off"-------
    for thisComponent in scene_sound_offComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "scene_sound_off" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'events'


# ------Prepare to start Routine "blank_screen"-------
routineTimer.add(0.500000)
# update component parameters for each repeat
#win.callOnFlip(sendTrigger, code=4)
#win.flip()

subj_stims['likely'] = rating
#pd.DataFrame.to_csv(subj_stims,os.path.join(data_dir,'subj_stims.csv'))
# keep track of which components have finished
blank_screenComponents = [text_blank]
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
while continueRoutine and routineTimer.getTime() > 0:
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
    if text_blank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_blank.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_blank.tStop = t  # not accounting for scr refresh
            text_blank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_blank, 'tStopRefresh')  # time at next scr refresh
            text_blank.setAutoDraw(False)
    
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
