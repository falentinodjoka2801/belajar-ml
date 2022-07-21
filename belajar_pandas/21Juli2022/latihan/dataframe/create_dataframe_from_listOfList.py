from pandas import DataFrame

_listOfList     =   [
    ['Peter', 18, 7],
    ['Riff', 15, 6],
    ['John', 17, 8],
    ['Michael', 18, 7],
    ['Shelli', 17, 5]
]
_columns    =   ['Name', 'Age', 'Score']
_dataFrame  =   DataFrame(_listOfList, columns=_columns)

print(_dataFrame)