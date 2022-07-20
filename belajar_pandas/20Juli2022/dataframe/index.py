from numpy import random
from pandas import DataFrame

try:
    random.seed(100)

    _data           =   random.randn(3, 5)
    _rowIndex       =   ['A', 'B', 'C']
    _columnIndex    =   ['Satu', 'Dua', 'Tiga', 'Empat', 'Lima']
    _dataFrame  =   DataFrame(_data, index=_rowIndex, columns=_columnIndex)

    # print(_dataFrame)
    # print(type(_dataFrame))
    # print(_dataFrame['Dua'])
    # print(type(_dataFrame['Dua']))
    # print(_dataFrame['Dua']['C'])
    # print(type(_dataFrame['Dua']['C']))

    print(_dataFrame)

    _enam               =   _dataFrame['Empat'] + _dataFrame['Lima']
    _dataFrame['Enam']  =   _enam

    print(_dataFrame)

    _dataFrame  =   _dataFrame.drop('A')
    
    print(_dataFrame)

    _dataFrame  =   _dataFrame.drop('Lima', axis=1)

    print(_dataFrame)
except KeyError as e:
    print(f'Key error => {e}')