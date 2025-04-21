from typing import Union
import math
import core
from core import VMFrame


class AddOp(core.Operation):
    type_dispatch = {
        (core.Number, core.Number): (core.Number,),
        (core.Vector, core.Vector): (core.Vector,),
        (core.Vector, core.Number): (core.Vector,),
        (core.Number, core.Vector): (core.Vector,),
        (tuple, tuple): (tuple,),
    }

    def __init__(self):
        super().__init__(
            mnemonic="ADD",
            signature="(Num|Vec, Num|Vec -> Num|Vec) or (List, List -> List)",
            name="Add",
            game_name="Additive Distillation",
            parameters=(Union[core.Number, core.Vector, tuple], Union[core.Number, core.Vector, tuple],),
            output=(Union[core.Number, core.Vector, tuple],),
            alias=["CONCAT"],
        )

    def execute(self, frame: core.VMFrame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return
        
        if len(frame.stack) == 1:
            frame.stack.append(core.Garbage())
            return

        b = frame.stack.pop()
        a = frame.stack.pop()

        try:
            r = a + b
        except TypeError as e:
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return

        frame.stack.append(r)

    def infer_output_type(self, args: list):
        a_type, b_type = args[0], args[1]
        r_type = self.type_dispatch.get((a_type, b_type,), None)
        if r_type is None:
            raise ValueError("ADD: Bad operands")
        else:
            return r_type
    
    tests = [
        ("basic addition", "5 1 ADD", [6]),
        ("vector addition", "3 0 1 PACKVEC 4 1 0 PACKVEC ADD", [core.Vector(7, 1, 1)]),
        ("scalar broadcast (right)", "0 0 1 PACKVEC 1 ADD", [core.Vector(1, 1, 2)]),
        ("scalar broadcast (left)", "1 3 4 5 PACKVEC ADD", [core.Vector(4, 5, 6)]),
        ("List concatonation", "4 5 6 3 PACK 7 8 9 3 PACK ADD", [(4, 5, 6, 7, 8, 9,)]),
        ("insufficient parameters 0 of 2", "ADD", [core.Garbage(), core.Garbage()]),
        ("insufficient parameters 1 of 2", "5 ADD", [5, core.Garbage()]),
        ("invalid type (left)", "PLAYER 5 ADD", [core.Garbage(), core.Garbage()]),
        ("invalid type (right)", "5 PLAYER ADD", [core.Garbage(), core.Garbage()]),
        ("invalid types", "PLAYER PLAYER ADD", [core.Garbage(), core.Garbage()]),
        ("incompatible types (List, Num)", "LIST 5 ADD", [core.Garbage(), core.Garbage()]),
        ("incompatible types (Num, List)", "5 LIST ADD", [core.Garbage(), core.Garbage()]),
        ("incompatible types (Vec, List)", "1 0 0 PACKVEC LIST ADD", [core.Garbage(), core.Garbage()]),
        ("incompatible types (List, Vec)", "LIST 1 0 0 PACKVEC ADD", [core.Garbage(), core.Garbage()]),
        ("incompatible types (List, str)", "LIST $pattern ADD", [core.Garbage(), core.Garbage()]),
    ]


class SubOp(core.Operation):
    type_dispatch = {
        (core.Number, core.Number): (core.Number,),
        (core.Vector, core.Vector): (core.Vector,),
        (core.Vector, core.Number): (core.Vector,),
        (core.Number, core.Vector): (core.Vector,),
    }

    def __init__(self):
        super().__init__(
            mnemonic="SUB",
            signature="Num|Vec, Num|Vec -> Num|Vec",
            name="Subtract",
            game_name="Subtractive Distillation",
            parameters=(Union[core.Number, core.Vector], Union[core.Number, core.Vector],),
            output=(Union[core.Number, core.Vector],)
        )
    def execute(self, frame: core.VMFrame):
        b = frame.stack.pop()
        a = frame.stack.pop()
        r = a - b
        frame.stack.append(r)

    def infer_output_type(self, args: list):
        a_type, b_type = args[0], args[1]
        r_type = self.type_dispatch.get((a_type, b_type,), None)
        if r_type is None:
            raise ValueError("SUB: Bad operands")
        else:
            return r_type


class MultiplyOp(core.Operation):
    type_dispatch = {
        (core.Number, core.Number): (core.Number,),
        (core.Vector, core.Vector): (core.Vector,),
        (core.Vector, core.Number): (core.Vector,),
        (core.Number, core.Vector): (core.Vector,),
    }

    def __init__(self):
        super().__init__(
            mnemonic="MUL",
            signature="Num|Vec, Num|Vec -> Num|Vec",
            name="Multiply/Dot Product",
            game_name="Multiplicative Distillation",
            parameters=(Union[core.Number, core.Vector], Union[core.Number, core.Vector],),
            output=(Union[core.Number, core.Vector],)
        )
    def execute(self, frame: core.VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        r = b * a
        frame.stack.append(r)

    def infer_output_type(self, args: list):
        a_type, b_type = args[0], args[1]
        r_type = self.type_dispatch.get((a_type, b_type,), None)
        if r_type is None:
            raise ValueError("SUB: Bad operands")
        else:
            return r_type


class DivideOp(core.Operation):
    type_dispatch = {
        (core.Number, core.Number): (core.Number,),
        (core.Vector, core.Vector): (core.Vector,),
        (core.Vector, core.Number): (core.Vector,),
        (core.Number, core.Vector): (core.Vector,),
    }

    def __init__(self):
        super().__init__(
            mnemonic="DIV",
            signature="Num|Vec, Num|Vec -> Num|Vec",
            name="Multiply/Dot Product",
            game_name="Division Distillation",
            parameters=(Union[core.Number, core.Vector], Union[core.Number, core.Vector],),
            output=(Union[core.Number, core.Vector],)
        )
    def execute(self, frame: core.VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        r = b / a
        frame.stack.append(r)

    def infer_output_type(self, args: list):
        a_type, b_type = args[0], args[1]
        r_type = self.type_dispatch.get((a_type, b_type,), None)
        if r_type is None:
            raise ValueError("SUB: Bad operands")
        else:
            return r_type


class AbsoluteOp(core.Operation):
    type_dispatch = {
        (core.Number,): (core.Number,),
        (core.Vector,): (core.Vector,),
    }
    def __init__(self):
        super().__init__(
            mnemonic="ABS",
            signature="Num|Vec -> Num",
            name="Absolute Value",
            game_name="Length Purification",
            parameters=[Union[core.Number, core.Vector]],
            output=[core.Number]
        )
    def execute(self, frame: core.VMFrame):
        a = frame.stack.pop()
        r = abs(a)
        frame.stack.append(r)
    def infer_output_type(self, args: list):
        a_type, b_type = args[0]
        r_type = self.type_dispatch.get((a_type,), None)
        if r_type is None:
            raise ValueError("ABS: Bad operands")
        else:
            return r_type

class VectorOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="PACKVEC",
            signature="Num, Num, Num -> Vec",
            name="Create Vector",
            game_name="Vector Exaltation",
            parameters=[core.Number, core.Number, core.Number],
            output=[core.Vector]
        )
    def execute(self, frame: VMFrame):
        z = frame.stack.pop()
        y = frame.stack.pop()
        x = frame.stack.pop()
        v = core.Vector(x=x, y=y, z=z)
        frame.stack.append(v)

class VectorExpandOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="UNPACKVEC",
            signature="VEC -> Num, Num, Num",
            name="Vector Decomposition",
            game_name="Vector Disintegration",
            parameters=[core.Vector],
            output=[core.Number, core.Number, core.Number]
        )
    def execute(self, frame: VMFrame):
        v: core.Vector = frame.stack.pop()
        x = v.x
        y = v.y
        z = v.z
        frame.stack.append(x)
        frame.stack.append(y)
        frame.stack.append(z)
