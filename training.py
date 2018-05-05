from sklearn.metrics import mean_squared_error
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import pandas as pd
raw_df = pd.read_csv('../raw_data/1999-2000rawdata_0505_noSEQN.csv')
#raw_df = raw_df.loc[:, ['DXDTRPF','DXDTOPF','DXDSTPF','DXDRLPF','DXDLLPF','DXDRAPF','DXDLAPF','DXDTOLE']]

label_column = 'DXDTOLE'
y = raw_df[label_column]
X = raw_df.drop(label_column, axis=1)
# training
k=10
print('=====================cross_val_score============================')
linear_regression_model = linear_model.LinearRegression()
scores = cross_val_score(linear_regression_model, X=X, y=y, cv=k, scoring='neg_mean_squared_error')
print('linear %f' % abs(scores.mean()))

regression_model = linear_model.Lasso()
scores = cross_val_score(regression_model, X=X, y=y, cv=k, scoring='neg_mean_squared_error')
print('Lasso %f' % abs(scores.mean()))

regression_model = linear_model.Ridge()
scores = cross_val_score(regression_model, X=X, y=y, cv=k, scoring='neg_mean_squared_error')
print('Ridge %f' % abs(scores.mean()))

regression_model = linear_model.ElasticNet()
scores = cross_val_score(regression_model, X=X, y=y, cv=k, scoring='neg_mean_squared_error')
print('ElasticNet %f' % abs(scores.mean()))

print('=====================cross_val_score============================')
m1_train_data, m1_test_data, m1_train_label, m1_test_label = train_test_split(X, y, test_size=0.4, random_state=42)
print(m1_train_data.shape)
"""
print('=====================training m1============================')
linear_regression_model = linear_model.LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=1)
scores = cross_val_score(linear_regression_model, X=X, y=y, cv=k, scoring='neg_mean_squared_error')
print('linear %f' % abs(scores.mean()))

regression_model = linear_model.Lasso(alpha=0.1, copy_X=True, fit_intercept=True, max_iter=1000,
                                      normalize=False, positive=False, precompute=False, random_state=None,
                                      selection='cyclic', tol=0.0001, warm_start=False)
scores = cross_val_score(regression_model, X=X, y=y, cv=k, scoring='neg_mean_squared_error')
print('Lasso 0.1 %f' % abs(scores.mean()))

regression_model = linear_model.Lasso(alpha=0.5, copy_X=True, fit_intercept=True, max_iter=1000,
                                      normalize=False, positive=False, precompute=False, random_state=None,
                                      selection='cyclic', tol=0.0001, warm_start=False)
scores = cross_val_score(regression_model, X=X, y=y, cv=k, scoring='neg_mean_squared_error')
print('Lasso 0.5 %f' % abs(scores.mean()))

regression_model = linear_model.Lasso(alpha=1.0, copy_X=True, fit_intercept=True, max_iter=1000,
                                      normalize=False, positive=False, precompute=False, random_state=None,
                                      selection='cyclic', tol=0.0001, warm_start=False)
scores = cross_val_score(regression_model, X=X, y=y, cv=k, scoring='neg_mean_squared_error')
print('Lasso 1.0 %f' % abs(scores.mean()))

regression_model = linear_model.Ridge(alpha=0.5, copy_X=True, fit_intercept=True, max_iter=None,
                                      normalize=False, random_state=None, solver='auto', tol=0.001)
scores = cross_val_score(regression_model, X=X, y=y, cv=k, scoring='neg_mean_squared_error')
print('Ridge %f' % abs(scores.mean()))

regression_model = linear_model.ElasticNet(alpha=1.0, l1_ratio=1, fit_intercept=True, normalize=False, precompute=False,
                                           max_iter=1000, copy_X=True)
scores = cross_val_score(regression_model, X=X, y=y, cv=k, scoring='neg_mean_squared_error')
print('ElasticNet 1 %f' % abs(scores.mean()))

regression_model = linear_model.ElasticNet(alpha=10.0, l1_ratio=1, fit_intercept=True, normalize=False, precompute=False,
                                           max_iter=1000, copy_X=True)
scores = cross_val_score(regression_model, X=X, y=y, cv=k, scoring='neg_mean_squared_error')
print('ElasticNet 10 %f' % abs(scores.mean()))

regression_model = linear_model.ElasticNet(alpha=100.0, l1_ratio=1, fit_intercept=True, normalize=False, precompute=False,
                                           max_iter=1000, copy_X=True)
scores = cross_val_score(regression_model, X=X, y=y, cv=k, scoring='neg_mean_squared_error')
print('ElasticNet 100 %f' % abs(scores.mean()))
"""