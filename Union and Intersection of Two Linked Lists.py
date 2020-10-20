#    HELPER FUNCTIONS    #
def ll_to_dict(linked_list, incoming_dictionary=None):
    """
    Turns every item in a linked list into a dictionary entry, where the value is the key and the
    num repetitions is the val
    :param incoming_dictionary: dictionary to add too. if none is given, creates a new dictionary
    :param linked_list: Linked list of values to add to dictionary
    :return: dictionary a dictionary of node values paired with intersection status
    """
    if incoming_dictionary is None:
        dictionary = dict()
    else:
        dictionary = incoming_dictionary.copy()
    node = linked_list.head
    while node is not None:
        if node.value not in dictionary:
            dictionary[node.value] = False
        if incoming_dictionary is not None and node.value in incoming_dictionary:
            dictionary[node.value] = True
        node = node.next
    return dictionary


#    CLASSES    #
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        self.length += 1
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        node = Node(value)
        self.tail.next = node
        self.tail = node

    def size(self):
        return self.length


#    MAIN FUNCTIONS    #
def union(list_1, list_2):
    """
    :param list_1: one of two linked lists to unify
    :param list_2: one of two linked lists to unify
    :return: linked list of set of all values from both lists
    """
    # check for empty list being passed
    if list_1.head is None:
        union_dict = None
    else:
        union_dict = ll_to_dict(list_1)
    # check for empty list being passed
    if list_2.head is not None:
        union_dict = ll_to_dict(list_2, union_dict)
    # edge case of both passed lists being empty
    if union_dict is None:
        return None

    unified_list = LinkedList()
    for node_val in union_dict.keys():
        unified_list.append(node_val)
    return unified_list


def intersection(list_1, list_2):
    """
    :param list_1: one of two linked lists to check intersection of
    :param list_2: one of two linked lists to check intersection of
    :return: linked list of all intersecting values
    """
    # check for empty list 1
    if list_1.head is None:
        intersect_dict = None
    else:
        intersect_dict = ll_to_dict(list_1)
    # check for empty list 2
    if list_2.head is not None:
        intersect_dict = ll_to_dict(list_2, intersect_dict)
    # edge case of two empty lists being passed
    if intersect_dict is None:
        return None

    intersect_list = LinkedList()
    for node_val, appears_in_both in intersect_dict.items():
        if appears_in_both:
            intersect_list.append(node_val)
    return intersect_list


#    TESTS    #
# Test case 1
print("Test One")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

union_1 = union(linked_list_1, linked_list_2)
print(f"\tExpecting: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->")
print(f"\tGot:       {union_1}")

intersection_1 = intersection(linked_list_1, linked_list_2)
print(f"\tExpecting: 4 -> 6 -> 21 -> ")
print(f"\tGot:       {intersection_1}")

# Test case 2
print("Test Two")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
for i in element_1:
    linked_list_4.append(i)

union_2 = union(linked_list_3, linked_list_4)
print(f"\tExpecting: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> ")
print(f"\tGot:       {union_2}")

intersection_2 = intersection(linked_list_3, linked_list_4)
print(f"\tExpecting:")
print(f"\tGot:       {intersection_2}")

# test case 3
print("Test Three")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

union_3 = union(linked_list_5, linked_list_6)
print(f"\tExpecting: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> ")
print(f"\tGot:       {union_3}")

intersection_3 = intersection(linked_list_5, linked_list_6)
print(f"\tExpecting:")
print(f"\tGot:       {intersection_3}")
