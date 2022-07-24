from pandas import Series

_series =   Series(['Falentino', 'Andrian', 'Yusuf'], index=['R1', 'R2', 'R3'])
print(_series)

_series['R1']   =   'Tino'
print(_series)