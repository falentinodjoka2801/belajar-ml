from numpy import random
from pandas import DataFrame

random.seed(100)

_data           =   random.randn(3, 5)
_rowIndex       =   ['A', 'B', 'C']
_columnIndex    =   ['Satu', 'Dua', 'Tiga', 'Empat', 'Lima']
_dataFrame  =   DataFrame(_data, index=_rowIndex, columns=_columnIndex)

print(_dataFrame)

_df_columnBiggerThanZero    =   _dataFrame[_dataFrame['Tiga']]
print(_df_columnBiggerThanZero)