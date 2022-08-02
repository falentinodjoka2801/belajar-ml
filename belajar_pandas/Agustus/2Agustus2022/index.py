import pandas as pd

_train  =   pd.read_csv('http://bit.ly/kaggletrain')
print(_train.head())

_sexSeries:pd.Series    =   _train['Sex']
_train['SexNum']        =   _sexSeries.map({'female':0, 'male':1})

print(_train.loc[0:4, ['Sex', 'SexNum']])