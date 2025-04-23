import math

import core
from core import VMFrame

class TrueLiteral(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="TRUE",
            signature="-> Bool",
            name="True",
            game_name="True Reflection",
            parameters=[],
            output=[bool]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(True)
    
    tests = [
        ("True object", "TRUE", [True]),
    ]


class FalseLiteral(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="FALSE",
            signature="-> Bool",
            name="False",
            game_name="False Reflection",
            parameters=[],
            output=[bool]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(False)

    tests = [
        ("False object", "FALSE", [False]),
    ]


class NullLiteral(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="NULL",
            signature="-> Null",
            name="Null",
            game_name="Nullary Reflection",
            parameters=[],
            output=[type(None)]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(None)
    
    tests = [
        ("Null object", "NULL", [None]),
    ]


#  I did not choose this, go ask hexcasting devs why these vectors are builtins
class VectorOrigin(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="VECORIGIN",
            signature="-> Vec",
            name="Vector Origin",
            game_name="Vector Reflection Zero",
            parameters=[],
            output=[core.Vector]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(core.Vector(0, 0, 0))
    
    tests = [
        ("Vector(0,0,0)", "VECORIGIN", [core.Vector(0, 0, 0)]),
    ]


class VectorXPos(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="VECXPOS",
            signature="-> Vec",
            name="Vector (1,0,0)",
            game_name="Vector Reflection +X",
            parameters=[],
            output=[core.Vector]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(core.Vector(1,0,0))
    
    tests = [
        ("Vector(1,0,0)", "VECXPOS", [core.Vector(1, 0, 0)]),
    ]


class VectorXNeg(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="VECXNEG",
            signature="-> Vec",
            name="Vector (-1,0,0)",
            game_name="Vector Reflection -X",
            parameters=[],
            output=[core.Vector]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(core.Vector(-1,0,0))

    tests = [
        ("Vector(-1,0,0)", "VECXNEG", [core.Vector(-1,0,0)]),
    ]


class VectorYPos(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="VECYPOS",
            signature="-> Vec",
            name="Vector (0,1,0)",
            game_name="Vector Reflection +Y",
            parameters=[],
            output=[core.Vector]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(core.Vector(0,1,0))
    
    tests = [
        ("Vector(0,1,0)", "VECYPOS", [core.Vector(0, 1, 0)]),
    ]


class VectorYNeg(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="VECYNEG",
            signature="-> Vec",
            name="Vector (0,-1,0)",
            game_name="Vector Reflection -Y",
            parameters=[],
            output=[core.Vector]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(core.Vector(0,-1,0))
    
    tests = [
        ("Vector(0,-1,0)", "VECYNEG", [core.Vector(0, -1, 0)]),
    ]


class VectorZPos(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="VECZPOS",
            signature="-> Vec",
            name="Vector (0,0,1)",
            game_name="Vector Reflection +Z",
            parameters=[],
            output=[core.Vector]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(core.Vector(0, 0, 1))

    tests = [
        ("Vector(0,0,1)", "VECZPOS", [core.Vector(0, 0, 1)]),
    ]


class VectorZNeg(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="VECZNEG",
            signature="-> Vec",
            name="Vector (0,0,-1)",
            game_name="Vector Reflection -Z",
            parameters=[],
            output=[core.Vector]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(core.Vector(0, 0, -1))
    
    tests = [
        ("Vector(0,0,-1)", "VECZNEG", [core.Vector(0, 0, -1)]),
    ]


class Tau(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="TAU",
            signature="-> Num",
            name="Tau",
            game_name="Circle's Reflection",
            parameters=[],
            output=[float]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(math.tau)
    
    tests = [
        ("Tau constant", "TAU", [math.tau]),
    ]


class Pi(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="PI",
            signature="-> Num",
            name="Pi",
            game_name="Arc's Reflection",
            parameters=[],
            output=[float]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(math.pi)

    tests = [
        ("Pi constant", "PI", [math.pi]),
        ("Pi Tau relation", "PI 2 MUL", [math.tau]),
        ("Pi Tau relation", "TAU 2 DIV", [math.pi]),
    ]


class Euler(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="EULER",
            signature="-> Num",
            name="Euler's constant",
            game_name="Euler's Reflection",
            parameters=[],
            output=[float]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(math.e)
    
    tests = [
        ("Eulers constant", "EULER", [math.e]),
    ]

