from Vector import Vector

_vector1    =   Vector(10, 20) + Vector(15, 30)
_vector2    =   Vector(50, 60)
_vector3    =   _vector1 + _vector2

print(_vector3.x)
print(_vector3.y)
print(_vector3)

_vector3()