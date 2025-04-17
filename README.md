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


This project is still very much a work in progress.
Stack objects are still mostly python types.
Not all glyphs/operations are implemented. I've done my best to make sure most reflect their in-game behavior when given the right arguments on the stack.
The Garbage object is not implemented yet so failures do not match game behavior.

### Roadmap
- [ ] unit test harness for operations
- [ ] stricter type checking on stack operations
- [ ] include documentation on operations more than simple input->output
- [ ] tree mapping and static analysis tooling
- [ ] templating engine to link up hexcast scripts
- [ ] glyph drawing to make transcribing in the game less painful
- [ ] an entity management system to help debug those raycasting and environment interaction spells
- [ ] meta operations "Iris' Gambit" and "Thanatos' Reflection"
- [ ] late game operations such as the Akashic Library