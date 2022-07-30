from pandas import DataFrame
import numpy as np

_rawData    =   np.random.randn(5, 3)
print('Raw Data')
print(_rawData)

_dataFrame  =   DataFrame(_rawData, columns=['Col1', 'Col2', 'Col3'])
print('DataFrame')
print(_dataFrame)

_dataFrame.apply(np.mean)

print('After apply() is applied')
print(_dataFrame)