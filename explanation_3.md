Problem 3, Huffman Coding:
	Time Complexity Analysis:
		Let L represent the length of the passed string, and m represent the number of distinct characters present.
		All functionality in the Node class is set internally and runs at O(1).
		In the encoding funtion we must visit each character present in the input string, which gives us O(l).
		We then must loop through all distinct characters stored previously (m) and insert them into a heap:
		Heap insertion runs at worst case O(n log n) where h is the number of items in the heap. 
		This makes our heap setup loop run at O(m*(nlogn). This can simplify to O(nlogn) as that takes complexity precedence.
		We then iterate through the priority heap taking the two smallest items from the heap at O(nlogn) each time,
		making them the children of a new node, and inserting said new node which adds another O(nlongn).
		Though we will iterate through this process some x number of times, the complexity will simplify down to
		O(nlogn). We then set the last node as the root of a tree which takes constant time.
		We must then run through a recursive function find_leaf_routes, which at worst case will take O(m) 
		(each leaf represents a distinct character from previous).
		We then loop through the original string a final time for O(h).
		Simplifying down basic multiplications we have O(L + nlogn + m). 
		Finally, we can simplify out the lower values, which leaves us with a Time complexity of O(nlogn).

		The decoding process is much simpler and will only run L number of constant time actions, where L is the length of 
		the given Huffman Code, which gives us O(L). 

		Of the two functions, endcoding has a higher runtime analasys, so we can simplify out the decoding runtime
		if we are looking at runnong them back-to-back.

		We are therefore left with a runtime of O(nlogn) for the encoding to decoding process.
		
		Space complexity is Linear
		

	Design Choices:
		For this problem I chose to implement a MinHeap as the priority queue used in the encoding process.
		This was due to the large number of reshuffles that needed to occur which made other types
		of priority queues not as time efficient. The MinHeap is set up to shuffle for minimum value many times
		efficiently. I also chose to use the python library's heapq library for the basic functionality of
		my MinHeap. Some slight changes were made using an external class to pass and pull heapq acceptable values.
		