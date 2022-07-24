from pandas import DataFrame, Series

_listOfDictionary   =   [
    {'name':'Sujeet', 'age':10},
    {'name':'Sameer', 'age':11},
    {'name':'Sumit', 'age':12}
]
_dataFrame  =   DataFrame(_listOfDictionary)

print('Original DataFrame:')
print(_dataFrame)

for _index, seriesOfRows in _dataFrame.iterrows():
    print(f'{seriesOfRows["name"]} {seriesOfRows["age"]}')