from pandas import Series, DataFrame, read_csv

_train  =   read_csv('http://bit.ly/kaggletrain')
print(_train)

#last name
def _lastNameGenerator(fullName, indexPosition):
    _lastName   =   fullName[indexPosition]
    return _lastName

_train['LastName']  =   _train['Name'].str.split(',').apply(_lastNameGenerator, indexPosition=0)
print(_train.loc[:, ['Name', 'LastName']])

#name length
_train['NameLength']    =   _train['Name'].apply(len)
print(_train.loc[:, ['Name', 'NameLength', 'LastName']])