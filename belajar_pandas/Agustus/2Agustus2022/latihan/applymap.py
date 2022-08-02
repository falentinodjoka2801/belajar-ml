from pandas import DataFrame, Series, read_csv
import numpy as np

_train  =   read_csv('http://bit.ly/kaggletrain')
print(_train)

_train_AgeFare   =   _train.reindex(['Age', 'Fare'], axis=1)
print(_train_AgeFare)

_train_AgeFare_int  =   _train_AgeFare.applymap(str)
print(_train_AgeFare_int)