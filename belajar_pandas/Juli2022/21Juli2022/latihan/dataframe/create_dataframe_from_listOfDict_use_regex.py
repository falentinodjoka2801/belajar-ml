from pandas import DataFrame
from re import search

#list of dictionary
_rawData    =   [
    {'City':'New Delhi (D)', 'Events':'Poetry', 'Cost':20},
    {'City':'New York (Y)', 'Events':'Music', 'Cost':30},
    {'City':'New Delhi (Delhi)', 'Events':'Circus', 'Cost':50},
    {'City':'New York (York)', 'Events':'Poetry', 'Cost':40},
    {'City':'new York (D)', 'Events':'Music', 'Cost':10}
]
_index      =   ['2018-02', '2018-04', '2018-06', '2018-08', '2018-10']
_dataFrame  =   DataFrame(_rawData, index=_index)
print('Raw Data\n')
print(_dataFrame)

_dataFrame  =   _dataFrame.replace(regex=True, to_replace='[nN]ew', value='New_')
print('Replace [nN]ew with New_')
print(_dataFrame)

def _removeWordsInBracket(cityName):
    if(search('\(.*', cityName)):
        _position   =   search('\(.*', cityName).start()
        return cityName[:_position]
    else:
        return cityName

def _changeCostTypeToDouble(cost):
    return float(cost)

_dataFrame['City']  =   _dataFrame['City'].apply(_removeWordsInBracket)
_dataFrame['Cost']  =   _dataFrame['Cost'].apply(_changeCostTypeToDouble)
print('Delete a word in a pair of bracket\n')
print(_dataFrame)