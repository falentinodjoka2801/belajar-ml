from pandas import Series, DataFrame
from datetime import datetime
from math import floor
from re import search

_dictionary =   {
    'Name'  :   ['Falentino', 'Andrian Tarigan', 'Yusuf Mansyur Ginting', 'Rihanna Tarigan', 'Joshua Sembiring'],
    'City'  :   ['Medan', 'Berastagi', 'Jakarta', 'Bogor', 'Bandung']
}
_dataFrame  =   DataFrame(_dictionary)
print('Original DataFrame:')
print(_dataFrame)

_tanggalLahirSeries =   Series(['2000-01-28', '1999-03-06', '2000-01-19', '2000-10-10', '1998-10-28'])
_dataFrame['Birth'] =   _tanggalLahirSeries

_today  =   datetime.today()
def _calculateAge(dateOfBirth):
    _dateOfBirthObject  =   datetime.strptime(dateOfBirth, '%Y-%m-%d')

    _todayDate          =   f'{_today.year}-{_today.month}-{_today.day}';
    _dateNowObject      =   datetime.strptime(_todayDate, '%Y-%m-%d')
    _ageObject  =   _dateNowObject - _dateOfBirthObject
    _ageInDays  =   _ageObject.days
    _ageInYear  =   floor(_ageInDays / 365)

    _age        =   _ageInYear

    return _age

_dataFrame['Age']   =   _dataFrame['Birth'].apply(_calculateAge)
print(_dataFrame)

_dataFrame  =   _dataFrame[_dataFrame['Age'] >= 23]

def _orangKaroFunction(studentName):
    return f'{studentName} (Orang Karo)'
_dataFrame['Name']  =   _dataFrame['Name'].apply(_orangKaroFunction)
print(_dataFrame)