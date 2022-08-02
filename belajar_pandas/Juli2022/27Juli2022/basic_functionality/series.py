from pandas import Series

_dictionary =   {
    'Name'  :   'Falentino',
    'Age'   :   22,
    'Skills'    :   ['PHP', 'CodeIgniter', 'jQuery'],
    'City'      :   'Kota Medan',
    'Province'  :   'Sumatera Utara'
}
_series =   Series(_dictionary)
print(_series)

print(_series.shape)

# _axes   =   _series.axes
# print(_axes)

# _dtype  =   _series.dtype
# print(_dtype)

# _isEmpty    =   _series.empty
# print(_isEmpty)

# _ndim   =   _series.ndim
# print(_ndim)

# _size   =   _series.size
# print(_size)

# _values =   _series.values
# print(_values)

# _head   =   _series.head(3)
# print(_head)

# _tail   =   _series.tail(3)
# print(_tail)

# print(_series.size)