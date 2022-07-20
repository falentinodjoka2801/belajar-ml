from pandas import DataFrame

#empty dataframe
_dataFrame  =   DataFrame()
print(_dataFrame)

#create a dataframe from list
#single list

_singleList     =   [1, 2, 3, 5, 7, 11] #bilangan prima
_dataFrame      =   DataFrame(_singleList)
print(_dataFrame)

#List of List
_listOfList =   [
    ['Alex', 10], ['Bob', 12], ['Clarke', 13]
]
_dataFrame  =   DataFrame(_listOfList, columns=['Name', 'Age'])
print(_dataFrame)