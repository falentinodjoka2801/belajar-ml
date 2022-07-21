from pandas import DataFrame
import re

# _dict   =   {
#     'City'      :   ['New York', 'Parague', 'new Delhi', 'Venice', 'new Orleans'],
#     'Events'    :   ['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
#     'Cost'      :   [10000, 5000, 15000, 2000, 12000]
# }
# _index      =   ['2018-02', '2018-04', '2018-06', '2018-08', '2018-10']
# _dataFrame  =   DataFrame(_dict, index=_index)
# print(_dataFrame)

# _dataFrame  =   _dataFrame.replace(regex=True, to_replace='[nN]ew', value='New_')
# print(_dataFrame)

_dict   =   {
    'City'      :   ['New York (City)', 'Parague', 'new Delhi (Delhi)', 'Venice', 'new Orleans'],
    'Events'    :   ['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
    'Cost'      :   [10000, 5000, 15000, 2000, 12000]
}
_index      =   ['2018-02', '2018-04', '2018-06', '2018-08', '2018-10']
_dataFrame  =   DataFrame(_dict, index=_index)

def cleanNames(cityName):
    if(re.search('\(.*', cityName)):
        _position   =   re.search('\(.*', cityName).start()
        return cityName[:_position]
    else:
        return cityName

_dataFrame  =   _dataFrame['City'].apply(cleanNames)
print(_dataFrame)