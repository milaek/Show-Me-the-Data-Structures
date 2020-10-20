Problem 4, Active Directory:
	Time Complexity Analysis:
		Adding users and groups runs in constant time.
		Cheking if a user is in a group also runs in constant time due to the use
		of a dictionary as the holder for all groups and users. 
		Thereofore the only variant in time is the depth of subgroups it must traverse.
		This gives us O(n), where n is the groups contained within the given group and 
		all its subgroups
		Space complexity is linear
	Design Choices:
		I chose to edit the group class and change the containers for groups and users to 
		dictionaries. This drops the runtime significantly by reducing the need to iterate
		through all items in each group, only available groups.
		Otherwise, the is_user_in_group function is a simple recursive function. 
		I chose this over a while loop to better handle the possibility of a group or subgroup
		to have multiple subgroups within. 