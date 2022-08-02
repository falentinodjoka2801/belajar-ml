from pandas import Series

_data       =   [1, 2, 3, 4, 5]
_index      =   ['A', 'I', 'U', 'E', '0']
_series     =   Series(_data, index=_index)

print(_series)
print(_series[3])
print(_series['E'])