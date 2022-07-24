from pandas import DataFrame, Series

_dictionary =   {
    'one'   :   Series([1, 2, 3]),
    'two'   :   Series([1, 2, 3, 4])
}
_dataFrame  =   DataFrame(_dictionary)
print(_dataFrame)