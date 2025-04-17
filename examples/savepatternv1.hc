#  example using the cache/Ravenmind as a sideeffect to aid in data access
#  placed in a rewritable item such as a Focus LD/ST allow data to persist between executions

#  run
[
	LD CACHE  # place program into cache

	PLAYER TO_POS PLAYER TO_FACING RAYCAST_BLOCK  # get position of a block
	DUP
	BOOL
	[ # true, we hit something
		UNCACHE DUP LEN 3 SUB SEL  	   # copy saved Anchor Position
		BOOL
		[  # is truthy (Vector)
			UNCACHE DUP LEN 3 SUB SEL  # copy anchor position
			SUB                        # calculate Vector(hitPos - anchor)
			UNCACHE DUP LEN 1 SUB SEL  # copy storage List
			SWAP WRAP CONCAT           # append to list
			UNCACHE DUP LEN 1 SUB      # stack: [[new_list], [prog], [idx]]
			ROTATE_RIGHT SET           # set new data into prog
			CACHE                      # place modified prog into cache
		]
		[  # is falsy (Null)
			UNCACHE DUP LEN 3 SUB      # stack: [hitPos, [prog], idx]
			ROTATE_RIGHT SET           # set anchor pos data into prog
			PLAYER TO_POS PLAYER TO_FACING RAYCAST_NORMAL
			# get normal at hit position. execution acts in single tick, no check/use contention
			SWAP DUP LEN 2 SUB         # stack: [hitNormal, [prog], idx]
			ROTATE_RIGHT SET		   # set anchor normal into prog
			CACHE
		]
		IF_ELSE EXEC
	]
	[ # false, raycast returned Null
		DROP                           # drop the null, copy cache to match sig of true block
	]
	IF_ELSE EXEC
	UNCACHE ST                         # write modified program ready for next invoke
	HALT
]

#  data store
NULL APPEND  # idx: LEN-3: Anchor Position. Vector
NULL APPEND  # idx: LEN-2: Anchor Normal. Vector
LIST APPEND  # idx: LEN-1: block pattern offsets. List[Vector...]