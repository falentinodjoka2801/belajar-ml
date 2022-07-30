from Vector import Vector as v

try:
    _vector1    =   v(10, 60)
    _vector2    =   v(20, 70)

    print(_vector1 == _vector2) 
    #object sama dengan class karena object adalah bentuk nyata dari class

    print(_vector1 == type(_vector2))
except:
    print('Terjadi Kesalahan')