#apply is a method in a series that applies its method to every item in a series

from pandas import Series, DataFrame

# _biroR3 =   Series(['BPSI', 'BSDM', 'BPAP'])
# print(_biroR3)

# def _keterangan(biro):
#     return f'{biro} di jajaran R3'

# _biroR3 =   _biroR3.apply(_keterangan)
# print(_biroR3)

_rawData    =   {
    'biroNickName'  :   ['BPSI', 'BSDM', 'BPAP'],
    'biroName'      :   ['Biro Pengelola Sistem Informasi', 'Biro Sumber Daya Manusia', 'Biro Pengembangan Akreditasi dan Pemeringkatan'],
    'jajaran'       :   ['R3', 'R3', 'R3']
}
_dataFrame  =   DataFrame(_rawData)

print('Original DataFrame')
print(_dataFrame)

_biroNameSeries:Series          =   _dataFrame['biroName']
_dataFrame['biroNameLength']    =   _biroNameSeries.apply(len)

print('New Column biroNameLength')
print(_dataFrame.loc[:, ['biroName', 'biroNameLength']])

_dataFrame.drop('biroNameLength', axis=1, inplace=True)

def _characterLengthGenerator(biroName):
    return f'{biroName} {len(biroName)} character(s)'

_dataFrame['biroName'] =   _biroNameSeries.apply(_characterLengthGenerator)

print('Biro Name Length in biroName column')
print(_dataFrame)