from pandas import Series, DataFrame, read_csv

_train  =   read_csv('http://bit.ly/kaggletrain')
print(_train)

print(_train.loc[0:4, ['Age', 'Fare']].apply(max, axis=1))