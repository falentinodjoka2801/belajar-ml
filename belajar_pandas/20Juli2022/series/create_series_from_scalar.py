#create a series from a scalar, you have to serve/provide the index, it's must
#your scalar value will be repeated as long as your index length
#we know the index is a list, so if your index list's length is 3 and your scalar value is 'Tino', then your series will be 
#0 Tino
#1 Tino
#2 Tino

#to prove it, lets see the example below

import pandas as pd

_scalarValue    =   'Tino'
_index      =   ['Juara 1', 'Juara 3 Harapan']
_series     =   pd.Series(_scalarValue, index=_index)

print(_series)

#the program above is right!