import pandas as pd

df_1999 = pd.read_csv('../new_data/1999-2000Demography_DEMO.csv')
data1999 = df_1999.loc[:, ['SEQN', 'RIAGENDR', 'RIDAGEYR', 'RIDAGEMN', 'RIDAGEEX', 'RIDRETH1', 'DMDEDUC3', 'DMDEDUC2',
                           'DMDMARTL', 'RIDEXPRG', 'RIDPREG']]
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
data1999.to_csv('../preprocessed/1999-2000MuscleMassDXA_All Years-ok.csv', index=False)

df_1999 = pd.read_csv('../new_data/1999-2000MuscleStrength_MSX.csv')
data1999 = df_1999.loc[:, ['SEQN',
                           'MSDEXCLU',
                           'MSXWTIME',
                           'MSXWPAIN',
                           'MSXARML',
                           'MSDAPF']]
data1999.to_csv('../preprocessed/1999-2000MuscleStrength_MSX-ok.csv', index=False)

df_1999 = pd.read_csv('../new_data/1999-2000Cardiovascular_CDQHealth.csv')
data1999 = df_1999.loc[:, ['SEQN',
                           'CDQ010',
                           'CDQ020',
                           'CDQ030',
                           'CDQ040']]
data1999.to_csv('../preprocessed/1999-2000Cardiovascular_CDQHealth-ok.csv', index=False)

df_1999 = pd.read_csv('../new_data/1999-2000Diabetes.csv')
data1999 = df_1999.loc[:, ['SEQN',
                           'DIQ010',
                           'DIQ050',
                           'DIQ080']]
data1999.to_csv('../preprocessed/1999-2000Diabetes-ok.csv', index=False)

df_1999 = pd.read_csv('../new_data/1999-2000Diet_DRXTOT.csv')
data1999 = df_1999.loc[:, ['SEQN',
                           'WTDRD1',
                           'WTDR4YR',
                           'DRDTSODF',
                           'DRXTKCAL',
                           'DRXTPROT',
                           'DRXTCARB',
                           'DRXTTFAT',
                           'DRXTSFAT',
                           'DRXTMFAT',
                           'DRXTPFAT',
                           'DRXTCHOL',
                           'DRXTFIBE',
                           'DRXTCALC',
                           'DRDTSODI',
                           'DRXTPOTA'
                           ]]
data1999.to_csv('../preprocessed/1999-2000Diet_DRXTOT-ok.csv', index=False)

df_1999 = pd.read_csv('../new_data/1999-2000Depression.csv')
data1999 = df_1999.loc[:, ['SEQN',
                           'CIDDSCOR']]
data1999.to_csv('../preprocessed/1999-2000Depression-ok.csv', index=False)