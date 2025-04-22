from typing import Union
import core
from core import VMFrame


class BoolOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="BOOL",
            signature="Any -> Bool",
            name="Boolean",
            game_name="Auger's Purification",
            parameters=[core.Iota],
            output=[bool]
        )

    def execute(self, frame: core.VMFrame):
        e = frame.stack.pop()
        if ((e == 0) or (e == False) or (e is None) or
            (isinstance(e, tuple) and len(e) == 0)):
            frame.stack.append(False)
        else:
            frame.stack.append(True)

class EqualityOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="EQ",
            signature="Any, Any -> Bool",
            name="Equal",
            game_name="Equality Distillation",
            parameters=[core.Iota, core.Iota],
            output=[bool]
        )
    def execute(self, frame: core.VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        r = b == a
        frame.stack.append(r)

class LessThanOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="LT",
            signature="Num, Num -> Bool",
            name="Less Than",
            game_name="Minimus Distillation",
            parameters=[Union[int, float], Union[int, float]],
            output=[bool]
        )
    def execute(self, frame: core.VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        r = b < a
        frame.stack.append(r)


class LessThanEqualOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="LTE",
            signature="Num, Num -> Bool",
            name="Less Than",
            game_name="Minimus Distillation II",
            parameters=[Union[int, float], Union[int, float]],
            output=[bool]
        )
    def execute(self, frame: core.VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        r = b <= a
        frame.stack.append(r)


class GreaterThanOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="GT",
            signature="Num, Num -> Bool",
            name="Less Than",
            game_name="Maximus Distillation",
            parameters=[Union[int, float], Union[int, float]],
            output=[bool]
        )
    def execute(self, frame: core.VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        r = b > a
        frame.stack.append(r)


class GreaterThanEqualOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="GTE",
            signature="Num, Num -> Bool",
            name="Less Than",
            game_name="Maximus Distillation II",
            parameters=[Union[int, float], Union[int, float]],
            output=[bool]
        )
    def execute(self, frame: core.VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        r = b >= a
        frame.stack.append(r)


class CondSel(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="IF_ELSE",
            signature="Bool, Any, Any -> Any",
            name="Conditional Selector (if-else)",
            game_name="Augur's Exaltation",
            parameters=[bool, core.Iota, core.Iota],
            output=[core.Iota]
        )
    def execute(self, frame: VMFrame):
        block_false = frame.stack.pop()
        block_true = frame.stack.pop()
        t = frame.stack.pop()
        if t:
            frame.stack.append(block_true)
        else:
            frame.stack.append(block_false)


class NotOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="NOT",
            signature="Bool -> Bool",
            name="Negate Bool",
            game_name="Negation Purification",
            parameters=[bool],
            output=[bool]
        )
    def execute(self, frame: VMFrame):
        b = frame.stack.pop()
        frame.stack.append(not b)


class OrOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="OR",
            signature="Bool, Bool -> Bool",
            name="Or",
            game_name="Disjunction Distillation",
            parameters=[bool, bool],
            output=[bool]
        )
    def execute(self, frame: VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        frame.stack.append(a or b)

class AndOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="AND",
            signature="Bool, Bool -> Bool",
            name="And",
            game_name="Conjunction Distillation",
            parameters=[bool, bool],
            output=[bool]
        )
    def execute(self, frame: VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        frame.stack.append(a and b)

class XorOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="XOR",
            signature="Bool, Bool -> Bool",
            name="And",
            game_name="Exclusion Distillation",
            parameters=[bool, bool],
            output=[bool]
        )
    def execute(self, frame: VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        frame.stack.append(a ^ b)