import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math

"""
df_1999 = pd.read_csv('./new_data/1999-2000.csv')
data1999 = df_1999.rename(columns = {'SEQN' : 'ID',
                          'DXDRLLE' : 'Right_leg_EXBMC',
                          'DXDRALE' : 'Right_arm_EXBMC',
                          'DXDLLLE' : 'Left_leg_EXBMC',
                          'DXDLALE' : 'Left_arm_EXBMC'})
data1999 = data1999.loc[:, ['ID', 'Right_leg_EXBMC', 'Right_arm_EXBMC', 'Left_leg_EXBMC','Left_arm_EXBMC']]
data1999['Total_BMC'] = data1999['Right_leg_EXBMC'] + data1999['Right_arm_EXBMC'] + data1999['Left_leg_EXBMC'] + data1999['Left_arm_EXBMC']
data1999['Arm_BMC'] = data1999['Right_arm_EXBMC'] + data1999['Left_arm_EXBMC']
data1999['Leg_BMC'] = data1999['Right_leg_EXBMC'] + data1999['Left_leg_EXBMC']
data1999.to_csv('1999-2000-ok.csv',index=False)
"""

df_1999 = pd.read_csv('../new_data/1999-2000(Demo).csv')
print(df_1999.shape)