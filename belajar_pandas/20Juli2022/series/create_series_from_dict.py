import pandas as pd
from datetime import datetime
from math import floor

_dict   =   {
    'name'          :   'Falentino',
    'address'       :   'Jl. Medan Raya',
    'dateOfBirth'   :   '2000-01-28',
    'city'          :   'Kota Medan',
    'province'      :   'Sumatera Utara'
}

_series =   pd.Series(_dict)

# _indexOfSeries            =   ['name', 'name']
# _seriesWithCustomIndex    =   pd.Series(_dict, index=_indexOfSeries)

# print(_series)
# print(_seriesWithCustomIndex)

_dateOfBirth            =   _series['dateOfBirth']
_dateOfBirth_object     =   datetime.strptime(_dateOfBirth, '%Y-%m-%d')

_today                  =   datetime.today()
_dateNow_object         =   datetime.strptime(str(_today.date()), '%Y-%m-%d')

_ageObject  =   _dateNow_object - _dateOfBirth_object
_ageInDays  =   _ageObject.days
_ageInYear  =   floor(_ageInDays / 365)

print(_series)

_series['age']  =   f'{_ageInYear} year(s) old'

print(_series)