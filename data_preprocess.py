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


df_1999 = pd.read_csv('../new_data/1999-2000(Demo).csv')
data1999 = df_1999.loc[:, ['SEQN','RIAGENDR','RIDAGEYR','RIDAGEMN','RIDAGEEX','RIDRETH1','DMDEDUC3','DMDEDUC2',
                           'DMDMARTL','RIDEXPRG','RIDPREG']]
data1999 = data1999.rename(columns={'SEQN': 'ID',
                                   'RIAGENDR': 'Gender',
                                   'RIDAGEYR': 'Age_at_Screening_Adjudicated',
                                   'RIDAGEMN': 'Age_in_Months',
                                   'RIDAGEEX': 'Exam_Age_in_Months',
                                   'RIDRETH1': 'Race_Ethnicity',
                                   'DMDEDUC3': 'Education_Level_Children_Youth_6_19',
                                   'DMDEDUC2': 'Education_Level_Adults_20',
                                   'DMDMARTL': 'Marital_Status',
                                   'RIDEXPRG': 'Pregnancy_Status_at_Exam',
                                   'RIDPREG': 'Pregnancy_Status',
                                   })
data1999.to_csv('../new_data/1999-2000-demo-ok.csv', index=False)
"""
df_1999 = pd.read_csv('../new_data/1999-2000MuscleMassDXA_All Years.csv')
data1999 = df_1999.loc[:, ['SEQN',
                           'DXXLAFAT',
                           'DXDLALE',
                           'DXDLATOT',
                           'DXDLAPF',
                           'DXXLLFAT',
                           'DXDLLLE',
                           'DXDLLTOT',
                           'DXDLLPF',
                           'DXXRAFAT',
                           'DXDRALE',
                           'DXDRATOT',
                           'DXDRAPF',
                           'DXXRLFAT',
                           'DXDRLLE',
                           'DXDRLTOT',
                           'DXDRLPF',
                           'DXXTRFAT',
                           'DXDTRLE',
                           'DXDTRTOT',
                           'DXDTRPF',
                           'DXDSTFAT',
                           'DXDSTLE',
                           'DXDSTTOT',
                           'DXDSTPF',
                           'DXDTOFAT',
                           'DXDTOTOT',
                           'DXDTOPF', ]]
data1999 = data1999.rename(columns={'SEQN': 'ID',
                                    'DXXLAFAT': 'Left_Arm_Fat',
                                    'DXDLALE': 'Left_Arm_Lean_excl_BMC',
                                    'DXDLATOT': 'Left_Arm_Total',
                                    'DXDLAPF': 'Left_Arm_Percent_Fat',
                                    'DXXLLFAT': 'Left_Leg_Fat',
                                    'DXDLLLE': 'Left_Leg_Lean_excl_BMC',
                                    'DXDLLTOT': 'Left_Leg Total',
                                    'DXDLLPF': 'Left_Leg_Percent_Fat',
                                    'DXXRAFAT': 'Right_Arm_Fat',
                                    'DXDRALE': 'Right_Arm_Lean_excl_BMC',
                                    'DXDRATOT': 'Right_Arm_Total',
                                    'DXDRAPF': 'Right_Arm_Percent_Fat',
                                    'DXXRLFAT': 'Right_Leg_Fat',
                                    'DXDRLLE': 'Right_Leg_Lean_excl_BMC',
                                    'DXDRLTOT': 'Right_Leg_Total',
                                    'DXDRLPF': 'Right_Leg_Percent_Fat',
                                    'DXXTRFAT': 'Trunk_Fat',
                                    'DXDTRLE': 'Trunk_Lean_excl_BMC',
                                    'DXDTRTOT': 'Trunk_Total',
                                    'DXDTRPF': 'Trunk_Percent_Fat',
                                    'DXDSTFAT': 'Subtotal_Fat',
                                    'DXDSTLE': 'Subtotal_Lean_excl_BMC',
                                    'DXDSTTOT': 'Subtotal',
                                    'DXDSTPF': 'SubtotalPercentFat',
                                    'DXDTOFAT': 'TotalFat',
                                    'DXDTOTOT': 'TotalLean_Fat',
                                    'DXDTOPF': 'TotalPercentFat',
                                    })
data1999.to_csv('../new_data/1999-2000MuscleMassDXA_All Years-ok.csv', index=False)
