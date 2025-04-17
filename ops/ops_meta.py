import core
from core import VMFrame
from copy import deepcopy

class Exec(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="EXEC",
            signature="List -> ...",
            name="Execute block",
            game_name="Hermes' Gambit",
            parameters=[tuple],
            output=None  # output block dependant
        )
    def execute(self, frame: VMFrame):
        block = frame.stack.pop()
        for e in block:
            if frame.machine.verbose_exec:
                print(e)
            if e == "HALT":
                break
            frame.machine.process_token(e)


class Halt(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="HALT",
            signature="->",
            name="Halt execution",
            game_name="Charon's Gambit",
            parameters=[],
            output=[],
        )
    def execute(self, frame: VMFrame):
        # this should never happen.
        # while exec'ing a block, the block's forEach should handle HALT
        # while in the interpreter, the repl loop should handle HALT
        raise RuntimeError("Attempted to execute HALT")


class Thoth(core.Operation):
    # Thoth is a weird one, not quite map.
    # it creates a copy of the stack, appends the element, maps then collects the entire stack,
    # placing the collection on top of the stack snapshot
    def __init__(self):
        super().__init__(
            mnemonic="THOTH",
            signature="List, List -> List",
            name="ForEach Replicate Collect",
            game_name="Thoth's Gambit",
            parameters=[tuple, tuple],
            output=[tuple],
        )
    def execute(self, frame: VMFrame):
        lst = frame.stack.pop()
        block = frame.stack.pop()
        snapshot = deepcopy(frame.stack)

        result = []

        for item in lst:
            frame.stack = deepcopy(snapshot)
            frame.stack.append(item)
            frame.stack.append(block)

            for e in block:
                if e == "HALT":
                    break
                frame.machine.execute(e)

            result += deepcopy(frame.stack)

        frame.stack = deepcopy(snapshot)
        frame.stack.append(tuple(result))