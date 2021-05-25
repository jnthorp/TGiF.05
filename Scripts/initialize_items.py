import os
import sys
import pandas as pd
import numpy as np
import re
import random
import glob

#exp_dir = os.path.join('/Users','jnthorp','Documents','TGIF')
#exp_dir = os.path.join('/Users','john','Library','Mobile Documents','com~apple~CloudDocs','Documents','TGIF')
exp_dir = os.getcwd()
stim_path = os.path.join(exp_dir,'Stimuli')
beach_scene = os.path.join(exp_dir,'Stimuli','pre-conditioning','beach.jpg')
beach_sound = os.path.join(exp_dir, 'Stimuli', 'pre-conditioning','beach.m4a')
camp_scene = os.path.join(exp_dir,'Stimuli','pre-conditioning_scenes','camp.jpg')
camp_sound = os.path.join(exp_dir, 'Stimuli', 'pre-conditioning','camp.m4a')

stim_path = os.path.join(exp_dir,'Stimuli','items','*','*','*')
stims_full_path = [f for f in glob.glob(stim_path) if 'DS.Store' not in f]
stims_filename = [f.rsplit(os.sep,1)[1] for f in stims_full_path]
stims_item = [re.split('[\- .]', i)[0] for i in stims_filename]
stims_object = [int(re.split('[\- .]', i)[1]) for i in stims_filename]
stims_group = [int(re.split('group', i)[1][0]) for i in stims_full_path]
beach_con = [''.join([os.sep, 'beach', os.sep]) in i for i in stims_full_path]
camp_con = [''.join([os.sep, 'camp', os.sep]) in i for i in stims_full_path]
incon = [''.join([os.sep, 'incongruent', os.sep]) in i for i in stims_full_path]


cols = ['path','filename','item','object','group','beach','camp','incongruent']
df_all_stims = pd.DataFrame(list(zip(stims_full_path, 
                                     stims_filename,
                                     stims_item,
                                     stims_object,
                                     stims_group,
                                     beach_con, 
                                     camp_con,
                                     incon)))
df_all_stims.columns = cols

subj_list = np.array(range(101,131))
old = np.tile(np.arange(1,4), 11)[0:31]
similar = np.tile(np.arange(1,4), 11)[1:32]
new = np.tile(np.arange(1,4), 11)[2:33]
CSplus = np.tile(['beach','camp'], 15)
conditioning = np.tile([1,2],15)
counterbalance_df = pd.DataFrame(list(zip(subj_list,
                                          old,
                                          similar,
                                          new,
                                          CSplus,
                                          conditioning
                                         )), columns = ['subject', 'old', 'similar', 'new','CSplus','conditioning'])

pd.DataFrame.to_csv(df_all_stims,os.path.join(exp_dir,'Lists','stim_list.csv'))
pd.DataFrame.to_csv(counterbalance_df,os.path.join(exp_dir,'Lists','counterbalance.csv'))