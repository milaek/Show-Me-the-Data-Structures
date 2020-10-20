from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        """
        :param capacity: int, desired cache capacity
        """
        # Initialize class variables
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :param key: key of desired value
        :return: value or -1 if no value found
        """
        # if key in dictionary
        if key in self.cache:
            # update queue
            self.cache.move_to_end(key)
            # return val
            return self.cache[key]

        # if key not found, return -1 and update nothing
        return -1

    def set(self, key, value=None):
        """
        :param key: key to set
        :param value: value to set linked to key
        """
        if self.capacity <= 0:
            print("LRU capacity is 0 or less. Please set a valid LRU capacity before continuing.")
            return
        if value is None:
            print("Please provide both a key and a value.")
            return
        # check for a full cache, remove least used item if full
        if len(self.cache) == self.capacity:
            self.cache.popitem(False)
        # add new item cache
        self.cache[key] = value


#    TESTING    #
# Test Setup
test = LRUCache(5)
test.set("one", "one")
test.set(2, 2)
test.set(3, 3)
test.set(4, 4)
test.set(5, 5)
test.set(6, 6)
# Test 1
print(test.get(7))
# expected result: -1 (because 7 is not present)

# Test 2
print(test.get(3))
# expected result: 3

# Test 3
print(test.get("one"))
# expected result: -1 (because one was dropped from cache

# Test 4
test.get(2)
test.set(7, 7)
print(test.get(2))
# expected result: 2 (because 2 was recently used and therefore wasn't the queue tail when the next value was set)

# Test 5
test = LRUCache(0)
test.set(1, 1)
print(test.get(1))
# expected result: LRU capacity is 0 or less. Please set a valid LRU capacity before continuing.
# -1
