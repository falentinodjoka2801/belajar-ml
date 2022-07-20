import pandas as pd

_list   =   [1, 2, 3, 4, 5]
_series =   pd.Series(_list, index=['a', 'b', 'c', 'd', 'e'])

print(_series[['a', 'b', 'e']])
print(_series[4] == _series['e'])