# for testing
import sys


#      CLASSES     #
class Node:
    """A node to be used  in our Huffman encoding.
    IN: weight(frequency) of symbol, (optional) symbol to be encoded
    """
    def __init__(self, weight, symbol=None):
        self.symbol = symbol
        self.weight = weight
        self.left_child = None
        self.right_child = None

    def has_left_child(self):
        if self.left_child is None:
            return False
        return True

    def has_right_child(self):
        if self.right_child is None:
            return False
        return True

    def is_leaf(self):
        if self.has_left_child() or self.has_right_child():
            return False
        return True


class Tree:
    """A tree data structure
    """
    def __init__(self, root=None):
        self.root = root

    def find_leaf_routes(self):
        """Helper function that Returns paths to all leaves
        IN: root node of tree
        OUT: Dictionary where keys are single symbols and values are the paths to them
        """
        root = self.root

        def leaf_recursion(node):
            output = {}
            # base case
            if node.is_leaf():
                # set a key as the leaf's symbol, value will later become the path taken
                output[node.symbol] = ""
                return output

            # recursive call left side (0)
            for key, value in leaf_recursion(node.left_child).items():
                value = "0" + value
                output[key] = value
            # recursive call right side (1)
            for key, value in leaf_recursion(node.right_child).items():
                value = "1" + value
                output[key] = value
            # return dict of symbols/paths
            return output
        # back to og function
        # call recursive on root and return dict
        return leaf_recursion(root)


# noinspection PyMethodMayBeStatic
class MinHeap:
    """
    A Binary Heap, Min Heap
    """
    def __init__(self):
        self.heap = []

    # value helper
    def length(self):
        return len(self.heap)

    # get indexes
    def parent_index(self, index):
        return (index - 1) // 2

    def left_child_index(self, index):
        return 2 * index + 1

    def right_child_index(self, index):
        return 2 * index + 1

    def get_children(self, parent_i):
        l_child_i = self.left_child_index(parent_i)
        r_child_i = self.right_child_index(parent_i)
        if self.length()-1 >= l_child_i:
            l_child = self.heap[l_child_i]
            if self.length()-2 >= r_child_i:
                r_child = self.heap[r_child_i]
            else:
                r_child = None
        else:
            l_child = None
            r_child = None
        return l_child, r_child

    # greater functions
    def insert(self, node):
        """Adds a node to our MinHeap, and re-balances to account for it
        IN: Node to add
        """
        # add new node to heap
        self.heap.append(node)
        # edge case for beginning the MinHeap
        if self.length() > 1:
            self.insertion_balance()

    def insertion_balance(self):
        # grab the current index, and both the index and node of parent for shuffling needs
        child_i = self.length()-1
        parent_i = self.parent_index(child_i)
        parent = self.heap[parent_i]
        child = self.heap[child_i]
        # reshuffle the MinHeap
        while child.weight > parent.weight:
            # swap node's index assignments
            self.heap[child_i] = parent
            self.heap[parent_i] = child
            child_i = parent_i
            parent_i = self.parent_index(child_i)
            # prep for next loop
            parent = self.heap[parent_i]
            child = self.heap[child_i]

    def extract(self):
        # get and hold the item you want to return at the end
        extracted_item = self.heap[0]
        # replace the head of the array with the last array item, and shrink array to reflect new size
        node = self.heap[-1]
        self.heap[0] = node
        self.heap = self.heap[:-1]
        # edge case final loop
        if self.length() != 0:
            self.extraction_balance()
        # return the extracted value
        return extracted_item

    def extraction_balance(self):
        # setup for trickle down looping
        parent_i = 0
        l_child_i = self.left_child_index(parent_i)
        r_child_i = self.right_child_index(parent_i)
        parent = self.heap[parent_i]
        l_child, r_child = self.get_children(parent_i)

        # trickle down loop to re-balance MinHeap
        while l_child is not None and parent.weight > l_child.weight:
            # right takes priority for weight balancing
            if r_child is not None and parent.weight > r_child.weight:
                swap_child = r_child
                swap_child_i = r_child_i
            else:
                swap_child = l_child
                swap_child_i = l_child_i
            # swap values
            self.heap[parent_i] = swap_child
            self.heap[swap_child_i] = parent
            # set values for next loop
            parent_i = swap_child_i
            l_child_i = self.left_child_index(parent_i)
            r_child_i = self.right_child_index(parent_i)
            parent = self.heap[parent_i]
            l_child, r_child = self.get_children(parent_i)


#     FUNCTIONS    #
def huffman_encoding(data):
    """Function to encode data using the Huffman method
    IN: data to be encoded
    OUT: code, tree made during encoding
    """
    # edge case of empty data
    if data == "" or data is None:
        return None, None
    # set external vars
    char_freq_dict = {}
    # get frequencies of all symbols in data
    for char in data:
        if char_freq_dict.get(char) is None:
            char_freq_dict[char] = 1
        else:
            char_freq_dict[char] += 1

    # turn dict info into min heap arr
    priority_heap = MinHeap()
    for key, value in char_freq_dict.items():
        new_node = Node(value, key)
        priority_heap.insert(new_node)

    # edge case of only one character in data string
    if priority_heap.length() == 1:
        # inserts a dummy blank node so at least one path will exist for encoding
        priority_heap.insert(Node(0))
    #  while len of items > 1, merge the two items with the lowest weight(frequency)
    while priority_heap.length() >= 2:
        smallest_one = priority_heap.extract()
        smallest_two = priority_heap.extract()
        new_node = Node(smallest_one.weight + smallest_two.weight)
        # make the two items the children of the new item in the Tree
        if smallest_one.weight <= smallest_two.weight:
            new_node.left_child = smallest_one
            new_node.right_child = smallest_two
        else:
            new_node.left_child = smallest_two
            new_node.right_child = smallest_one
        # add the new node back into the priority heap to be further considered
        priority_heap.insert(new_node)

    # make the final node in priority heap the root of a tree object
    huff_tree = Tree(priority_heap.extract())
    # convert the data stored in this new huff tree into a dictionary for encoding
    encoding_dictionary = huff_tree.find_leaf_routes()
    # encode each letter from the original string, using the dict created
    code = ""
    for char in data:
        code += encoding_dictionary[char]
    # return encoded string and the tree used for encoding
    return code, huff_tree


def huffman_decoding(data, tree):
    """Function to decode a huffman encoded item
    IN: the encoded Huffman data, the tree used for the encoding
    OUT: decoded string
    """
    if data is None and tree is None:
        return None
    # set root variable
    if isinstance(tree, Tree):
        root = tree.root
    else:
        root = tree
    # convert data to a string for looping purposes, set other external variables
    data = str(data)
    node = root
    decoded = ""

    # loop through encoded data, following its directions through provided tree.
    for num in data:
        # if num is 0 traverse left
        if int(num) == 0:
            node = node.left_child
        # if num is not 0, num must be 1, which means traverse right
        else:
            node = node.right_child
        # if this new node is a leaf, append symbol to string and return to head of tree for next round
        if node.is_leaf():
            decoded += node.symbol
            node = root

    # return decoded string
    return decoded


#    TESTING    #
if __name__ == "__main__":
    codes = {}

    a_great_sentence = str(input("What would you like to encode?\n"))
    while a_great_sentence is None:
        a_great_sentence = str(input("Please input something.\n"))

    print("\nThe size of the incoming data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the incoming data is: {}\n".format(a_great_sentence))

    encoded_data, h_tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    yes_no = str(input("Would you like to run the decoding process?\n")).lower()[0]
    while yes_no != "y" and yes_no != "n":
        yes_no = str(input("Please answer yes or no")).lower()[0]
    if yes_no == "y":
        decoded_data = huffman_decoding(encoded_data, h_tree)

        print("\nThe size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the decoded data is: {}\n".format(decoded_data))
    else:
        print("Ok, have a nice day")
