from typing import Literal, Union, Tuple
from dataclasses import dataclass

from iota.Vector import Vector

Iota = Union[bool, None, int, float, str, Tuple, Vector, "Entity"]

@dataclass
class Entity:
    name: str
    position: Vector
    position_eyes: Vector
    facing: Vector
    velocity: Vector
    data_mode: Literal["r", "w", "rw"] = ""
    data: Iota = None

    def copy(self):
        return Entity(
            self.name,
            self.position,
            self.position_eyes,
            self.facing,
            self.velocity,
            self.data_mode,
            self.data
        )