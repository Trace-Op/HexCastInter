# HexCastInter
An interpreter for a language based on the HexCasting minecraft mod.


A side project to create a more human readable environment for testing glyphcode.

The main REPL environment is hexcaster.py and can be launched with an optional relative filepath to a .hc script
```sh
python hexcaster.py [file]
```

### Idioms:
- '[' and ']' behave like the quoting system in game "Introspection" and "Retrospection"
- '$' is equivelent to "Consideration" and will place a string litteral on the stack
- '!' at the start of the line is used for repl commands
- '#' denotes a comment in files, any characters after '#' will be ignored


### Evaluation Model:
Hexcasting Mod uses a direct evaluation model where tokens are drawn as glyphs and immediatly evaluated.
HexCastInter follows the same pattern, glyphs other than numbers are written as string litteral and processed directly by the stack machine.
as such the line:
```
4 5 ADD [ 6 7 8 ]
```
places 4 and 5 on the stack, performs the add operation (popping 4 and 5, pushing 9),
starts a quote, adds the strings '6' '7' '8', ends the quote and pushes the quote to the stack.
at the end of this sequence the stack is [9, ('6', '7', '8',)]

### Project Status:
This project is still very much a work in progress.
Not all glyphs/operations are implemented. A list of of operations available can be found using the command "!ops"
I've done my best to make sure most reflect their in-game behavior when given the right arguments on the stack.
Mishap/Garbage support is incomplete.

### Roadmap
- [x] unit test harness for operations
- [ ] stricter type checking on stack operations
- [ ] include documentation on operations more than simple input->output
- [ ] tree mapping and static analysis tooling
- [ ] templating engine to link up hexcast scripts
- [ ] glyph drawing to make transcribing in the game less painful
- [ ] an entity management system to help debug those raycasting and environment interaction spells
- [ ] meta operations "Iris' Gambit" and "Thanatos' Reflection"
- [ ] late game operations such as the Akashic Library