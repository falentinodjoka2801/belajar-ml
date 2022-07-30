class Students:
    def __init__(self, idNo, grade):
        self.idNo   =   idNo
        self.grade  =   grade
    
    def __new__(otherClass, idNo, grade):
        print('Creating Instance')
        _instance   =   super(Students, otherClass).__new__(otherClass)
        if(5 <= grade <= 10):
            return _instance
        else:
            return None

    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__})'

_stud1  =   Students(1, 7)
print(_stud1)

_stud2  =   Students(2, 12)
print(_stud2)