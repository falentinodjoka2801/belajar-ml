from pandas import DataFrame
from numpy import random

# def adder(element1, element2):
#     return element1 + element2

# _rawData    =   random.randn(5, 3)
# _dataFrame  =   DataFrame(_rawData, columns=['col1', 'col2', 'col3'])

# print(_dataFrame)

# _dataFrame.pipe(adder, 2)

# print(_dataFrame)

def _changeAge(itemData):
    itemData['age'] =   [22, 23, 24]
    return itemData

_dictionary =   {
    'name'  :   ['Falentino', 'Andrian', 'John'],
    'age'   :   [23, 24, 25]
}
_dataFrame  =   DataFrame(_dictionary)

print(_dataFrame)

_dataFrame.pipe(_changeAge)

print(_dataFrame)
