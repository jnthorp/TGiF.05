#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Sun Feb 16 12:17:17 2020
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
expName = 'pre-conditioning'  # from the Builder filename that created this script
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
    originPath='/Users/jnthorp/Documents/TGIF/Protocol/pre-conditioning_lastrun.py',
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
from psychopy import parallel
import time

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
event_onstamps = []

#randomize the seed
random.seed()

#stimulus file
#expDir = os.path.join('/Users','jnthorp','Documents','TGIF')
#expDir = os.path.join('/Users','john','Library','Mobile Documents','com~apple~CloudDocs','Documents','TGIF')
expDir = os.path.dirname(os.getcwd())
dataDir = os.path.join(expDir,'Data')
full_stim_path = os.path.join(expDir, 'Lists', 'stim_list.csv')
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

# Initialize components for Routine "wait_S"
wait_SClock = core.Clock()
text_waitS = visual.TextStim(win=win, name='text_waitS',
    text='The experiment will start in a moment.',
    font='Arial', pos=(0,0),
    height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_waitS = keyboard.Keyboard()

# Initialize components for Routine "event_init_routine"
event_init_routineClock = core.Clock()

event_idx = 0

rating = list()

# Initialize components for Routine "event_jitter_routine"
event_jitter_routineClock = core.Clock()
event_jitter_text = visual.TextStim(win=win, name='event_jitter_text',
    text='+',
    font='Arial',
    height=0.1, wrapWidth=None, ori=0, 
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
    texRes=128, interpolate = True, depth=-1.0)
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


mouse = psychopy.event.Mouse()
mouse.setVisible(0)

#access the xls stimulus file
full_stims = pd.read_csv(full_stim_path)
counterbalance = pd.read_csv(counterbalance_path)

#############
##Generate subject-specific stim list
#############

colnames = ['item', 'object']
random.seed()

subj_num = int(expInfo['participant'])
subj_idx = counterbalance.subject == subj_num

dataDir = os.path.join(expDir,'data',str(subj_num))
if not os.path.exists(dataDir):
    os.makedirs(dataDir)

items_to_show = np.unique(full_stims.item[(full_stims.group == int(counterbalance.old[subj_idx])) | (full_stims.group == int(counterbalance.similar[subj_idx]))])

#Randomize which exemplar of each item is shown to the participant
oldies = pd.DataFrame(list(zip(items_to_show,
                               np.random.randint(2, size = len(items_to_show)) + 1)),
                      columns = colnames)


#Label the results in full_stims in the 'old' column
full_stims['old'] = full_stims.index.isin(pd.merge(full_stims, oldies)['Unnamed: 0'])

#num of items total
num_events = 16
num_trialspevent = 12

num_trials = num_trialspevent*num_events

if list(counterbalance.CSplus[subj_idx]) == ['beach']:
    context_list = ['beach','camp']
    context_sortby = ['camp','beach']
    scene_list = [beach_scene_1, camp_scene_1, beach_scene_2, camp_scene_2]
    sound_list = [beach_sound, camp_sound]
else:
    context_list = ['camp','beach']
    context_sortby = ['beach','camp']
    scene_list = [camp_scene_1, beach_scene_1, camp_scene_2, beach_scene_2]
    sound_list = [camp_sound, beach_sound]
    
#random.shuffle(context)
subj_stims = full_stims.loc[full_stims['old'] == 1].reset_index(drop = True)

#randomize and then sort items by their context, with the context randomized per participant
subj_stims = subj_stims.sample(frac=1).sort_values(context_sortby).reset_index(drop = True)

#Assign each item to an event
subj_stims["event"] = np.concatenate([np.repeat(np.arange(1,num_events+1), num_trialspevent/2), 
                                      np.repeat(np.arange(1,num_events+1,2), num_trialspevent/2), 
                                      np.repeat(np.arange(2,num_events+1,2), num_trialspevent/2)])

#sort values by event
subj_stims = subj_stims.sort_values(by='event').reset_index(drop = True)

#Create context variable, 1 = unshocked, even number context; 2 = shocked, odd number context
subj_stims["shocked_context"] = np.tile(np.repeat([True,False], num_trialspevent), int(num_events/2))

#Shuffle the stimuli, then sort by event so that the order of congruent and incongruent stimuli is randomized across trials
subj_stims = subj_stims.sample(frac=1).sort_values(by='event').reset_index(drop = True)
subj_stims["iti"] = (np.random.random(num_trials)-0.5)*2+4 #Determine the inter-trial interval, between 3 and 5 seconds
loc_range = np.array(range(-280,-50)) + np.array(range(50,280))
rng = np.random.default_rng()
subj_stims["x"] = rng.choice(loc_range, size = num_trials)/1000  #x location that the item will display at
subj_stims["y"] = rng.choice(loc_range, size = num_trials)/1000 + 0.05 #y location that the item will display at

#pd.DataFrame.to_csv(subj_stims,os.path.join(expDir,'Scripts','Protocol','old_stims.csv'))

###########Event variables#############
#Generate the columns for the event dataframe, which is dependent on which context is CS+
cols = ['event_idx', 'iei','scene','sound']
[cols.insert(int(i+1),item) for i,item in enumerate(context_list)]
events_idx = [i for i in range(1,num_events+1)] #list of events

#Whether or not a given event is within the beach or camping context, determined by the randomization of context
context1 = np.tile([True, False], int(num_events/2))
context2 = context1 == False

iei = (np.random.random(num_events)-0.5)*4+8 #Determine the event-level inter-event interval

#List subject-dependent order of scenes and sounds
scenes = np.tile(scene_list, int(num_events/4))
sounds = np.tile(sound_list, int(num_events/2))

#Write all this to a dataframe
events_df = pd.DataFrame(list(zip(events_idx,
                                  context1,
                                  context2,
                                  iei,
                                  scenes,
                                  sounds)), columns = cols)

pd.DataFrame.to_csv(events_df,os.path.join(dataDir,'events.csv'))
pd.DataFrame.to_csv(subj_stims,os.path.join(dataDir,'pre-conditioning_stims.csv'))
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
events = data.TrialHandler(nReps=len(events_df), method='sequential', 
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
    event_iei = events_df.iei[event_idx]
    event_scene = events_df.scene[event_idx]
    event_sound = events_df.sound[event_idx]
    event_idx = event_idx + 1
    
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
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    event_onset_scene.setImage(event_scene)
    background_sound = sound.Sound(event_sound)
    #background_sound.setSound(event_sound)
    background_sound.play()
    stamp_onoffset('event_onset',BIO=BIO,SHOCK=False)
    time.sleep(0.05)
    stamp_onoffset('event_offset',BIO=BIO,SHOCK=False)
    #win.callOnFlip(sendTrigger, code=1)
    #win.flip()
    
    rating_background = visual.RatingScale(win=win, name='rating_background', size=1.0, pos=[0.0, -0.85], low=1, high=3, labels=['Unlikely', 'Not Sure', 'Likely'], scale='', lineColor = 'Gray', textColor = 'Gray', markerColor = 'Gray')
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
            if tThisFlipGlobal > event_onset_scene.tStartRefresh + 4-frameTolerance:
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
    trials = data.TrialHandler(nReps=num_trialspevent, method='random', 
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
        trial_x = subj_stims.x[trial]
        trial_y = subj_stims.y[trial]
        trial_loc = [subj_stims.x[trial],subj_stims.y[trial]]
        
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
        stamp_onoffset('onset',BIO=BIO,SHOCK=False)
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
                if tThisFlipGlobal > trial_onset_object.tStartRefresh + 4-frameTolerance:
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
                
        stamp_onoffset('offset',BIO=BIO,SHOCK=False)
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
        
    # completed num_trialspevent repeats of 'trials'
    
    
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
# completed len(events_df) repeats of 'events'


# ------Prepare to start Routine "blank_screen"-------
routineTimer.add(0.500000)
# update component parameters for each repeat
#win.callOnFlip(sendTrigger, code=4)
#win.flip()

subj_stims['likely'] = rating
pd.DataFrame.to_csv(subj_stims,os.path.join(dataDir,'subj_stims.csv'))
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
