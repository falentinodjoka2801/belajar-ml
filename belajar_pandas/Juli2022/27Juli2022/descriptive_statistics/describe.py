from pandas import DataFrame
from data import dictionary

_dataFrame  =   DataFrame(dictionary)
print(_dataFrame)

_desc   =   _dataFrame.describe()
print(_desc)