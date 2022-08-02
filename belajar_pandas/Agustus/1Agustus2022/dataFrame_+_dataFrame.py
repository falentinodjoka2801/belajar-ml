from pandas import DataFrame

_rawData    =   {
    'Biro'  :   [
        'Biro Pelaksana Administrasi Akademik', 'Biro Pengelola Sistem Informasi',
        'Biro Pengembangan Akreditasi dan Pemeringkatan', 'Biro Sumber Daya Manusia',
        'Biro Kerjasama, Protokoler dan Humas'
    ],
    'Jajaran'   :   ['R1', 'R3', 'R3', 'R3', 'R2']
}
_dataFrame  =   DataFrame(_rawData, index=['BPAA', 'BPSI', 'BPAP', 'BSDM', 'BKPH'])
# print(_dataFrame)

_dataFrame_Jajaran =   _dataFrame.reindex(['Jajaran'], axis='columns')
print(_dataFrame_Jajaran)

print('---')

_dataFrame_Biro =   _dataFrame.reindex(['Biro'], axis='columns')
print(_dataFrame_Biro)

print('---')

_dataFrame_BiroJajaran  =   _dataFrame_Biro + _dataFrame_Jajaran
print(_dataFrame_BiroJajaran)

print('---')

_dataFrame_BiroJajaran  =   _dataFrame_Biro.sum()
print(_dataFrame_BiroJajaran)