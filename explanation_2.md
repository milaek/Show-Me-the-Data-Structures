Problem 2, File Recursion:

Time complexity Analysis:
		
		For this code n must represent the total number of path elements in the given search directory (i.e all subdirectories and items contained therein)
		In both the worst case and best case scenarios we must iterate over each path element at least once to check for the desired suffix.
		Creating and appending to a list is all done in constant time O(1). 
		Os.path.join, os.path.isfile, and os.path.isdir are all also constant time O(1).
		The for loop in he find_files meathod does not iterate through all n items,
		only x number of them, where x is the number accessible in each subdirectory. However,
		find_files will recursively run z number of times, where z is the number of sub_directories accessible at any point in the given path.
		Therefore z*x will equal n, meaning our recursive use of the for loop results in O(n). 
		This gives us an overall time complexity of O(n).
	
		Space complexity is linear.

Design Choices:
		
		I chose to implement a recursive use of a for loop due to the nested nature of subdirectories. The recursive will run through all items, stopping each time it finds
		another subdirectory and recursing into it. This means we will only see each item once, which has the best time complexity. 
		Using a recursive function rather than a while loop allows us to avoid having to loop through presented items multiple times, once looking for files and then looking
		for subdirectories, and another few fdepending on the number of subdirecotries present.


	
