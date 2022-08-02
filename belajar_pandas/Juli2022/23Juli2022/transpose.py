from pandas import DataFrame, Series

_dictionary =   {
    'Age'   :   Series([25, 26, 25, 23, 30, 29, 23]),
    'Name'  :   Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
    'Rating'    :   Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.60, 3.80])
}
_dataFrame  =   DataFrame(_dictionary)
print(_dataFrame)

#transpose
_transposedDataFrame    =   _dataFrame.T
print(_transposedDataFrame)