from pandas import DataFrame
from re import search

_rawData    =   {
    'City'      :   ['New Delhi (D)', 'New York (Y)', 'New Delhi (Delhi)', 'New York (York)', 'new york'],
    'Events'    :   ['Poetry', 'Music', 'Circus', 'Poetry', 'Music'],
    'Cost'      :   [20, 30, 50, 40, 10]
}
_index      =   ['2018-02', '2018-04', '2018-06', '2018-08', '2018-10']
_dataFrame  =   DataFrame(_rawData, index=_index)
print('Raw DataFrame\n')
print(_dataFrame)

print('---')

_dataFrame  =   _dataFrame.replace(regex=True, to_replace='[nN]ew', value='New_')
print('Replace [nN]ew with New_')
print(_dataFrame)

print('---')

def _removerFunction(cityName):
    if(search('\(.*', cityName)):
        _position   =   search('\(.*', cityName).start()
        return cityName[:_position]
    else:
        return cityName

_dataFrame['City']  =   _dataFrame['City'].apply(_removerFunction)
print('Remove the word(s) in a pair of bracket')
print(_dataFrame)