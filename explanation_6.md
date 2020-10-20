Problem 6, Union and Intersection of Two Linked Lists
	Time Complexity Analysis:
		The node class init runs in constant time, as does the LinkedList init.
		Within the linked list, all functions run in constant time except for the print function,
		which must iterate through every item in the linked list in order to print it.
		This gives us O(n) for any printing of a linked list.

		The union function calls the ll_to_dict function which creates a dictionary
		from a linked list by iterating through all items. If passed a dictionary it will
		check for the key each time, which does not increase runtime past O(1)
		However, the iteration through all items means this is O(n) each time the function is called.
		where n is the number of items in the list. 
		The union function calls this same transfer function twice, which leaves us with O(2n).
		Then we iterate through all items in the dictionary to create the new unified list, adding another
		O(n). However, this can all be simplified down to an overall O(n).

		The intersection function uses the same two calls and final dictionary iteration that the union
		function does. The only difference is checking the value of the pulled key during the final iteration.
		This is a constant time action, and therefore the overall time complexity of this function is no different
		to the union function, which gives us O(n)
		Space complexity is linear.
	Design Choice:
		Implementing a simple dictionary and value check in for use in both the union and intersection functions
		cut down on potential looping to create set's or check for duplicates. It also means that the 
		majority of the code can be shared between the two functions via the helper function. 

		I also chose to add both a length value and a tail value to the linked list to allow for faster appending
		and size checking, at the cost of ony a few lines of code and tracking length durring appends.
