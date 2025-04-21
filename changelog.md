# Changelog
## [0.1.0] - Initial Release 2025-04-18
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