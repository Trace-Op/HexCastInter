#  DEF is an extension to the language and not provided in game.
#    it provides rudimentary symbol binding into a frame local dictionary

# Range ( Num: start, Num: end, Num: step -> List )
#  Create a range of numerical datapoints e.g. Range(0, 5, 1) -> [0 1 2 3 4]
$Range [
    LIST
    [
        SWAP 4 COPY WRAP CONCAT SWAP      # get start, append to list
        4 MOVE 3 COPY ADD -4 MOVE         # incr start by step
        4 COPY 4 COPY LT                  # check end < start
        1 COPY                            # copy this block
        [ DROP -3 MOVE DROP DROP DROP ]   # Clean up stack
        IF_ELSE EXEC                      # recurse
    ]
    DUP EXEC
] DEF


# Clear (... -> )
#  Remove all items from the stack
$Clear [ HEIGHT PACK DROP ] DEF


# Top (... -> Any)
#  keep only top item on the stack 
$Top [ HEIGHT PACK LISTPOP SWAP DROP ] DEF


# Map ( List: block(... -> Any), List: onto -> List)
# For Each item in onto: 
#   copy a snapshot of the stack
#   perform the operations in block
#   take the top item on the stack and append it to result
$Map [
    SWAP
    [ HEIGHT PACK LISTPOP SWAP DROP ] CONCAT  # Guard as thoth collects entire stack
    SWAP
    THOTH
] DEF