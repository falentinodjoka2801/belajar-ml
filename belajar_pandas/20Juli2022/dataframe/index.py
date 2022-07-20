from numpy import random
from pandas import DataFrame

try:
    _data           =   random.randn(3, 5)
    _rowIndex       =   ['A', 'B', 'C']
    _columnIndex    =   ['Satu', 'Dua', 'Tiga', 'Empat', 'Lima']
    _dataFrame  =   DataFrame(_data, index=_rowIndex, columns=_columnIndex)

    print(_dataFrame)
    print(_dataFrame['Dua']['C'])
except KeyError as e:
    print(f'Key error => {e}')