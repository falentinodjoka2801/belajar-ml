from pandas import DataFrame, Series

# _data   =   [
#     [25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46],
#     ['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack', 'Lee', 'David', 'Gasper', 'Betina', 'Andres'],
#     [4.23, 3.24, 3.98, 2.56, 3.20, 4.60, 3.80, 3.78, 2.98, 4.80, 4.10, 3.65]
# ]
# _dataFrame  =   DataFrame(_data, index=['Age', 'Name', 'Rating'])

# print(_dataFrame.transpose())

# _data   =   [
#     {'Age' : 25, 'Name' : 'Tom', 'Rating' : 4.24},
#     {'Age' : 26, 'Name' : 'James', 'Rating' : 3.24},
#     {'Age' : 25, 'Name' : 'Ricky', 'Rating' : 3.98},
#     {'Age' : 23, 'Name' : 'Vin', 'Rating' : 2.56},
#     {'Age' : 30, 'Name' : 'Steve', 'Rating' : 3.20},
#     {'Age' : 29, 'Name' : 'Smith', 'Rating' : 4.60},
#     {'Age' : 23, 'Name' : 'Jack', 'Rating' : 3.80},
#     {'Age' : 34, 'Name' : 'Lee', 'Rating' : 3.78},
#     {'Age' : 40, 'Name' : 'David', 'Rating' : 2.98},
#     {'Age' : 30, 'Name' : 'Gasper', 'Rating' : 4.80},
#     {'Age' : 51, 'Name' : 'Betina', 'Rating' : 4.10},
#     {'Age' : 46, 'Name' : 'Andres', 'Rating' : 3.65},
# ]
# _dataFrame  =   DataFrame(_data)
# print(_dataFrame)

# _data_series   =   {
#     'Age'       :   Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
#     'Name'      :   Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack', 'Lee', 'David', 'Gasper', 'Betina', 'Andres']),
#     'Rating'    :   Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.60, 3.80, 3.78, 2.98, 4.80, 4.10, 3.65])
# }
# _dataFrame  =   DataFrame(_data_series)
# _dataFrame_series  =   DataFrame(_data_series)
# print(_dataFrame_series)

_data_list   =   {
    'Age'       :   [25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46],
    'Name'      :   ['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack', 'Lee', 'David', 'Gasper', 'Betina', 'Andres'],
    'Rating'    :   [4.23, 3.24, 3.98, 2.56, 3.20, 4.60, 3.80, 3.78, 2.98, 4.80, 4.10, 3.65]
}
_dataFrame  =   DataFrame(_data_list)
# _dataFrame_list     =   DataFrame(_data_list)
# # print(_dataFrame_list)

# _age_dataFrameSeries    =   _dataFrame_series['Age']
# _age_dataFrameList      =   _dataFrame_list['Age']
# print(type(_age_dataFrameList))
# print(type(_age_dataFrameSeries))

_rating:Series      =   _dataFrame['Rating']
_meanOfRating       =   _rating.mean()
print(_meanOfRating)

_meanOfDataFrame    =   _dataFrame.mean(numeric_only=True)
print(_meanOfDataFrame['Rating'])