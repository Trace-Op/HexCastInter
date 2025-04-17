import core
from core import VMFrame

class ListPackOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="PACK",
            signature="..., Num -> List",
            name="Create List",
            game_name="Flock's Gambit",
            parameters=None,  # dynamic type inferences not fully implemented
            output=[tuple]
        )
    def execute(self, frame: VMFrame):
        n = frame.stack.pop()
        lst = frame.stack[-n:]
        frame.stack = frame.stack[:-n]
        frame.stack.append(tuple(lst))

class ListExpandOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="UNPACK",
            signature="List -> ...",
            name="Expand List",
            game_name="Flock's Disintegration",
            parameters=[tuple],
            output=None  # dynamic, inferred from parameter 0 length
        )
    def execute(self, frame: VMFrame):
        lst = frame.stack.pop()
        frame.stack.extend(lst)

class ListNewOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="LIST",
            signature="-> List",
            name="New Empty List",
            game_name="Vacant Reflection",
            parameters=[],
            output=[tuple]
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(tuple())

class ListSingleOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="WRAP",
            signature="Any -> List",
            name="Create list of single item",
            game_name="Single's Purification",
            parameters=[core.Iota],
            output=[tuple]
        )
    def execute(self, frame: VMFrame):
        e = frame.stack.pop()
        frame.stack.append(tuple([e]))

class ListConcatOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="CONCAT",
            signature="List, List -> List",
            name="Concatenate Lists",
            game_name="Additive Distillation",
            parameters=[tuple, tuple],
            output=[tuple]
        )
    def execute(self, frame: VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        r = b + a
        frame.stack.append(r)

class LengthOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="LEN",
            signature="List -> Num",
            name="Length",
            game_name="Length Purification",
            parameters=[tuple],
            output=[int]
        )
    def execute(self, frame: VMFrame):
        lst = frame.stack.pop()
        frame.stack.append(len(lst))

class SelectOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="SEL",
            signature="List, Num -> Any",
            name="Selection",
            game_name="Selection Distillation",
            parameters=[tuple, int],
            output=[core.Iota]
        )
    def execute(self, frame: VMFrame):
        idx = frame.stack.pop()
        lst = frame.stack.pop()
        r = lst[idx]
        frame.stack.append(r)

class ReverseOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="REV",
            signature="List -> List",
            name="Reverse List",
            game_name="Retrograde Purification",
            parameters=[tuple],
            output=[tuple]
        )
    def execute(self, frame: VMFrame):
        lst = frame.stack.pop()
        frame.stack.append(tuple(reversed(lst)))

class ListPopOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="LISTPOP",
            signature="List -> List, Any",
            name="Pop from List",
            game_name="Derivation Decomposition",
            parameters=[tuple],
            output=[tuple, core.Iota]
        )
    def execute(self, frame: VMFrame):
        lst = frame.stack.pop()
        e = lst[-1]
        lst = lst[:-1]
        frame.stack.append(lst)
        frame.stack.append(e)

class ListAppendOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="APPEND",
            signature="List, Any -> List",
            name="Append to List",
            game_name="Integration Distillation",
            parameters=[tuple, core.Iota],
            output=[tuple]
        )
    def execute(self, frame: VMFrame):
        e = frame.stack.pop()
        lst = frame.stack.pop()
        r = lst + tuple([e])
        frame.stack.append(r)

class ListPushOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="LISTPUSH",
            signature="List, Any -> List",
            name="Left Push",
            game_name="Speaker's Distillation",
            parameters=[tuple, core.Iota],
            output=[tuple]
        )
    def execute(self, frame: VMFrame):
        e = frame.stack.pop()
        lst = frame.stack.pop()
        r = tuple([e]) + lst
        frame.stack.append(r)

class ListPopLeftOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="LISTPOPLEFT",
            signature="List -> List, Any",
            name="Pop Left",
            game_name="Speaker's Decomposition",
            parameters=[tuple],
            output=[tuple, core.Iota]
        )
    def execute(self, frame: VMFrame):
        lst = frame.stack.pop()
        e = lst[0]
        lst = lst[1:]
        frame.stack.append(lst)
        frame.stack.append(e)

class ListSubListOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="SUBLIST",
            signature="List, Num, Num -> List",
            name="Subarray of List",
            game_name="Selection Exaltation",
            parameters=[tuple, int, int],
            output=[tuple]
        )
    def execute(self, frame: VMFrame):
        end = frame.stack.pop()
        start = frame.stack.pop()
        lst = frame.stack.pop()
        r = lst[start:end]
        frame.stack.append(r)

class ListRemoveOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="REM",
            signature="List, Num -> List",
            name="Remove item from list",
            game_name="Excisor's Distillation",
            parameters=[tuple, int],
            output=[tuple]
        )
    def execute(self, frame: VMFrame):
        idx = frame.stack.pop()
        lst = frame.stack.pop()
        left = lst[:idx]
        right = lst[idx+1:]
        r = left + right
        frame.stack.append(r)

class ListSetItemOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="SET",
            signature="List, Num, Any -> List",
            name="Set index to item",
            game_name="Surgeon's Exaltation",
            parameters=[tuple, int, core.Iota],
            output=[tuple]
        )
    def execute(self, frame: VMFrame):
        e = frame.stack.pop()
        idx = frame.stack.pop()
        lst = frame.stack.pop()
        left = lst[:idx]
        right = lst[idx+1:]
        r = left + tuple([e]) + right
        frame.stack.append(r)

class ListSearchOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="SEARCH",
            signature="List, Any -> Num",
            name="Search List",
            game_name="Locator's Distillation",
            parameters=[tuple, core.Iota],
            output=[int]
        )
    def execute(self, frame: VMFrame):
        e = frame.stack.pop()
        lst = frame.stack.pop()
        try:
            r = lst.index(e)
        except ValueError:
            r = -1
        frame.stack.append(r)
