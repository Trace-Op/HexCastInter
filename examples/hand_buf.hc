# Process Env Emulator
#   Provides a boilerplate for more useful programs to be written.
#   The Stack is initialized with a list of utility routines that can be executed with
#   the Call operation, an example of it's expanded usage is given in Push
#   Data can be saved between executions to the Storage position in this list using
#   the provided Load and Store. This is essentially rewriting the device to initialize in a new state.

# This file builds the process object and saves it to the hand buffer
#  TypeProcessObject: [ bootstrap, ..., HALT, [entry] [func_table] [storage] ]

# SECTION bootstrap
[
    LD DUP LEN 2 SUB SEL  # place function table
    LD DUP LEN 3 SUB SEL  # place entry block

    # user definitions
    $Call [ HEIGHT 1 SUB COPY SWAP SEL EXEC ] DEF        # Call(Num: index, ...) -> Any?
    $Clear [ HEIGHT PACK DROP ] DEF

    # begin execution
    EXEC HALT
]


# SECTION entry
[
    # your program code here
]
WRAP CONCAT


# SECTION function table: bootstrap will load this at bottom of stack
[
# 0: Load ( -> List ) Copy storage to top of stack
    [ LD DUP LEN 1 SUB SEL ]

# 1: Store ( List -> ) Place item at top of stack into storage
    [ LD DUP LEN 1 SUB ROTATE_RIGHT SET ST ]

# 2: Push ( Any -> ) append item at top of stack to list in storage
    [
        0 HEIGHT 1 SUB COPY SWAP SEL EXEC        # Call(0)
        SWAP WRAP CONCAT                        # append
        1 HEIGHT 1 SUB COPY SWAP SEL EXEC        # Call(1, modified_list)
    ]

# 3: N_Loop ( Num: count, List: block -> ) Execute the patterns in List N times.
#        DANGER! Assumes stack is not modified during block's call
    [
        SWAP DUP 0 EQ                                  # check counter
        [ DROP DROP ]                                  # no more runs, clean up stack
        [
            SWAP DUP EXEC                              # run block parameter
            SWAP 1 SUB SWAP                            # decrement counter
            3 HEIGHT 1 SUB COPY SWAP SEL EXEC    # recurse
        ]
        IF_ELSE EXEC                                   # select and execute branch
    ]

# 4: Range ( Num: start, Num: end, Num: step -> List )
#        Create a range of numerical datapoints e.g. Range(0, 5, 1) -> [0 1 2 3 4]
    [
        LIST                                 # create new list
        [
            SWAP 4 COPY WRAP CONCAT SWAP     # get start, append to list
            4 MOVE 3 COPY ADD -4 MOVE        # incr start by step
            4 COPY 4 COPY LT                 # check end < start
            1 COPY                           # copy this block
            [ DROP -3 MOVE DROP DROP DROP ]  # Clean up stack
            IF_ELSE EXEC                     # recurse
        ]
        DUP EXEC
    ]
]
WRAP CONCAT

# SECTION storage
[
    # Your env data here
]
WRAP CONCAT

# and store
ST