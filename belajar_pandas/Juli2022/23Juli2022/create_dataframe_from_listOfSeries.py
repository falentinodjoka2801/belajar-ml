from pandas import DataFrame, Series

_listOfSeries   =   [
    Series([1, 2, 3, 4, 5]),
    Series([6, 7, 8, 9, 10])
]
_dataFrame  =   DataFrame(_listOfSeries)
print(_dataFrame)