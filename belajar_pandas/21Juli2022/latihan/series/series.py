from pandas import Series

#series can be formed from : list and dictionary
_list   =   ['Falentino', 22, 'Medan']
_index  =   ['Name', 'Age', 'Address']
_seriesOfList   =   Series(_list, index=_index)
print(_seriesOfList)

_dictionary =   {'Name' : 'Falentino', 'Age' : 22, 'Address' : 'Medan'}
_seriesOfDictionary =   Series(_dictionary)
print(_seriesOfDictionary)