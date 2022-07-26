from data import dictionary

from pandas import DataFrame

_dataFrame   =   DataFrame(dictionary)
print(_dataFrame)

_mean   =   _dataFrame.mean(numeric_only=True)
print(_mean)