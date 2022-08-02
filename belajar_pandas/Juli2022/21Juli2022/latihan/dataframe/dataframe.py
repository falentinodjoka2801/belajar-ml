from pandas import DataFrame

# _data   =   {
#     'Category'  :   ['Array', 'Stack', 'Queue'],
#     'Student1'  :   [20, 21, 19],
#     'Student2'  :   [15, 20, 14]
# }

# _dataFrame  =   DataFrame(_data)
# print(_dataFrame)

# _dataFrameTranspose     =   _dataFrame.transpose()
# print(_dataFrameTranspose)

#create dataframe from dictionary
_dictionary  =   {
    'Agama'     :   [25.0, 50.0, 25.5, 40.1, 30.0],
    'Penjas'    :   [90.0, 20.1, 10.0, 57.6, 30.0],
    'Matematika'    :   [27.23, 71.3, 25.3, 61.5, 10.5],
    'Produktif'     :   [93.5, 75.7, 76.3, 60.0, 100.0]
}

_namaSiswa  =   ['Falentino', 'Andrian', 'Herianto', 'Sutomo', 'Ferdinand']
_dataFrame  =   DataFrame(_dictionary, index=_namaSiswa)
print(_dataFrame)

_transpose  =   _dataFrame.transpose()
print(_transpose)