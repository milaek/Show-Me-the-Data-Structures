Problem 5, Block Chain:
	Time Complexity Analysis:
		The block class and all of its internal functions run in cosntant time.
		In the LinkedBlockList class, the init, craft new block, append, and delete functions
		all run in constant time, as they all pull specific keys from the dictionary.
		and point to the previous block within their own variables.
	
		In the LinkedBlockList class, the to_list fucntion (used only for printing) must 
		recursively iterate through all blocks and building a list from the head down. This is done in
		O(n) time, since each output list it built upon the previous without looping through the items again.

		Therefore, the runtime of the testing code provided is O(n).
		Used without printing the blockchain, you have a runtime of O(1)
		Space complexity is linear
	Design Choice:
		The main esign choice here was to use a recursive function to aid in printing
		a visualisation of the blockchain. A while loop would have required pre-appending
		to a list, which would have forced an added iteration and slightly increased runtime.

		I also chose to include a delete_tail functionality to the BlockListChain class allow for the 
		final value to be removed.
		I considered adding a function to remove specified blocks in the chain, but realised that would go
		against the purpous of a blockchain, and decided against it. 