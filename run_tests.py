from typing import get_type_hints
from pathlib import Path
import sys

from core import *
from hexmachine import StackMachine


def load_operations(machine: StackMachine, module):
    for member_name in dir(module):
        member = getattr(module, member_name)
        if isinstance(member, type) and issubclass(member, Operation):
            machine.register_op(member())



if __name__ == "__main__":
    machine = StackMachine()

    from ops import ops_math, ops_logic, ops_stack, ops_list, ops_rw, ops_meta, ops_constants, ops_entity
    load_operations(machine, ops_math)
    load_operations(machine, ops_logic)
    load_operations(machine, ops_stack)
    load_operations(machine, ops_list)
    load_operations(machine, ops_rw)
    load_operations(machine, ops_meta)
    load_operations(machine, ops_constants)
    load_operations(machine, ops_entity)

    if not machine.strict:
        from ops import ops_extensions
        load_operations(machine, ops_extensions)

    player: Entity = Entity(
        name="Player",
        position=Vector(x=5, y=6, z=7),
        position_eyes=Vector(x=5, y=7.67, z=7),
        facing=(Vector(x=5, y=7.67, z=7) + Vector(x=9, y=7.82, z=9)).normalize(),
        velocity=Vector(x=0, y=0, z=0)
    )

    machine.player = player


    init_snapshot = deepcopy(machine.frame)

    seen = set()

    for op_key in machine.operations:
        op = machine.operations[op_key]
        if op.mnemonic in seen:
            print(f"{op_key} aliased as {op.mnemonic}\n")
            continue

        if "tests" in dir(op):
            if op_key != op.mnemonic:
                print(f"Running tests for {op_key} as {op.mnemonic} ({op.game_name}):")
            else:
                print(f"Running tests for {op.mnemonic} ({op.game_name}):")

            for idx, [desc, command, result] in enumerate(op.tests):
                print(f"{idx+1}: {desc} [ {command} ]  expects: {result}", end=" ")
                machine.frame = deepcopy(init_snapshot)
                try:
                    for token in command.split():
                        machine.process_token(token)

                    if machine.frame.stack == result:
                        print("\033[92mPASSED\033[0m")
                    else:
                        print("\033[91mFAILED\033[0m ", machine.frame.stack)
                except Exception as e:
                    print(f"\033[91mFAILED\033[0m\nEXCEPTION: {e}")
            print()

        seen.add(op.mnemonic)
                
