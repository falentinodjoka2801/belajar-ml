from pandas import Series, DataFrame

_series_name        =   Series(['Falentino', 'Andrian', 'Anggi'])
_series_religion    =   Series(['Islam', 'Katolik', 'Islam'])

_rawData    =   {
    'Name'      :   _series_name,
    'Religion'  :   _series_religion
}
_dataFrame  =   DataFrame(_rawData)
print('Raw DataFrame')
print(_dataFrame)

_religionSeriesFromDataFrame:Series     =   _dataFrame.Religion
_dataFrame['ReligionMap']               =   _religionSeriesFromDataFrame.map({'Islam' : 'I', 'Katolik' : 'Ka'})
print('DataFrame with ReligionMap Column')
print(_dataFrame.loc[1:3, ['Religion', 'ReligionMap']])