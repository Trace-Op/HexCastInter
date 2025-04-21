from typing import Dict
import sys

import core
from core import *
from copy import deepcopy


class StackMachine:
    def __init__(self, **kwargs):
        self.frame = VMFrame(self)
        self.operations: Dict[str, core.Operation] = {}
        self.debug = kwargs.get("debug", True)
        self.strict = kwargs.get("strict", False)
        self._history = []
        self.savestates: Dict[str, VMFrame]  = {}
        self.verbose_exec = True

    @property
    def history(self):
        return self._history.copy()

    @history.setter
    def history(self, val):
        raise TypeError("StackMachine.history is read only")

    @property
    def player(self):
        return deepcopy(self.frame.player)

    @player.setter
    def player(self, e):
        self.frame.player = deepcopy(e)


    def register_op(self, op: Operation):
        self.operations[op.mnemonic] = op
        for alias in op.alias:
            self.operations[alias] = op

    def execute(self, instr):
        debug = self.debug
        prev_frame = None
        if debug:
            prev_frame = deepcopy(self.frame)
            self._history.append(instr)
        try:
            if instr in self.frame.user_definitions:
                for token in self.frame.user_definitions[instr]:
                    self.process_token(token)
            elif instr in self.operations:
                self.operations[instr].execute(self.frame)
            else:
                raise ValueError(f"Unknown instruction: {instr}")
        except Exception as err:
            print(f"Error: {err}", file=sys.stderr)
            if debug:
                if prev_frame is None:
                    raise RuntimeError("Saved frame was None")
                self.frame = prev_frame
                self._history.append("***")
            raise err

    def process_token(self, token: str):
        token = token.upper()
        # Quoting mode
        if self.frame.quote_depth >= 1:
            if token == "[":
                self.frame.quote_depth += 1

            if token == "]":
                self.frame.quote_depth -= 1

            if self.frame.quote_depth == 0:
                quoted = tuple(self.frame.quote_buffer)
                self.frame.quote_buffer = []
                self.frame.stack.append(quoted)
            else:
                self.frame.quote_buffer.append(token)
            return

        # Start quote
        if token == "[":
            self.frame.quote_depth += 1
            return

        # Literals
        if token[0] == "$":
            self.frame.stack.append(token[1:])
        elif token.lstrip('-').isdigit():
            self.frame.stack.append(int(token))
        else:
            try:
                self.execute(token)
            except Exception as err:
                raise RuntimeError(f"Error processing token or command: {token}, {err}")