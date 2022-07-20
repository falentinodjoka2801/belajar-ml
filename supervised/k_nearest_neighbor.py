from mysql import connector
from math import sqrt

_rumah      =   input('Nama Rumah\n')
_latitude   =   float(input('Latitude\n'))
_longitude  =   float(input('Longitude\n'))

_connection     =   connector.connect(database='belajar_ml', host='localhost', user='root', password='')
_cursor         =   _connection.cursor()

_cursor.execute('select * from rumah')
_getListRumah   =   _cursor.fetchall()

_cursor.close()
_connection.close()

if len(_getListRumah) >= 1:
    _distanceFromRumah  =   {}
    for _dataRow in _getListRumah:
        _id, _namaRumah, _lat, _long, _lokasi   =   _dataRow
        _distanceKuadrat   =   (_lat - _latitude) ** 2 + (_long - _longitude) ** 2
        _distance   =   sqrt(_distanceKuadrat)

        _distanceFromRumah[_namaRumah]  =   _distance

    print(_distanceFromRumah)

    

