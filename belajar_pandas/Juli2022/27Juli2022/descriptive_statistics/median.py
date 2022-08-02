from data import dictionary

from pandas import DataFrame

_dataFrame  =   DataFrame(dictionary)
print(_dataFrame)

_median     =   _dataFrame.median(numeric_only=True)
print(_median)