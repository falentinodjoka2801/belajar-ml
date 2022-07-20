import pandas as pd

_dict   =   {
    'name'      :   'Falentino',
    'address'   :   'Jl. Medan',
    'age'   :   22,
    'point' :   95.75
}

_series     =   pd.Series(_dict)
_seriesWithCustomIndex  =   pd.Series(_dict, index=['name', 'Alamat', 'Umur', 'Poin'])
print(_series)
print(_seriesWithCustomIndex)
print(_seriesWithCustomIndex['name'])