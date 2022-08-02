from pandas import DataFrame, Series, concat

_rawData    =   {
    'id'    :   [100, 101, 102],
    'color' :   ['red', 'blue', 'red']
}
_dataFrame  =   DataFrame(_rawData, index=['a', 'b', 'c'])
print(_dataFrame)

_series     =   Series(['square', 'round'], index=['a', 'c'], name='shape')

_dataFrame  =   concat([_dataFrame, _series], axis=1)
print(_dataFrame)

_series     =   Series(['Tino', 'Andrian', 'Yudha'], index=['a', 'b', 'c'])
_dataFrame['person']    =   _series

print(_dataFrame)