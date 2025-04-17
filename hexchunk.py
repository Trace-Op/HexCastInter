# ingests a hexcast file and produces a tree in the form of a linked block structure
# this can aid transcription into the game by giving reasonable sized blocks to copy.

# "1 2 3 PACKVEC 4 5 6 PACKVEC SUB DUP 0 0 0 PACKVEC EQ [ PRINT $zero PRINT DROP ] [ PRINT $not_zero PRINT DROP ] IF_ELSE"
# produces:
#  [ ("1 2 3 PACKVEC 4 5 6 PACKVEC SUB DUP 0 0 0 PACKVEC EQ", 1, 2, "IF_ELSE"),
#    ("PRINT $zero PRINT DROP"),
#    ("PRINT $not_zero PRINT DROP")
#   ]
#

from typing import List
import sys
from pathlib import Path

def parse_hexcast_blocks(tokens: List[str]):
    blocks = []

    def parse_block():
        part = []
        block = []
        while tokens:
            tok = tokens.pop(0)
            if tok == "[":
                inner_block = parse_block()
                if part:
                    block.append(" ".join(part))
                    part.clear()
                blocks.append(inner_block)
                block.append(len(blocks)-1)
            elif tok == "]":
                if part:
                    block.append(" ".join(part))
                    part.clear()
                return block
            else:
                part.append(tok)
        if part:
            block.append(" ".join(part))
            part.clear()
        return block

    blocks.append(parse_block())

    return blocks



def strip_file(path: Path):
    # remove interpreter commands and comments leaving only hexcast tokens
    out = []
    with path.open("r") as file:
        for line in file:
            if line[0] == '!':
                continue

            tokens = line.strip().split()
            for token in tokens:
                try:
                    if token[0] == '#':
                        break
                    out.append(token)
                except Exception as e:
                    print("Error:", e, file=sys.stderr)
                    return
    return out



if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = Path(".") / Path(sys.argv[1])
        tokens = strip_file(path)
    else:
        code = "1 2 3 PACKVEC 4 5 6 PACKVEC SUB DUP 0 0 0 PACKVEC EQ [ PRINT $zero PRINT DROP ] [ PRINT $not_zero PRINT DROP ] IF_ELSE"
        tokens = code.split()
    blocks = parse_hexcast_blocks(tokens)
    for idx, b in enumerate(blocks):
        print(f"{idx}: {b}")
