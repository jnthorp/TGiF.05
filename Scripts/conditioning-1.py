#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Sat Feb 15 15:44:25 2020
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
psychopyVersion = '2020.1.2'
expName = 'conditioning'  # from the Builder filename that created this script
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
    originPath=os.path.join('/Users/jnthorp/Documents/TGIF/Protocol/Scripts/conditioning.py'),
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
import glob
from psychopy import parallel
BIO = True

# import libraries and specify SCR port address
#from psychopy import parallel
import time




#######
###Gus Code
#######

def shock():
    port.setPin(9,1)
    time.sleep(.05)
    port.setPin(9,0)

def stamp_next_flip(on_or_offset):
    #stamp_df.loc[stamp_idx,'true_{:s}'.format(on_or_offset)] = clock.getTime()
    if 'on' in on_or_offset:
        onstamps.append(clock.getTime())
        
    elif 'off' in on_or_offset:
        offstamps.append(clock.getTime())

def stamp_onoffset(on_or_offset,BIO=False,SHOCK=False):
    win.callOnFlip(stamp_next_flip,on_or_offset)
    
    if SHOCK: shock()
    
    if BIO:
        if 'on' in on_or_offset:
            port.setPin(2,1)
            
        elif 'off' in on_or_offset:
            port.setPin(2,0)

if BIO:
    port = parallel.ParallelPort(address=0xEFF8)
    port.setData(0)



#randomize the seed
random.seed()

#stimulus file
#expDir = os.path.join('/Users','jnthorp','Documents','TGIF')
#expDir = os.path.join('/Users','john','Library','Mobile Documents','com~apple~CloudDocs','Documents','TGIF')
expDir = os.path.dirname(os.getcwd())
beach_scene_1 = os.path.join(expDir,'Stimuli','conditioning','beach_scene-1.png') #pre-conditioning beach scene
beach_scene_2 = os.path.join(expDir, 'Stimuli','conditioning','beach_scene-2.png') #pre-conditioning beach scene
beach_scene = [beach_scene_1,beach_scene_2]
beach_sound = os.path.join(expDir, 'Stimuli', 'conditioning','beach_sounds','*') #directory with the alternative beach scenes
camp_scene_1 = os.path.join(expDir,'Stimuli','conditioning','camp_scene-1.png') #pre-conditioning camp scene
camp_scene_2 = os.path.join(expDir, 'Stimuli','conditioning','camp_scene-2.png') #pre-conditioning camp scene
camp_scene = [camp_scene_1, camp_scene_2]
camp_sound = os.path.join(expDir, 'Stimuli', 'conditioning','camp_sounds','*') #directory with the alternative camp scenes

full_stim_path = os.path.join(expDir,'Lists','conditioning_scenes.csv') #csv with all the conditioning stims compiled by initialize_conditioning_stims.py
counterbalance_path = os.path.join(expDir,'Lists','counterbalance.csv') #csv with subject-level counterbalance data

trials = 96

# Initialize components for Routine "wait_routine"
wait_routineClock = core.Clock()
wait_text = visual.TextStim(win=win, name='wait_text',
    text='The experiment will start in a moment.',
    font='Arial',
    height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
wait_key = keyboard.Keyboard()

# Initialize components for Routine "trial_init_routine"
trial_init_routineClock = core.Clock()
trial = 0


# Initialize components for Routine "trial_jitter_routine"
trial_jitter_routineClock = core.Clock()
trial_jitter_text = visual.TextStim(win=win, name='trial_jitter_text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_scene_routine"
trial_scene_routineClock = core.Clock()
trial_scene_scene = visual.ImageStim(
    win=win,
    name='trial_scene_scene', 
    image='sin', mask=None,
    ori=0, pos=(0, 0.05), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
trial_scene_rating = visual.RatingScale(win=win, name='trial_scene_rating', marker='triangle', size=1.0, pos=[0.0, -0.85], low=1, high=2,  respKeys=['num_1','num_2'], labels=['No', 'Yes'], scale='', singleClick=True, disappear=True, showAccept=False)

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

#access the xls stimulus file
full_stims = pd.read_csv(full_stim_path) #read in all the conditioning stims
counterbalance = pd.read_csv(counterbalance_path) #read in the counterbalance csv

#############
##Generate subject-specific stim list
#############
random.seed()

subj_num = int(expInfo['participant']) #read in the participant number
subj_idx = counterbalance.subject == subj_num #index subj_num within the counterbalance df
dataDir = os.path.join(expDir, 'Data', str(subj_num)) #location of the data directory for this subject

#read the stimuli from the proper group, as determined by counterbalance
stims = full_stims[(full_stims.group == int(counterbalance.conditioning[subj_idx]))]
stims = stims.drop(['group'], axis=1) #drop group from the stimuli df
cols = ['path','filename','beach','camp'] #columns for the stimuli df going forward

#add 24 repetitions of the pre-conditioning beach scene to the stimuli df
beach_scene_tile = np.tile(beach_scene, int(trials/8))
beach_scene_filename = np.tile([beach_scene[0].rsplit(os.sep,1)[1],beach_scene[1].rsplit(os.sep,1)[1]], int(trials/4))
beach_beach_con = np.tile([True], int(trials/4))
beach_camp_con = np.tile([False], int(trials/4))

stims = stims.append(pd.DataFrame(list(zip(beach_scene_tile,
                                                            beach_scene_filename,
                                                            beach_beach_con,
                                                            beach_camp_con)),
                                                   columns = cols))

#add pre-conditioning camp scene to stimuli df
camp_scene_tile = np.tile(camp_scene, int(trials/8))
camp_scene_filename = np.tile([camp_scene[0].rsplit(os.sep,1)[1],camp_scene[1].rsplit(os.sep,1)[1]], int(trials/8))
camp_beach_con = np.tile([False], int(trials/4))
camp_camp_con = np.tile([True], int(trials/4))

stims = stims.append(pd.DataFrame(list(zip(camp_scene_tile,
                                                            camp_scene_filename,
                                                            camp_beach_con,
                                                            camp_camp_con)),
                                                   columns = cols))

#randomize which sound will be played on each trial, from 1 - 8
sound_num = [random.randint(0,7) for i in range(len(stims))]

#list full directory of sounds for both beach and camp
beach_sound_full = [i for i in glob.glob(beach_sound) if '.DS_Store' not in i]
camp_sound_full = [i for i in glob.glob(camp_sound) if '.DS_Store' not in i]

stims = stims.sort_values('beach').reset_index(drop = True) #sort stims by beach so that sounds can be added properly

#add paths of the sounds to be used for each trial, as determined by sound_num
print(len(stims))
stims['sound_path'] = [camp_sound_full[sound_num[i]] for i in range(0,int(trials/2))] + [beach_sound_full[sound_num[i]] for i in range(int(trials/2),trials)]

#determine the iti for each trial, from 6 to 8 seconds
stims["iti"] = (np.random.random(trials)-0.5)*2+7 #Determine the inter-trial interval, between 6 and 10 seconds

#determine which trials to shock
CSplus = list(counterbalance.CSplus[subj_idx]) #find CSplus in counterbalance
stims = stims.sort_values([CSplus[0],'filename']).reset_index(drop = True) #sort stims by the CSplus and by the filename type (alt or pre-conditioning)
stims['shock'] = np.repeat([False,False,False,False,False,True,True,False], int(trials/8)) #add column of False and True, with CSplus being shocked 50% of the time, regardless of file type


#While loop to shuffle stimuli so that:
# no pre-conditioning scenes repeat right after themselves
# there are never three in a row of CSplus or CSminus
while 1:
    index = [i for i in stims.index]

    shuffle = []

    while index:
        l = index
        if shuffle:
            l = [x for x in l if stims.filename[x] != stims.filename[shuffle[-1]]]
        if len(shuffle) > 3 and stims.beach[shuffle[-1]] == stims.beach[shuffle[-2]] and stims.beach[shuffle[-1]] == stims.beach[shuffle[-3]]:
            l = [x for x in l if stims.beach[x] != stims.beach[shuffle[-1]]]
        if not l:
            #no valid solution
            break
 
        newEl = random.choice(l)
        shuffle.append(newEl)
        index.remove(newEl)
    if not index:
        break

#shuffle the stims according to shuffle
stims = stims.iloc[shuffle].reset_index(drop = True)

#store the dataframe as 'conditioning_stims.csv'
pd.DataFrame.to_csv(stims,os.path.join(dataDir, 'conditioning_stims.csv'))

onstamps = list()
offstamps = list()

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
trials = data.TrialHandler(nReps=trials, method='random', 
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
    
    if trial > 0:
        background_sound.fadeOut(1000)
    
    trial_iti = stims.iti[trial]
    trial_item = stims.path[trial]
    trial_sound = stims.sound_path[trial]
    SHOCK = stims.shock[trial]
    
    #log enc information to data file
    #thisExp.addData('image_item', image_item2[enc_order2[enc_trial2]])
    #thisExp.addData('emotion_item', emotion_item2[enc_order2[enc_trial2]])
    #thisExp.addData('old_new', old_new2[enc_order2[enc_trial2]])
    #thisExp.addData('size_item', size_item2[enc_order2[enc_trial2]])
    #thisExp.addData('enc_trial', enc_trial2)
    #thisExp.nextEntry()
    
    #increment the current enc item counter
    trial = trial + 1
    myMarker = visual.TextStim(win=win,text='',units='norm')
    rating_background = visual.RatingScale(win=win, name='rating_background', size=1.0, pos=[0.0, -0.85], low=1, high=2, labels=['No','Yes'], scale='', lineColor = 'Gray', textColor = 'Gray', marker = myMarker)
    rating_background.noResponse = False
    rating_background.setAutoDraw(True)
    
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
    
    background_sound = sound.Sound(trial_sound)

    mouse = psychopy.event.Mouse()
    mouse.setVisible(0)

    # keep track of which components have finished
    trial_jitter_routineComponents = [trial_jitter_text]
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
        
        # *trial_jitter_text* updates
        if trial_jitter_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_jitter_text.frameNStart = frameN  # exact frame index
            trial_jitter_text.tStart = t  # local t and not account for scr refresh
            trial_jitter_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_jitter_text, 'tStartRefresh')  # time at next scr refresh
            trial_jitter_text.setAutoDraw(True)
        if trial_jitter_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_jitter_text.tStartRefresh + trial_iti-frameTolerance:
                # keep track of stop time/frame for later
                trial_jitter_text.tStop = t  # not accounting for scr refresh
                trial_jitter_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_jitter_text, 'tStopRefresh')  # time at next scr refresh
                trial_jitter_text.setAutoDraw(False)
        
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
    trials.addData('trial_jitter_text.started', trial_jitter_text.tStartRefresh)
    trials.addData('trial_jitter_text.stopped', trial_jitter_text.tStopRefresh)
    # the Routine "trial_jitter_routine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_scene_routine"-------
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    trial_scene_scene.setImage(trial_item)
    trial_scene_rating.reset()
    
    background_sound.play()
    
    stamp_onoffset('onset',BIO=BIO,SHOCK=False)
    start = clock.getTime()
    flag = True
    
    #win.callOnFlip(sendTrigger, code=1)
    #win.flip()
    # keep track of which components have finished
    trial_scene_routineComponents = [trial_scene_scene, trial_scene_rating]
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_scene_routineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_scene_routineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_scene_scene* updates
        if trial_scene_scene.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_scene_scene.frameNStart = frameN  # exact frame index
            trial_scene_scene.tStart = t  # local t and not account for scr refresh
            trial_scene_scene.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_scene_scene, 'tStartRefresh')  # time at next scr refresh
            trial_scene_scene.setAutoDraw(True)
        if trial_scene_scene.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_scene_scene.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                trial_scene_scene.tStop = t  # not accounting for scr refresh
                trial_scene_scene.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_scene_scene, 'tStopRefresh')  # time at next scr refresh
                trial_scene_scene.setAutoDraw(False)

        # *trial_scene_rating* updates
        if trial_scene_rating.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            trial_scene_rating.frameNStart = frameN  # exact frame index
            trial_scene_rating.tStart = t  # local t and not account for scr refresh
            trial_scene_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_scene_rating, 'tStartRefresh')  # time at next scr refresh
            trial_scene_rating.setAutoDraw(True)

        
        if trial_scene_rating.noResponse == False:
            trial_scene_rating.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        # for thisComponent in trial_scene_routineComponents:
        #     if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
        #         continueRoutine = True
        #         break  # at least one component has not yet finished
        if trial_scene_scene.status != FINISHED:
            continueRoutine = True
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    ####Added by John, will shock on offset
    stamp_onoffset('offset',BIO=BIO,SHOCK=SHOCK)
    # -------Ending Routine "trial_scene_routine"-------
    for thisComponent in trial_scene_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('trial_scene_scene.started', trial_scene_scene.tStartRefresh)
    trials.addData('trial_scene_scene.stopped', trial_scene_scene.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('trial_scene_rating.response', trial_scene_rating.getRating())
    trials.addData('trial_scene_rating.rt', trial_scene_rating.getRT())
    trials.addData('trial_scene_rating.started', trial_scene_rating.tStart)
    trials.addData('trial_scene_rating.stopped', trial_scene_rating.tStop)
    thisExp.nextEntry()
    
# completed 96 repeats of 'trials'


# ------Prepare to start Routine "blank_screen"-------
routineTimer.add(0.500000)
# update component parameters for each repeat


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

stims['onset'] = onstamps
stims['offset'] = offstamps

pd.DataFrame.to_csv(stims,os.path.join(dataDir,'conditioning_stims.csv'))

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
