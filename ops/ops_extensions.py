from typing import Tuple
import core
from core import VMFrame


class Define(core.Operation):
    def __init__(self):
        super().__init__(
            mnemonic="DEF",
            signature="Literal, List -> ",
            name="Define",
            game_name="NONE (Language extension)",
            parameters=[str, Tuple],
            output=[]
        )
    def execute(self, frame: VMFrame):
        block = frame.stack.pop()
        name = frame.stack.pop()
        if not isinstance(name, str):
            raise ValueError("DEF: name must be a string literal")
        if not isinstance(block, tuple):
            raise ValueError("DEF: block must be a List")
        frame.user_definitions[name] = block