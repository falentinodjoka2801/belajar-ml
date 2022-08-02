from pandas import DataFrame

_dictionary =   {
    'Name'  :   ['Falentino', 'Andrian', 'Sophia', 'Gery'],
    'Age'   :   [22, 23, 19, 26],
    'City'  :   ['Medan', 'Kabanjahe', 'Binjai', 'Medan']
}
_index      =   ['Tino', 'Ian', 'Phia', 'Ery']
_dataFrame  =   DataFrame(_dictionary, index=_index)
# print(_dataFrame)

_transpose  =   _dataFrame.T
# print(_transpose)

# print(_dataFrame.axes)
# print(_transpose.axes)

# _ndim   =   _dataFrame.ndim
# print(_ndim)

# _size   =   _dataFrame.size
# print(_size)

_ordo_dataFrame     =   _dataFrame.shape
_ordo_transpose     =   _transpose.shape
print(_ordo_dataFrame)
print(_ordo_transpose)