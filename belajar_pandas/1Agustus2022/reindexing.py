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
print(_dataFrame)

#reindexing rows
_dataFrame  =   _dataFrame.reindex(['BPSI', 'BSDM', 'BPAP', 'BKPH', 'BPAA'])
print(_dataFrame)

#reindexing columns
_dataFrame  =   _dataFrame.reindex(['Jajaran', 'Biro'], axis='columns')
print(_dataFrame)
