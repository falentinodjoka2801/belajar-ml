import pandas as pd

_data   =   {
    'name'      :   ['Falentino', 'Andrian', 'Risky'],
    'date'      :   ['2000-01-28', '1999-03-06', '1999-09-09'],
    'shares'    :   [100, 50, 90],
    'price'     :   [195.5, 200.0, 500.0]
}

_dataFrame  =   pd.DataFrame(_data, index=['tino', 'andri', 'risky'])
_dataFrame['jurusan']   =   'Unknown'

print(_dataFrame)
# print(_dataFrame['name'])

del _dataFrame['jurusan']

print(_dataFrame)

# _dataFrame  =   _dataFrame.set_index('name')

# print(_dataFrame)