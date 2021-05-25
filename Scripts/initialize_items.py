import os
import sys
import pandas as pd
import numpy as np
import re
import random
import glob

exp_dir = os.getcwd()

stim_path = os.path.join(exp_dir,'Stimuli','items','*','*','*')
stims_full_path = [f for f in glob.glob(stim_path) if 'DS.Store' not in f]
stims_filename = [f.rsplit(os.sep,1)[1] for f in stims_full_path]
stims_item = [re.split('.png', i)[0] for i in stims_filename]
stims_group = [int(re.split('group', i)[1][0]) for i in stims_full_path]
beach_con = [''.join([os.sep, 'beach', os.sep]) in i for i in stims_full_path]
camp_con = [''.join([os.sep, 'camp', os.sep]) in i for i in stims_full_path]
incon = [''.join([os.sep, 'incongruent', os.sep]) in i for i in stims_full_path]


cols = ['path','filename','item','group','beach','camp','incongruent']
df_all_stims = pd.DataFrame(list(zip(stims_full_path, 
                                     stims_filename,
                                     stims_item,
                                     stims_group,
                                     beach_con, 
                                     camp_con,
                                     incon)))
df_all_stims.columns = cols

subj_list = np.array(range(101,131))
old = np.tile([1,2], 30)
CSplus = np.tile(['beach','camp'], 30)
conditioning = np.tile([1,2],30)
counterbalance_df = pd.DataFrame(list(zip(subj_list,
                                          old,
                                          CSplus,
                                          conditioning
                                         )), columns = ['subject', 'old','CSplus','conditioning'])

pd.DataFrame.to_csv(df_all_stims,os.path.join(exp_dir,'Lists','stim_list.csv'))
pd.DataFrame.to_csv(counterbalance_df,os.path.join(exp_dir,'Lists','counterbalance.csv'))