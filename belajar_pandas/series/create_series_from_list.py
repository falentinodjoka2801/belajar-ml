import pandas as pd

try:
    _list   =   [2, 3, 5, 7, 11] #bilangan prima
    _series =   pd.Series(_list)

    _seriesWithIndex    =   pd.Series(_list, index=['Ke-0', 'Ke-1', 'Ke-2', 'Ke-3', 'Ke-4', 'Ke-5'])

    print(_series)
    print(_seriesWithIndex)
except ValueError as e:
    print('Terjadi Kesalahan')
    print(e)