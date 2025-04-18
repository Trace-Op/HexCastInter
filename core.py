from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Literal, Protocol, Tuple, Union
from numbers import Number

from copy import deepcopy

from iota.Vector import Vector
from iota.Entity import Entity

Iota = Union[bool, None, Number, str, Tuple, Vector, Entity]

@dataclass
class VMFrame:
    machine: Any
    stack: List[Iota] = field(default_factory=list)
    scratch: Iota = None
    hand: Iota = None
    hand_mode: Literal["r", "w", "rw"] = "rw"
    user_definitions: Dict[str, tuple[str]] = field(default_factory=dict)
    quote_buffer: List[str] = field(default_factory=list)
    quote_depth: int = 0
    player: ["Entity" , None] = None

    def __deepcopy__(self, memo):
        # override since we don't want secondary instances of the parent machine in saved states
        new = VMFrame(
            self.machine,
            deepcopy(self.stack, memo),
            deepcopy(self.scratch, memo),
            deepcopy(self.hand, memo),
            self.hand_mode,
            deepcopy(self.user_definitions, memo),
            self.quote_buffer.copy(),
            self.quote_depth,
            deepcopy(self.player, memo),
        )
        return new


@dataclass
class Operation:
    mnemonic: str
    signature: str
    name: str
    game_name:str
    parameters: List[Iota]
    output: List[Iota]

    def execute(self, frame: VMFrame):
        raise NotImplementedError()

    def infer_output_type(self, args: list):
        return self.output.copy()

