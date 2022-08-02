from pandas import DataFrame, Series
from re import search

#dictionary of series
_rangking   =   ['Rangking 1', 'Rangking 2', 'Rangking 3']
_siswaBerprestasiKelas12 =   {
    'TSM'   :   Series(['Daud Pranatha Simbolon', 'Benni Tarigan', 'Sadawari Laia'], index=_rangking),
    'AP'    :   Series(['Fatmawati Kaban', 'Yolanda Silaban', 'Anita Tarigan'], index=_rangking),
    'MM'    :   Series(['Andrian Tarigan', 'Jhikry Maulana', 'Adilta Perangin - Angin'], index=_rangking),
    'RPL'   :   Series(['Meidianta Sembiring', 'Siti Khadijah', 'Tarulina Sihotang'], index=_rangking)
}
_dataFrame  =   DataFrame(_siswaBerprestasiKelas12)
print(_dataFrame)

print('----------------')

_rangking3 : Series  =   _dataFrame.loc['Rangking 3']
print('Rangking 3')
print(_rangking3)

def _tariganFilter(namaSiswa):
    _isMergaBeruTarigan =   search('[tT]arigan', namaSiswa)

    _returnedNamaSiswa  =   '-'
    if(_isMergaBeruTarigan):
        _returnedNamaSiswa  =   namaSiswa

    return _returnedNamaSiswa  

_rangking3MergaBeruTarigan   =   _rangking3.apply(_tariganFilter)
print('Rangking 3 Merga/Beru Tarigan')
print(_rangking3MergaBeruTarigan)