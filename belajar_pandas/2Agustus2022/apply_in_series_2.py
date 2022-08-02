from pandas import DataFrame, Series, read_csv
import numpy as np

_train  =   read_csv('http://bit.ly/kaggletrain')
print(_train.head())

_nameSeries:Series      =   _train['Name']
_train['NameLength']    =   _nameSeries.apply(len)

print(_train.loc[0:4, ['Name', 'NameLength']])

#Apply apply() with numpy function(s)
_fareSeries:Series  =   _train['Fare']
_train['FareCeil']  =   _fareSeries.apply(np.ceil)
print(_train.loc[0:4, ['Fare', 'FareCeil']])

def getElement(item, position):
    return item[position]

print(_nameSeries.str.split(',').apply(getElement, position=0))