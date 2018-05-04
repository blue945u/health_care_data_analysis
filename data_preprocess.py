import pandas as pd

df_1999 = pd.read_csv('../new_data/1999-2000Demography_DEMO.csv')
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
data1999.to_csv('../preprocessed/1999-2000Demography_DEMO-ok.csv', index=False)

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
data1999.to_csv('../preprocessed/1999-2000MuscleMassDXA_All Years-ok.csv', index=False)

df_1999 = pd.read_csv('../new_data/1999-2000MuscleStrength_MSX.csv')
data1999 = df_1999.loc[:, ['SEQN',
                           'MSDEXCLU',
                           'MSXWTIME',
                           'MSXWPAIN',
                           'MSXARML',
                           'MSDAPF']]
data1999 = data1999.rename(columns={'SEQN': 'ID',
                                    'MSDEXCLU': 'Exclusion_criteria_for_muscle_strength',
                                    'MSXWTIME': 'Time_to_complete_20_ft_walk',
                                    'MSXWPAIN': 'Pain_reported_on_walking',
                                    'MSXARML': 'Arm_length_cm',
                                    'MSDAPF': 'Average_peak_force',
                                    })
data1999.to_csv('../preprocessed/1999-2000MuscleStrength_MSX-ok.csv', index=False)

df_1999 = pd.read_csv('../new_data/1999-2000Cardiovascular_CDQHealth.csv')
data1999 = df_1999.loc[:, ['SEQN',
                           'CDQ010',
                           'CDQ020',
                           'CDQ030',
                           'CDQ040']]
data1999 = data1999.rename(columns={'SEQN': 'ID',
                                    'CDQ010': 'Shortness_of_breath_on_stairs_inclines',
                                    'CDQ020': 'Short_of_breath_walking_on_level_surface',
                                    'CDQ030': 'Stop_for_breath_walking_at_own_pace',
                                    'CDQ040': 'Stop_for_breath_walking_100_yards',
                                    })
data1999.to_csv('../preprocessed/1999-2000Cardiovascular_CDQHealth-ok.csv', index=False)

df_1999 = pd.read_csv('../new_data/1999-2000Diabetes.csv')
data1999 = df_1999.loc[:, ['SEQN',
                           'DIQ010',
                           'DIQ050',
                           'DIQ080']]
data1999 = data1999.rename(columns={'SEQN': 'ID',
                                    'DIQ010': 'Doctor_told_you_have_diabetes',
                                    'DIQ050': 'Taking_insulin_now',
                                    'DIQ080': 'Diabetes_affected_eyes_had_retinopathy',
                                    })
data1999.to_csv('../preprocessed/1999-2000Diabetes-ok.csv', index=False)

df_1999 = pd.read_csv('../new_data/1999-2000Diet_DRXTOT.csv')
data1999 = df_1999.loc[:, ['SEQN',
                           'DIQ010',
                           'DIQ050',
                           'DIQ080']]
data1999 = data1999.rename(columns={'SEQN': 'ID',
                                    'DIQ010': 'Doctor_told_you_have_diabetes',
                                    'DIQ050': 'Taking_insulin_now',
                                    'DIQ080': 'Diabetes_affected_eyes_had_retinopathy',
                                    })
data1999.to_csv('../preprocessed/1999-2000Diabetes-ok.csv', index=False)