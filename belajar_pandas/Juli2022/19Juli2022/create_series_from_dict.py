import pandas as pd

_dict   =   {
    'name'  :   'Falentino',
    'age'   :   22
}

_series     =   pd.Series(_dict)
_series2    =   pd.Series(_dict, index=['id', 'name', 'age', 'address'])

print(_series)
print(_series2)