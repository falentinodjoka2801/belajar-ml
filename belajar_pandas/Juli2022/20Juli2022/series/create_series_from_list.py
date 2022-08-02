import pandas as pd

try:
    _list   =   [28, 4, 2, 18, 4, 90]

    _series                 =   pd.Series(_list)
    _seriesWithCustomIndex  =   pd.Series(_list, index=['Tino', 'Andri', 'Anggi', 'Fery', 'Medianta', 'Sonia'])

    print(_series)
    print(_seriesWithCustomIndex)
except ValueError as e:
    print(e)