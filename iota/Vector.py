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

    def __repr__(self) -> str:
        return f"<{self.x:.2f}, {self.y:.2f}, {self.z:.2f}>"

    def __add__(self, other):
        if isinstance(other, numberType):
            return Vector(
                self.x + other,
                self.y + other,
                self.z + other,
            )
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
        return self.__sub__(other)

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