import pandas as pd
from mysql import connector

_connection     =   connector.connect(database='belajar_ml', host='localhost', user='root', password='')
_cursor         =   _connection.cursor()

_getListRumah   =   _cursor.execute('select * from rumah')
_listRumah      =   _cursor.fetchall()

#converting tuple to Series
_i  =   0
for _rumah in _listRumah:
    if(_i == 0):
        #without custom index name
        _seriesOfTuple  =   pd.Series(_rumah)
        print(_seriesOfTuple)
        
        #with custom index name
        _seriesOfTupleWithCustomIndex  =   pd.Series(_rumah, index=['id', 'rumah', 'lat', 'long', 'lokasi'])
        print(_seriesOfTupleWithCustomIndex)

        #dictionary
        _id, _rumah, _latitude, _longitude, _lokasi     =   _rumah
        _rumahDict      =   {'id' : _id, 'rumah' : _rumah, 'latitude' : _latitude, 'longitude' : _longitude, 'lokasi' : _lokasi}
        _seriesOfDict   =   pd.Series(_rumahDict)
        print(_seriesOfDict)

        print(_seriesOfTupleWithCustomIndex['rumah'])
    else:
        break

    _i += 1

_cursor.close()
_connection.close()