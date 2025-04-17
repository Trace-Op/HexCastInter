# emits a program to be loaded onto a rewritable item
#   when executed transforms a state variable to store anchor and normal vectors on first invocation
#   subsequent invocations append to a pattern list

#   v2 try at this structure. We cache just a list of a global env and jump to main
#      afterwards we take the env and save it back into the item

# _start
[
    LD DUP LEN 1 SUB SEL CACHE  # get a copy of program, load env into cache

    UNCACHE 1 SEL EXEC          # main()
    DROP                        # keep it simple, not checking status code, saving anyway

    LD DUP LEN 1 SUB            # save env back into item
    UNCACHE SET ST

    HALT                        # sentinel to keep from trying to execute env
]

#  section: env
LIST

# 0: prev_state: [anchor_pos: Vector, anchor_normal: Vector, pattern: List[Vector] ]
LIST APPEND  # emit uninitialized list

# 1: main (-> int) effects: env.prev_state modified on success.
[
    UNCACHE 3 SEL EXEC                 # doRaycastBlock()
    DUP BOOL
    [  # got a hit
        UNCACHE 0 SEL                  # get prev_state
        UNCACHE 2 SEL EXEC             # updatePattern()
        UNCACHE SWAP 0 SWAP SET CACHE  # set prev_state to state'
        0
    ]
    [  # got a null
        DROP  # drop the null
        -1
    ]
    IF_ELSE EXEC
] APPEND

 # 2: updatePattern (vector, state -> state')
[
    DUP BOOL
    [  # True (list populated): state initialized
        # append arg vector to state.pattern
        2                #  place 2 on stack
        1 COPY 2 SEL     #  place copy of state.pattern on stack
        3 MOVE           #  move arg vector to top
        3 COPY 0 SEL     #  place copy of state.anchor_pos on stack
        SUB APPEND SET   #  calculate offset, append to pattern, set new pattern in state
    ]
    [  # False (list empty): state empty
        # initialize state
        SWAP APPEND                # append arg vector
        UNCACHE 4 SEL EXEC APPEND  # DoRaycastNormal(), append normal vector
        LIST APPEND                # append empty pattern list
    ]
    IF_ELSE EXEC
] APPEND

# 3: doRaycastBlock (-> Vector) effects: read player entity and raycast from game
[
    PLAYER TO_POS PLAYER TO_FACING RAYCAST_BLOCK
] APPEND

# 4: doRaycastNormal (-> Vector) effects: read player entity and raycast from game
[
    PLAYER TO_POS PLAYER TO_FACING RAYCAST_NORMAL
] APPEND

APPEND  # end section: env