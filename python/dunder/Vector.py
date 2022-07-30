class Vector:
    def __init__(self, xValue, yValue):
        self.x  =   xValue
        self.y  =   yValue

        return True

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'(x, y) => ({self.x}, {self.y})'

    def __call__(self):
        print('Hello, I was called!')

    def __eq__(self, other):
        return type(self) == other