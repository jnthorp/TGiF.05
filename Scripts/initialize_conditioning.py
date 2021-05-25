import os
import sys
import pandas as pd
import numpy as np
import re
import random
import glob

exp_dir = os.getcwd()

scene_alts = os.path.join(exp_dir,'Stimuli', 'conditioning','*alts','*','*') #directory of alternate scenes

stims_full_path = [f for f in glob.glob(scene_alts)] #make full list of alternate scenes
stims_filename = [f.rsplit(os.sep,1)[1] for f in stims_full_path]
stims_group = [int(re.split('group', i)[1][0]) for i in stims_full_path]
beach_con = [''.join([os.sep,'beach_']) in i for i in stims_full_path]
camp_con = [''.join([os.sep,'camp_']) in i for i in stims_full_path]

cols = ['path','filename','group','beach','camp']
df_all_stims = pd.DataFrame(list(zip(stims_full_path, 
                                     stims_filename,
                                     stims_group,
                                     beach_con, 
                                     camp_con)), columns = cols)

pd.DataFrame.to_csv(df_all_stims,os.path.join(exp_dir,'Lists','conditioning_scenes.csv'))