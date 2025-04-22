from typing import Tuple, Union
import math

numberType = Union[int, float]

class Vector:
    _val: Tuple[numberType, numberType, numberType] = None

    def __init__(self, x, y, z):
        self._val = (x,y,z)

    @property
    def x(self):
        return self._val[0]

    @property
    def y(self):
        return self._val[1]

    @property
    def z(self):
        return self._val[2]


    def dot(self, other: "Vector") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: "Vector") -> "Vector":
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def project_onto(self, other: "Vector") -> "Vector":
        scale = self.dot(other) / other.dot(other)
        return Vector(other.x * scale, other.y * scale, other.z * scale)

    def magnitude(self) -> float:
        return math.sqrt(self.dot(self))

    def normalize(self) -> "Vector":
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0, 0)
        return Vector(self.x / mag, self.y / mag, self.z / mag)

    def clamp_to_basis(self) -> "Vector":
        x, y, z = self.x, self.y, self.z
        a, b, c = abs(x), abs(y), abs(z)
        
        if b >= a and b >= c:
            max_idx = 1
        elif c >= a and c >= b:
            max_idx = 2
        else:
            max_idx = 0


        if max([a,b,c]) == 0:
            return Vector(0, 0, 0)

        sign = lambda v: 1 if v > 0 else -1
        if max_idx == 0:
            return Vector(sign(x), 0, 0)
        elif max_idx == 1:
            return Vector(0, sign(y), 0)
        else:
            return Vector(0, 0, sign(z))


    def __str__(self) -> str:
        return f"<{self.x:.2f}, {self.y:.2f}, {self.z:.2f}>"

    def __repr__(self):
        return f"Vector({self.x.__repr__()}, {self.y.__repr__()}, {self.z.__repr__()})"

    def __add__(self, other):
        if isinstance(other, numberType):
            return Vector(
                self.x + other,
                self.y + other,
                self.z + other,
            )
        
        if not isinstance(other, type(self)):
            raise TypeError
        
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __sub__(self, other):
        if isinstance(other, numberType):
            return Vector(
                self.x - other,
                self.y - other,
                self.z - other,
            )
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        if isinstance(other, numberType):
            return Vector(
                other - self.x,
                other - self.y,
                other - self.z,
            )
        return other.__sub__(self)

    def __abs__(self):
        return self.magnitude()

    def __mul__(self, other):
        if isinstance(other, numberType):
            return Vector(
                self.x * other,
                self.y * other,
                self.z * other,
            )
        return self.dot(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, numberType):
            return Vector(
                self.x / other,
                self.y / other,
                self.z / other,
            )
        return self.cross(other)

    def __rtruediv__(self, other):
        if isinstance(other, numberType):
            return Vector(
                other / self.x,
                other / self.y,
                other / self.z,
            )
        return other.__trudiv__(self)
    
    def __eq__(self, other):
        return (self.x == other.x and 
                self.y == other.y and
                self.z == other.z)
    
    def __pow__(self, other):
        if isinstance(other, numberType):
            return Vector(
                self.x ** other,
                self.y ** other,
                self.z ** other,
            )
        elif isinstance(other, Vector):
            return self.project_onto(other)
        else:
            raise TypeError
    
    def __rpow__(self, other):
        if isinstance(other, numberType):
            return Vector(
                other ** self.x,
                other ** self.y,
                other ** self.z
            )
    
    def __floor__(self):
        return Vector(
            self.x.__floor__(),
            self.y.__floor__(),
            self.z.__floor__()
        )
    
    def __ceil__(self):
        return Vector(
            self.x.__ceil__(),
            self.y.__ceil__(),
            self.z.__ceil__()
        )
    
    def __mod__(self, other):
        if isinstance(other, numberType):
            return Vector(
                self.x % other,
                self.y % other,
                self.z % other,
            )
        return self.dot(other)
    
    def __rmod__(self, other):
        if isinstance(other, numberType):
            return Vector(
                other % self.x,
                other % self.y,
                other % self.z,
            )
        return self.dot(other)