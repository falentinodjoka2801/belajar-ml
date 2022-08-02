from pandas import DataFrame, Series, read_csv

_train  =   read_csv('http://bit.ly/kaggletrain')
print(_train)

_train['PassengerId']   =   _train['PassengerId'].apply(float)
print(_train)

# def _getLastName(fullName, index):
#     _lastName       =   fullName[index]
#     return _lastName

# _nameSeries:Series  =   _train['Name']
# _train['LastName']  =   _nameSeries.str.split(',').apply(_getLastName, index=0)

# print(_train)

# _train  =   _train.reindex(['PassengerId', 'Survived', 'Pclass', 'Name', 'LastName', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'], axis=1)
# print(_train)