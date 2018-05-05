import pandas as pd

df = pd.read_csv('../raw_data/1999-2000rawdata_0505_noSEQN.csv')
# Feature Importance with Extra Trees Classifier
from sklearn.ensemble import ExtraTreesClassifier
# load data
label = 'DXDTOLE'
print(df.shape) #(9188, 250)
corr_df = df.corr()
label_corr = corr_df[label]
print(label_corr)
label_corr.to_csv('../raw_data/corr.csv')