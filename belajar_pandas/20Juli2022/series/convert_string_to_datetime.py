from datetime import datetime

_dateString     =   '27/10/20'
_dataObject     =   datetime.strptime(_dateString, '%d/%m/%y')

_dateOfBirth        =   '2000-01-28'
_dataOfBirth_object =   datetime.strptime(_dateOfBirth, '%Y-%m-%d')

print(_dataObject.day)
print(_dataOfBirth_object)

#ubah string ke waktu PHP
#$waktu     =   date('Y-m-d', strtotime($tanggalYangMauDiformat))