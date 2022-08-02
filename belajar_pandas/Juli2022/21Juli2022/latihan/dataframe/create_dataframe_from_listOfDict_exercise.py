from pandas import DataFrame

_listOfDict =   [
    {'Geeks' : 'dataframe', 'For' : 'using', 'geeks' : 'list'},
    {'Geeks' : 10, 'For' : 20, 'geeks' : 30}    
]

_index      =   ['Baris1', 'Baris2']
_dataFrame  =   DataFrame(_listOfDict, index=_index)

print(_dataFrame)