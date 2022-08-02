from pandas import DataFrame, Series

_dictionary =   {
    'Age'   :   Series([25, 27, 34, 51, 19, 20, 22]),
    'Name'  :   Series(['Falentino', 'Andrian', 'Meidianta', 'Tarulina', 'Megawati', 'Siti', 'Yusuf']),
    'Rating'    :   Series([4.35, 7.10, 4.7, 4.9, 5.0, 3.5, 9.0])
}
_dataFrame  =   DataFrame(_dictionary)
print(_dataFrame)

#axes
_axes   =   _dataFrame.axes
print(_axes)

#size
_size   =   _dataFrame.size
print(_size)

#shape
_shape  =   _dataFrame.shape
print(_shape)

#lainnya
_numbersOfRows, _numbersOfColumns   =   _shape
_comparisonOfSizeAndShape   =   (_numbersOfRows * _numbersOfColumns) == _size
print(_comparisonOfSizeAndShape)