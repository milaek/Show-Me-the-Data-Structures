Problem 1, Least Recently Used Cache:
	
Time complexity Analysis:
		
		Adding to, removing from, getting keyed values from, and move_to_end in an OrderefDict
		all take constant time. Calling the len() function is also constant time. Therefore
		the time complexity is O(1)
		
		The space complexity is linear until 5 items are in the memory.


Design Choices:
		
		I chose to use an ordered dictionary for referecing and holding the values since the lookup 
		time is constant. It allso allows for standard LRU cache functionatily to be done in constant time.