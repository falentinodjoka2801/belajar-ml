from pandas import DataFrame

_dictOfList     =   {
    'Name'  :   ['Peter', 'Riff', 'John', 'Michael', 'Shelli'],
    'Age'   :   [18, 15, 17, 18, 17],
    'Score' :   [7, 6, 8, 7, 5]
}
_dataFrame  =   DataFrame(_dictOfList)

print(_dataFrame)