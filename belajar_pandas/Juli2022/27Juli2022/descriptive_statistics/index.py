from pandas import DataFrame
import numpy
from data import dictionary as _dictionary

_dataFrame  =   DataFrame(_dictionary)
print(_dataFrame)

#karena baris itu vertikal, oleh karena itu hasil dari sum
#akan menjadikan tiap tiap kolom menjumlahkan atau menggabungkan data datanya
#misal pada dataframe di atas, Age akan menjadi 382
# _sum    =   _dataFrame.sum(axis=1, numeric_only=True)
# print(_sum)

# _mean   =   _dataFrame.mean(numeric_only=True)
# print(_mean)