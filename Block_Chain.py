import hashlib
import datetime
from datetime import timezone


def get_timestamp():
    # Getting the current date and time
    dt = datetime.datetime.now()

    utc_time = dt.replace(tzinfo=timezone.utc)
    utc_timestamp = utc_time.timestamp()
    return utc_timestamp


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp)+str(self.data)+str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class LinkedBlockList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.lookup_registry = {}

    def craft_new_block(self, data, previous_hash):
        """
        helper function that collects all info and creates the new block
        :param data: data to store in block
        :param previous_hash: the hashcode of the previous block in the chain
        :return:
        """
        timestamp = get_timestamp()
        new_block = Block(timestamp, data, previous_hash)
        self.lookup_registry[new_block.hash] = new_block
        return new_block

    def append(self, data):
        """
        Adds data to the end of the block chain
        :param data: data to store in block
        :return: None
        """
        # edge case first item in list
        if self.length == 0:
            new_block = self.craft_new_block(data, 0)
            self.length = 1
            self.head = new_block
            self.tail = new_block
            return

        previous_hash = self.tail.hash
        new_block = self.craft_new_block(data, previous_hash)
        self.tail = new_block
        self.length += 1

    def delete_tail(self):
        if self.length > 0:
            self.length -= 1
            # edge case for deleting last item in block chain
            if self.length == 0:
                self.head = None
                self.tail = None
                return
            # standard tail replace
            self.tail = self.lookup_registry[self.tail.previous_hash]

    def to_list(self, block):
        """
        turns the block chain into a list for printing purposes
        :param block: tail of the block chain
        :return: a list representing the block chain using its data
        """

        # edge case of an empty blockchain
        if block is None:
            return []

        # end case
        if block == self.head:
            output = [block.data]
            return output

        previous_block = self.lookup_registry[block.previous_hash]
        output = self.to_list(previous_block)
        output.append(block.data)
        return output

    def __repr__(self):
        s = str(self.to_list(self.tail))
        return s


#   TESTING    #
myList = LinkedBlockList()
myList.append("number one")

myList.append("number two")
myList.append("number three")
print("Test One")
print(f"\tExpecting: ['number one', 'number two', 'number three']\n\tGot: {myList}")

myList.delete_tail()
print("Test Two")
print(f"\tExpecting: ['number one', 'number two']\n\tGot: {myList}")

myList.append(4)
print("Test Three")
print(f"\tExpecting: ['number one', 'number two', 4]\n\tGot: {myList}")

myList.delete_tail()
myList.delete_tail()
myList.delete_tail()
myList.delete_tail()
print("Test Four")
print(f"\tExpecting: []\n\tGot: {myList}")


