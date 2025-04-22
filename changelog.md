# Changelog

## [0.1.2] - 2025-04-22
### Features
* Added `EXP` with alias `PROJECT`. provides support for numeric exponentiaion and vector projection. "Power Distillation".
* Added math operations `FLOOR`, `CIEL`, `MOD`.
* `iota.Vector.__pow__` implements scalar broadcasts.
* `iota.Vector.__mod__` implements scalar broadcasts.

### Testing
* Test cases for `SUB`, `MUL`, `DIV`, `ABS`, `PACKVEC`, `UNPACKVEC`, `EXP`, `FLOOR`, `CEIL`, and `MOD`.

### Changed
* Added `DOT` and `CROSS` aliases for `MUL` and `DIV` to aid readability of vector pipelines.
* Removed `BOOLTONUM` and `LEN` operations. Aliases of `ABS`

### Fixed
* Corrected scalar broadcasts for iota.Vector under non-commutative operations `SUB` and `DIV`.
* Bool type gaurds on math operations that expect Numbers.


## [0.1.1] - 2025-04-21
### Features
* Added alias field to core.Operation and support for mnemonic overloading.
* Added Garbage Iota type for invalid stack states.

### Testing
* Operation testing harness run_tests.py 
* test cases for ADD

### Changed
* Removed CONCAT as an operation. CONCAT is now aliased in ADD to reflect the overloading of "Additive Distillation" in game.
* Improved string representations for iota.Vector.
* Include equality check for iota.Vector types.
* ADD now correctly handles stack underflows and type mismatches.

### Fixed
* Bugfix: StackMachine now checks user definitions first before checking builtins when ingesting tokens.


## [0.1.0] - Initial Release 2025-04-18