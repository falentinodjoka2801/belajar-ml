from pandas import DataFrame
from numpy import random

random.seed(100)

_data           =   random.randn(5, 3)
_rowIndex       =   ['A', 'B', 'C', 'D', 'E']
_columnIndex    =   ['A', 'B', 'C']
_dataFrame  =   DataFrame(_data, index=_rowIndex, columns=_columnIndex)

_column_D       =   _dataFrame['A'] + _dataFrame['B'] + _dataFrame['C']
_dataFrame['D'] =   _column_D

print(_dataFrame)

_dataFrame  =   _dataFrame.drop('C', axis=1)
print(_dataFrame)

_dataFrame  =   _dataFrame[_dataFrame['D'] >= 1]
print(_dataFrame)

_dataFrame  =   _dataFrame <= 0
print(_dataFrame)