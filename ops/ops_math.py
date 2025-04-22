from typing import Union
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

        if (not isinstance(a, self.parameters[0]) or 
            not isinstance(b, self.parameters[1]) or
            #  python bool is a numbers.Number
            isinstance(a, bool) or
            isinstance(b, bool)
        ):
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return

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
        ("invalid types (bool)", "5 1 BOOL ADD", [core.Garbage(), core.Garbage()]),
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
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return
        
        if len(frame.stack) == 1:
            frame.stack.append(core.Garbage())
            return
        
        b = frame.stack.pop()
        a = frame.stack.pop()
        
        if (not isinstance(a, self.parameters[0]) or 
            not isinstance(b, self.parameters[1]) or
            #  python bool is a numbers.Number
            isinstance(a, bool) or
            isinstance(b, bool)
        ):
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return

        try:
            r = a - b
        except TypeError as e:
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return
        
        frame.stack.append(r)

    def infer_output_type(self, args: list):
        a_type, b_type = args[0], args[1]
        r_type = self.type_dispatch.get((a_type, b_type,), None)
        if r_type is None:
            raise ValueError("SUB: Bad operands")
        else:
            return r_type

    tests = [
        ("basic subtraction", "1 5 SUB", [-4]),
        ("vector subtraction", "3 0 1 PACKVEC 4 1 0 PACKVEC SUB", [core.Vector(-1, -1, 1)]),
        ("scalar broadcast (right)", "0 0 1 PACKVEC 1 SUB", [core.Vector(-1, -1, 0)]),
        ("scalar broadcast (left)", "1 3 4 5 PACKVEC SUB", [core.Vector(-2, -3, -4)]),
        ("insufficient parameters 0 of 2", "SUB", [core.Garbage(), core.Garbage()]),
        ("insufficient parameters 1 of 2", "5 SUB", [5, core.Garbage()]),
        ("invalid type (left)", "PLAYER 5 SUB", [core.Garbage(), core.Garbage()]),
        ("invalid type (right)", "5 PLAYER SUB", [core.Garbage(), core.Garbage()]),
        ("invalid types", "LIST LIST SUB", [core.Garbage(), core.Garbage()]),
        ("invalid types (bool)", "5 1 BOOL SUB", [core.Garbage(), core.Garbage()]),
    ]


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
            output=(Union[core.Number, core.Vector],),
            alias=["DOT"],
        )
    def execute(self, frame: core.VMFrame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return
        
        if len(frame.stack) == 1:
            frame.stack.append(core.Garbage())
            return
    
        a = frame.stack.pop()
        b = frame.stack.pop()
    
        if (not isinstance(a, self.parameters[0]) or 
            not isinstance(b, self.parameters[1]) or
            #  python bool is a numbers.Number
            isinstance(a, bool) or
            isinstance(b, bool)
        ):
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return

        try:
            r = a * b
        except TypeError as e:
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return
    
        frame.stack.append(r)

    def infer_output_type(self, args: list):
        a_type, b_type = args[0], args[1]
        r_type = self.type_dispatch.get((a_type, b_type,), None)
        if r_type is None:
            raise ValueError("SUB: Bad operands")
        else:
            return r_type

    tests = [
        ("basic multiplication", "1 5 MUL", [5]),
        ("vector dot product", "1 2 3 PACKVEC 3 4 5 PACKVEC MUL", [26]),
        ("scalar multiplication (right)", "0 0 1 PACKVEC 1 MUL", [core.Vector(0, 0, 1)]),
        ("scalar multiplication (left)", "1 3 4 5 PACKVEC MUL", [core.Vector(3, 4, 5)]),
        ("insufficient parameters 0 of 2", "MUL", [core.Garbage(), core.Garbage()]),
        ("insufficient parameters 1 of 2", "5 MUL", [5, core.Garbage()]),
        ("invalid type (left)", "PLAYER 5 MUL", [core.Garbage(), core.Garbage()]),
        ("invalid type (right)", "5 PLAYER MUL", [core.Garbage(), core.Garbage()]),
        ("invalid types", "LIST LIST MUL", [core.Garbage(), core.Garbage()]),
        ("Invalid type (bool)", "1 BOOL 5 MUL", [core.Garbage(), core.Garbage()]),
    ]


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
            output=(Union[core.Number, core.Vector],),
            alias=["CROSS"],
        )
    def execute(self, frame: core.VMFrame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return
        
        if len(frame.stack) == 1:
            frame.stack.append(core.Garbage())
            return
    
        a = frame.stack.pop()
        b = frame.stack.pop()
    
        if (not isinstance(a, self.parameters[0]) or 
            not isinstance(b, self.parameters[1]) or
            #  python bool is a numbers.Number
            isinstance(a, bool) or
            isinstance(b, bool)
        ):
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return

        try:
            r = b / a
        except TypeError as e:
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return
    
        frame.stack.append(r)

    def infer_output_type(self, args: list):
        a_type, b_type = args[0], args[1]
        r_type = self.type_dispatch.get((a_type, b_type,), None)
        if r_type is None:
            raise ValueError("SUB: Bad operands")
        else:
            return r_type

    tests = [
        ("basic division", "10 5 DIV", [2]),
        ("vector cross product", "1 2 3 PACKVEC 3 4 5 PACKVEC DIV", [core.Vector(-2, 4, -2)]),
        ("scalar division (right)", "10 20 30 PACKVEC 5 DIV", [core.Vector(2, 4, 6)]),
        ("scalar division (left)", "12 2 3 4 PACKVEC DIV", [core.Vector(6, 4, 3)]),
        ("insufficient parameters 0 of 2", "DIV", [core.Garbage(), core.Garbage()]),
        ("insufficient parameters 1 of 2", "5 DIV", [5, core.Garbage()]),
        ("invalid type (left)", "PLAYER 5 DIV", [core.Garbage(), core.Garbage()]),
        ("invalid type (right)", "5 PLAYER DIV", [core.Garbage(), core.Garbage()]),
        ("invalid types", "LIST LIST DIV", [core.Garbage(), core.Garbage()]),
        ("Invalid type (bool)", "1 BOOL 5 DIV", [core.Garbage(), core.Garbage()]),
    ]


class AbsoluteOp(core.Operation):
    type_dispatch = {
        (core.Number,): (core.Number,),
        (core.Vector,): (core.Number,),
        (bool,): (core.Number),
        (tuple,): (core.Number),
    }
    def __init__(self):
        super().__init__(
            mnemonic="ABS",
            signature="Num|Vec -> Num",
            name="Absolute Value",
            game_name="Length Purification",
            parameters=[Union[core.Number, core.Vector]],
            output=[core.Number],
            alias=["LEN", "BOOLTONUM"],
        )

    def execute(self, frame: core.VMFrame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            return

        a = frame.stack.pop()
        
        if isinstance(a, tuple):
            r = len(a)
        elif isinstance(a, bool):
            r = int(a)
        elif isinstance(a, core.Number) or isinstance(a, core.Vector):
            r = abs(a)
        else:
            r = core.Garbage()
        
        frame.stack.append(r)
    
    def infer_output_type(self, args: list):
        a_type, b_type = args[0]
        r_type = self.type_dispatch.get((a_type,), None)
        if r_type is None:
            raise ValueError("ABS: Bad operands")
        else:
            return r_type

    tests = [
        ("Numeric absolute value", "5 ABS", [5]),
        ("Numeric absolute value", "-5 ABS", [5]),
        ("Vector magnitude", "3 0 0 PACKVEC ABS", [3]),
        ("Vector magnitude", "4 -8 8 PACKVEC ABS", [12]),
        ("List length", "[ 0 1 2 3 4 ] ABS", [5]),
        ("Boolean to number coersion", "TRUE ABS", [1]),
        ("Boolean to number coersion", "FALSE ABS", [0]),
        ("Invalid type", "PLAYER ABS", [core.Garbage()]),
        ("Insufficient parameters 0 of 1", "ABS", [core.Garbage()]),
    ]

class VectorPack(core.Operation):
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
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return
        if len(frame.stack) == 1:
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return
        if len(frame.stack) == 2:
            frame.stack.append(core.Garbage())
            return
        
        z = frame.stack.pop()
        y = frame.stack.pop()
        x = frame.stack.pop()

        if ((not isinstance(x, core.Number)) or isinstance(x, bool) or
            (not isinstance(y, core.Number)) or isinstance(y, bool) or
            (not isinstance(z, core.Number)) or isinstance(z, bool)
            ):
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return

        v = core.Vector(x=x, y=y, z=z)

        frame.stack.append(v)
    
    tests = [
        ("Vector Packing", "0 4 5 PACKVEC", [core.Vector(0, 4, 5)]),
        ("Insufficient parameters 0 of 3", "PACKVEC", [core.Garbage(), core.Garbage(), core.Garbage()]),
        ("Insufficient parameters 1 of 3", "10 PACKVEC", [10, core.Garbage(), core.Garbage()]),
        ("Insufficient parameters 2 of 3", "10 20 PACKVEC", [10, 20, core.Garbage()]),
        ("Invalid Types", "10 PLAYER 30 PACKVEC", [core.Garbage(), core.Garbage(), core.Garbage()]),
        ("Invalid Types (bool)", "10 TRUE 30 PACKVEC", [core.Garbage(), core.Garbage(), core.Garbage()]),
    ]


class VectorExpand(core.Operation):
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
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            return
        
        v = frame.stack.pop()
        
        if not isinstance(v, core.Vector):
            frame.stack.append(core.Garbage())
            return
        
        x = v.x
        y = v.y
        z = v.z

        frame.stack.append(x)
        frame.stack.append(y)
        frame.stack.append(z)

    tests = [
        ("Vector expansion", "3 4 5 PACKVEC UNPACKVEC", [3, 4, 5]),
        ("Insufficient parameters 0 of 1", "UNPACKVEC", [core.Garbage()]),
        ("Invalid type", "PLAYER UNPACKVEC", [core.Garbage()]),
        ("Invalid type", "3 4 5 3 PACK UNPACKVEC", [core.Garbage()]),
    ]


class ExpOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="EXP",
            signature="Num|Vec, Num|Vec -> Num|Vec",
            name="Exponentiaion/Projection",
            game_name="Power Distillation",
            parameters=[Union[core.Number, core.Vector], Union[core.Number, core.Vector]],
            output=[Union[core.Number, core.Vector]],
            alias=["PROJECT"],
        )
    
    def execute(self, frame: VMFrame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return
        
        if len(frame.stack) == 1:
            frame.stack.append(core.Garbage())
            return
        
        n = frame.stack.pop()
        b = frame.stack.pop()

        if (isinstance(b, bool) or isinstance(n, bool)):
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return

        if not (isinstance(b, self.parameters[0]) and isinstance(n, self.parameters[1])):
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return

        r = b ** n

        frame.stack.append(r)

    
    tests = [
        ("Numerical exponentiation", "2 4 EXP", [16]),
        ("Zero base", "0 4 EXP", [0]),
        ("Scalar broadcast (right)", "0 1 2 PACKVEC 4 EXP", [core.Vector(0, 1, 16)]),
        ("Scalar broadcast (left)", "3 0 1 2 PACKVEC EXP", [core.Vector(1, 3, 9)]),
        ("Vector Projection", "6 6 6 PACKVEC 3 0 0 PACKVEC EXP", [core.Vector(6, 0, 0)]),
        ("Insufficient parameters 0 of 2", "EXP", [core.Garbage(), core.Garbage()]),
        ("Insufficient parameters 1 of 2", "2 EXP", [2, core.Garbage()]),
        ("Invalid Type", "PLAYER 2 EXP", [core.Garbage(), core.Garbage()]),
    ]


class FloorOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="FLOOR",
            signature="Num|Vec -> Num|Vec",
            name="Floor",
            game_name="Floor Purification",
            parameters=[Union[core.Number, core.Vector]],
            output=[Union[core.Number, core.Vector]],
        )
    
    def execute(self, frame: VMFrame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            return
        
        a = frame.stack.pop()

        if isinstance(a, bool):
            frame.stack.append(core.Garbage())
            return

        if not isinstance(a, self.parameters[0]):
            frame.stack.append(core.Garbage())
            return
        
        r = a.__floor__()

        frame.stack.append(r)

    tests = [
        ("Numeric Floor", "5 2 DIV FLOOR", [2]),
        ("Numeric Floor", "-5 2 DIV FLOOR", [-3]),
        ("Vector Floor", "5 2 DIV -5 2 DIV 1 PACKVEC FLOOR", [core.Vector(2, -3, 1)]),
        ("Zero Vector Floor", "0 0 0 PACKVEC FLOOR", [core.Vector(0, 0, 0)]),
        ("Invalid type", "PLAYER FLOOR", [core.Garbage()]),
        ("Invalid type bool", "TRUE FLOOR", [core.Garbage()]),
        ("Insufficient parameters 0 of 1", "FLOOR", [core.Garbage()]),
    ]


class CeilingOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="CEIL",
            signature="Num|Vec -> Num|Vec",
            name="Ceiling",
            game_name="Ceiling Purification",
            parameters=[Union[core.Number, core.Vector]],
            output=[Union[core.Number, core.Vector]],
        )
    
    def execute(self, frame: VMFrame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            return
        
        a = frame.stack.pop()

        if isinstance(a, bool):
            frame.stack.append(core.Garbage())
            return

        if not isinstance(a, self.parameters[0]):
            frame.stack.append(core.Garbage())
            return
        
        r = a.__ceil__()

        frame.stack.append(r)

    tests = [
        ("Numeric Floor", "5 2 DIV CEIL", [3]),
        ("Numeric Floor", "-5 2 DIV CEIL", [-2]),
        ("Vector Floor", "5 2 DIV -5 2 DIV 1 PACKVEC CEIL", [core.Vector(3, -2, 1)]),
        ("Zero Vector Floor", "0 0 0 PACKVEC FLOOR", [core.Vector(0, 0, 0)]),
        ("Invalid type", "PLAYER FLOOR", [core.Garbage()]),
        ("Invalid type bool", "TRUE FLOOR", [core.Garbage()]),
        ("Insufficient parameters 0 of 1", "FLOOR", [core.Garbage()]),
    ]


class ModulusOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="MOD",
            signature="Num|Vec, Num|Vec -> Num|Vec",
            name="Modulus",
            game_name="Modulus Distillation",
            parameters=(Union[core.Number, core.Vector], Union[core.Number, core.Vector],),
            output=(Union[core.Number, core.Vector],)
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
        
        if (not isinstance(a, self.parameters[0]) or 
            not isinstance(b, self.parameters[1]) or
            #  python bool is a numbers.Number
            isinstance(a, bool) or
            isinstance(b, bool)
        ):
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return

        try:
            r = a % b
        except TypeError as e:
            frame.stack.append(core.Garbage())
            frame.stack.append(core.Garbage())
            return
        
        frame.stack.append(r)

    tests = [
        ("Integer remainder", "5 2 MOD", [1]),
        ("Float remainder", "11 2 DIV 2 MOD", [1.5]),
        ("scalar broadcast (right)", "5 7 10 PACKVEC 3 MOD", [core.Vector(2, 1, 1)]),
        ("scalar broadcast (left)", "10 2 3 4 PACKVEC MOD", [core.Vector(0, 1, 2)]),
        ("insufficient parameters 0 of 2", "MOD", [core.Garbage(), core.Garbage()]),
        ("insufficient parameters 1 of 2", "5 MOD", [5, core.Garbage()]),
        ("invalid type (left)", "PLAYER 5 MOD", [core.Garbage(), core.Garbage()]),
        ("invalid type (right)", "5 PLAYER MOD", [core.Garbage(), core.Garbage()]),
        ("invalid types", "LIST LIST MOD", [core.Garbage(), core.Garbage()]),
        ("invalid types (bool)", "5 1 BOOL MOD", [core.Garbage(), core.Garbage()]),
    ]


class SignOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="SIGN",
            signature="Num|Vec -> Num|Vec",
            name="Sign",
            game_name="Axial Purification",
            parameters=[Union[core.Number, core.Vector]],
            output=[Union[core.Number, core.Vector]],
        )
    
    def execute(self, frame: VMFrame):
        if len(frame.stack) == 0:
            frame.stack.append(core.Garbage())
            return
        
        a = frame.stack.pop()

        if isinstance(a, bool):
            frame.stack.append(core.Garbage())
            return

        if not isinstance(a, self.parameters[0]):
            frame.stack.append(core.Garbage())
            return
        
        if isinstance(a, core.Number):
            if a > 0:
                frame.stack.append(1)
            elif a < 0:
                frame.stack.append(-1)
            else:
                frame.stack.append(0)
            return
        elif isinstance(a, core.Vector):
            r = a.clamp_to_basis()
            frame.stack.append(r)
            return

    tests = [
        ("Numeric pos sign", "5 SIGN", [1]),
        ("Numeric neg sign", "-5 SIGN", [-1]),
        ("Numeric zero sign", "0 SIGN", [0]),
        ("Vector clamping", "5 0 0 PACKVEC SIGN", [core.Vector(1, 0, 0)]),
        ("Vector clamping negative", "0 0 -5 PACKVEC SIGN", [core.Vector(0, 0, -1)]),
        ("Vector clamping zero", "0 0 0 PACKVEC SIGN", [core.Vector(0, 0, 0)]),
        ("Vector clamping order", "5 5 5 PACKVEC SIGN", [core.Vector(0, 1, 0)]),
        ("Vector clamping order", "5 5 0 PACKVEC SIGN", [core.Vector(0, 1, 0)]),
        ("Vector clamping order", "0 5 5 PACKVEC SIGN", [core.Vector(0, 1, 0)]),
        ("Vector clamping order", "5 0 5 PACKVEC SIGN", [core.Vector(0, 0, 1)]),
        ("Invalid type", "PLAYER SIGN", [core.Garbage()]),
        ("Invalid type bool", "TRUE SIGN", [core.Garbage()]),
        ("Insufficient parameters 0 of 1", "SIGN", [core.Garbage()]),
    ]


class GetRandom(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="RAND",
            signature="->Num",
            name="Random value",
            game_name="Entropy Reflection",
            parameters=[],
            output=[core.Number],
        )
    def execute(self, frame: VMFrame):
        frame.prng.setstate(frame.prng_state)
        r = frame.prng.random()
        frame.stack.append(r)
        frame.prng_state = frame.prng.getstate()
    
    tests = [
        ("Random lower bound", "RAND 0 GT", [True]),
        ("Random upper bound", "RAND 1 LT", [True]),
    ]