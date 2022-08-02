from numpy import random
from pandas import DataFrame, Series

_array  =   random.rand(5, 4)
print(_array)

_dataFrame          =   DataFrame(_array, columns=['Indonesia', 'Matematika', 'Inggris', 'Kejuruan'])
_dataFrame['Siswa'] =   Series(['Falentino', 'Andrian', 'Yudha', 'Abdi', 'Yuni'])
_dataFrame          =   _dataFrame.reindex(['Siswa', 'Indonesia', 'Matematika', 'Inggris', 'Kejuruan'], axis=1)

print(_dataFrame)

_dataFrame  =   _dataFrame.set_index('Siswa')
print(_dataFrame)