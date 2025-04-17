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
    }

    def __init__(self):
        super().__init__(
            mnemonic="ADD",
            signature="Num|Vec, Num|Vec -> Num|Vec",
            name="Add",
            game_name="Additive Distillation",
            parameters=(Union[core.Number, core.Vector], Union[core.Number, core.Vector],),
            output=(Union[core.Number, core.Vector],)
        )

    def execute(self, frame: core.VMFrame):
        b = frame.stack.pop()
        a = frame.stack.pop()
        r = a + b  # type checking supported by Vector.__add__ and Vector.__radd__
        frame.stack.append(r)

    def infer_output_type(self, args: list):
        a_type, b_type = args[0], args[1]
        r_type = self.type_dispatch.get((a_type, b_type,), None)
        if r_type is None:
            raise ValueError("ADD: Bad operands")
        else:
            return r_type


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
