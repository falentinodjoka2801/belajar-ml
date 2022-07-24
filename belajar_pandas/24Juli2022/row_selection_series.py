from pandas import DataFrame, Series

_dictionary =   {
    'one'   :   Series([1, 2, 3], index=['a', 'b', 'c']),
    'two'   :   Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}
_dataFrame  =   DataFrame(_dictionary)
print(_dataFrame)

print('---')
print('Baris B')

_barisB =   _dataFrame.loc['b']
print(_barisB)

print('Series of Baris B')
_seriesOfBarisB =   Series([2.0, 2.0], index=['one', 'two'], name='b')
print(_seriesOfBarisB)

print('---')

_kolomTwo   =   _dataFrame['two']
print(_kolomTwo)

print('---')

print(type(_dataFrame))
print(type(_barisB))
print(type(_kolomTwo))