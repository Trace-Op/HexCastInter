from typing import get_type_hints
from pathlib import Path
import sys

from core import *
from hexmachine import StackMachine



def run_command(machine: StackMachine, line: str):

    def _load(args: list):
        path = Path(".") / Path(args[0])
        if path.is_file():
            run_file(machine, path)
        else:
            print(f"{path} not found")

    def _echo(args: list):
        print(" ".join(args))

    def _nop(args):
        pass

    def _savestate(args):
        machine.savestates[args[0]] = deepcopy(machine.frame)

    def _loadstate(args):
        machine.frame = deepcopy(machine.savestates[args[0]])

    def _help(args):
        if len(args) == 0:
            for key in commands:
                _, parameters, desc = commands[key]
                out = f"!{key} {parameters}"
                out += " "*(20 - len(out)) + f"- {desc}"
                print(out)
        else:
            key = args[0].upper()
            op = machine.operations.get(key, None)
            if op:
                print(f"{op.mnemonic} ({op.signature}): {op.game_name}")
        print()

    def _ops(args):
        for key in machine.operations:
            op = machine.operations[key]
            out = f"{key} ({op.signature})"
            out += " "*(65 - len(out)) + f"{op.game_name}"
            print(out)

    def _verbose_exec(args):
        if len(args) != 1:
            return
        if args[0] == "set":
            machine.verbose_exec = True
        elif args[0] == "clear":
            machine.verbose_exec = False

    commands = {
        "echo": (_echo, "string", "echo a string to stdout"),
        "load": (_load, "filename", "execute a hexcast file"),
        "savestate": (_savestate, "name", "store a savestate of the machine frame"),
        "loadstate": (_loadstate, "name", "recover a savestate"),
        "help": (_help, "[operation]", "print a list of commands, or gets a description of an operation"),
        "ops": (_ops, "", "print a list available operations"),
        "verbose": (_verbose_exec, "set|clear", "when set, exec will print every operation"),
        "quit": (_nop, "", "exits the repl")
    }

    if line[0] != '!':
        raise RuntimeError("Invalid command line")
    cmd, *args = line[1:].split()

    if cmd == "quit":
        return True
    else:
        commands.get(cmd, _nop)[0](args)




def format_stack(stack: get_type_hints(VMFrame)['stack']) -> str:
    buf = []
    for idx, item in enumerate(reversed(stack)):
        buf.append(f"{idx}: {item}")
    return "\n".join(buf)


def repl(machine: StackMachine):
    print("Stack Machine REPL. Type '!quit' to quit or '!help' for a list of commands")
    while True:
        if machine.frame.quote_depth > 0:
            print(f"Quote Depth: {machine.frame.quote_depth}")
            print(f"Quote: {machine.frame.quote_buffer}")
        print("Stack:")
        print(format_stack(machine.frame.stack))
        line = input("^_^ ").strip()

        if not line:
            continue

        if line[0] == '!':
            terminate = run_command(machine, line)
            if terminate:
                return
            continue

        tokens = line.split()

        try:
            for token in tokens:
                machine.process_token(token)
        except Exception as e:
            print("Error:", e, file=sys.stderr)


def load_operations(machine: StackMachine, module):
    for member_name in dir(module):
        member = getattr(module, member_name)
        if isinstance(member, type) and issubclass(member, Operation):
            machine.register_op(member())


def run_file(machine, path: Path):
    with path.open("r") as file:
        for line in file.readlines():
            if line[0] == '!':
                cond = run_command(machine, line)
                if cond:
                    return
                continue

            tokens = line.strip().split()
            for token in tokens:
                try:
                    if token[0] == '#':
                        break
                    machine.process_token(token)
                except Exception as e:
                    print("Error:", e, file=sys.stderr)
                    return


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


    if len(sys.argv) > 1:
        path = Path(".") / Path(sys.argv[1])
        run_file(machine, path)

    repl(machine)