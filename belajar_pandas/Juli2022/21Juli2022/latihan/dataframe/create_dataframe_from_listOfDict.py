from pandas import DataFrame

_listOfDict     =   [
    {'Geeks' : 'DataFrame', 'for' : 'using', 'geeks' : 'list'},
    {'Geeks' : 10, 'for' : 20, 'geeks' : 30}
]

_dataFrame  =   DataFrame(_listOfDict, index=['Baris 1', 'Baris 2'])
print(_dataFrame)

_listOfDict =   [
    {'Geeks' : 'dataframe', 'For' : 'using', 'geeks' : 'list', 'Portal' : 10000},
    {'Geeks' : 10, 'For' : 20, 'geeks' : 30}
]
_dataFrame  =   DataFrame(_listOfDict)
print(_dataFrame)