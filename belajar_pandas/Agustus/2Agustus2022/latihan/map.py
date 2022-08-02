from pandas import Series, DataFrame, read_csv

_train  =   read_csv('http://bit.ly/kaggletrain')
print(_train)

_train['SexCode']   =   _train['Sex'].map({'female':'F', 'male':'M'})
_train  =   _train.reindex(['PassengerId', 'Name', 'Sex', 'SexCode', 'Age'], axis=1)

print(_train)