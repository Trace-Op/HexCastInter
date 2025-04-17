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


class Euler(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="Euler",
            signature="-> Num",
            name="Euler's constant",
            game_name="Euler's Reflection",
            parameters=[],
            output=[float]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(math.e)