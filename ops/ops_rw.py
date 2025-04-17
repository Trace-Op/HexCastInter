import core
from core import VMFrame


class PrintOp(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="PRINT",
            signature="Any->Any",
            name="print",
            game_name="Reveal",
            parameters=[core.Iota],
            output=[core.Iota],
        )
    def execute(self, frame: VMFrame):
        print(frame.stack[-1])


class RavenRead(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="UNCACHE",
            signature="-> Any",
            name="Read Cache",
            game_name="Muninn's Reflection",
            parameters=[],
            output=[core.Iota],
        )
    def execute(self, frame: core.VMFrame):
        frame.stack.append(frame.scratch)


class RavenWrite(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="CACHE",
            signature="Any ->",
            name="Write Cache",
            game_name="Huginn's Gambit",
            parameters=[core.Iota],
            output=[],
        )
    def execute(self, frame: core.VMFrame):
        e = frame.stack.pop()
        frame.scratch = e


class HandRead(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="LD",
            signature="-> Any",
            name="Read Hand",
            game_name="Scribe's Reflection",
            parameters=[],
            output=[core.Iota],
        )
    def execute(self, frame: core.VMFrame):
        frame.stack.append(frame.hand)


class HandCanRead(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="LDACCESS",
            signature="-> Bool",
            name="Hand Readable",
            game_name="Auditor's Reflection",
            parameters=[],
            output=[bool]
        )
    def execute(self, frame: core.VMFrame):
        frame.stack.append('r' in frame.hand_mode)


class HandWrite(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="ST",
            signature="Any ->",
            name="Write to Hand",
            game_name="Scribe's Gambit",
            parameters=[core.Iota],
            output=[],
        )
    def execute(self, frame: core.VMFrame):
        e = frame.stack.pop()
        frame.hand = e


class HandCanWrite(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="STACCESS",
            signature="-> Bool",
            name="Hand Writable",
            game_name="Assessor's Reflection",
            parameters=[],
            output=[bool],
        )
    def execute(self, frame: core.VMFrame):
        frame.stack.append('w' in frame.hand_mode)


class EntityRead(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="READ",
            signature="Entity -> Any",
            name="Read from Entity",
            game_name="Chronicler's Purification",
            parameters=[core.Entity],
            output=[core.Iota],
        )
    def execute(self, frame: core.VMFrame):
        raise NotImplementedError


class EntityWrite(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="WRITE",
            signature="Entity, Any ->",
            name="Write to Entity",
            game_name="Chronicler's Gambit",
            parameters=[core.Entity, core.Iota],
            output=[],
        )
    def execute(self, frame: core.VMFrame):
        raise NotImplementedError


class EntityCanRead(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="READACCESS",
            signature="-> Bool",
            name="Entity readable",
            game_name="Auditor's Purification",
            parameters=[],
            output=[bool],
        )
    def execute(self, frame: core.VMFrame):
        raise NotImplementedError


class EntityCanWrite(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="WRITEACCESS",
            signature="-> Bool",
            name="Entity writable",
            game_name="Assessor's Purification",
            parameters=[],
            output=[bool],
        )
    def execute(self, frame: core.VMFrame):
        raise NotImplementedError