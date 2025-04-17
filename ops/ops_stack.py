import core
from core import VMFrame


class Drop(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="DROP",
            signature="Any -> ",
            name="Drop",
            game_name="Novice's Gambit",
            parameters=[core.Iota],
            output=[None],
        )
    def execute(self, frame: VMFrame):
        _ = frame.stack.pop()


class DuplicateOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="DUP",
            signature="Any -> Any, Any",
            name="Duplicate",
            game_name="Gemini Decomposition",
            parameters=[core.Iota],
            output=[core.Iota, core.Iota],
        )
    def execute(self, frame: VMFrame):
        e = frame.stack.pop()
        frame.stack.append(e)
        frame.stack.append(e)


class Duplicate2(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="DUP2",
            signature="Any, Any -> Any, Any, Any, Any",
            name="Duplicate 2",
            game_name="Dioscuri Gambit",
            parameters=[core.Iota, core.Iota],
            output=[core.Iota, core.Iota, core.Iota, core.Iota],
        )
    def execute(self, frame: VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        frame.stack.append(a)
        frame.stack.append(b)
        frame.stack.append(a)
        frame.stack.append(b)


class Replicate(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="REP",
            signature="Any, Num -> ...",
            name="Replicate",
            game_name="Gemini Gambit",
            parameters=[core.Iota, core.Number],
            output=None,  # variable output
        )
    def execute(self, frame: VMFrame):
        n = frame.stack.pop()
        e = frame.stack.pop()
        lst = [e]*n
        frame.stack.extend(lst)


class SwapOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="SWAP",
            signature="Any, Any -> Any, Any",
            name="Swap",
            game_name="Jester's Gambit",
            parameters=[core.Iota, core.Iota],
            output=[core.Iota, core.Iota],
        )
    def execute(self, frame: VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        frame.stack.append(a)
        frame.stack.append(b)


class RotateRightOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="ROTATE_RIGHT",
            signature="Any, Any, Any -> Any, Any, Any",
            name="Rotate Right",
            game_name="Rotation Gambit",
            parameters=[core.Iota, core.Iota, core.Iota],
            output=[core.Iota, core.Iota, core.Iota],
        )

    def execute(self, frame: VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        c = frame.stack.pop()
        frame.stack.append(b)
        frame.stack.append(a)
        frame.stack.append(c)


class RotateLeftOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="ROTATE_LEFT",
            signature="Any, Any, Any -> Any, Any, Any",
            name="Rotate Left",
            game_name="Rotation Gambit II",
            parameters=[core.Iota, core.Iota, core.Iota],
            output=[core.Iota, core.Iota, core.Iota],
        )
    def execute(self, frame: VMFrame):
        a = frame.stack.pop()
        b = frame.stack.pop()
        c = frame.stack.pop()
        frame.stack.append(a)
        frame.stack.append(c)
        frame.stack.append(b)


class Move(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="MOVE",
            signature="Num -> Any",
            name="Pick and Place",
            game_name="Fisherman's Gambit",
            parameters=[core.Number],
            output=[core.Iota],
        )
    def execute(self, frame: VMFrame):
        idx = frame.stack.pop()
        if idx > 0:  # Roll
            e = frame.stack[-idx-1]
            del frame.stack[-idx-1]
            frame.stack.append(e)
        elif idx < 0:  # Bury
            e = frame.stack.pop()
            frame.stack.insert(idx, e)
        # else idx == 0: equiv to Drop


class Copy(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="COPY",
            signature="Num -> Any",
            name="Inspect Stack",
            game_name="Fisherman's Gambit II",
            parameters=[core.Number],
            output=[core.Iota],
        )
    def execute(self, frame: VMFrame):
        idx = frame.stack.pop()
        if idx > 0:  # Inspect
            e = frame.stack[-idx - 1]
            frame.stack.append(e)
        elif idx < 0:  # Dup and Bury
            e = frame.stack[-1]
            frame.stack.insert(idx-1, e)

class Height(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="HEIGHT",
            signature=" -> Num",
            name="Height",
            game_name="Flock's Reflection",
            parameters=[],
            output=[core.Number],
        )
    def execute(self, frame: VMFrame):
        frame.stack.append(len(frame.stack))