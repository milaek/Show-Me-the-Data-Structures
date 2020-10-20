#     CLASSES     #
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = {}
        self.users = {}

    def add_group(self, group):
        # adds group to the self's dictionary of groups making the key the string name, and the value the group obj
        self.groups[group.name] = group

    def add_user(self, user):
        # adds user to the self's dictionary of users making the key the user, and the value the same
        self.users[user] = user

    def get_groups(self):
        return self.groups.values()

    def get_users(self):
        return self.users.values()

    def get_name(self):
        return self.name


#     FUNCTIONS     #
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # check all users. if not found, recurse into groups
    # base case, user is found
    if group.users.get(user) is not None:
        return True
    # base case, user is not in subgroup
    internal_groups = group.get_groups()
    if internal_groups is None:
        return False
    for new_group in internal_groups:
        found = is_user_in_group(user, new_group)
        if found:
            return True
    return False


#     TESTING     #
parent = Group("parent")
child = Group("child")
child_2 = Group("electric boogaloo")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

parent_user = "parent_user"
parent.add_user(parent_user)

babiest_user = "babiest_user"
child_2.add_user(babiest_user)

child.add_group(sub_child)
parent.add_group(child)
parent.add_group(child_2)

# Test 1
print("Test One")
test_1 = is_user_in_group("sub_child_user", child_2)
print(f"Expected: False. Got {test_1}")

# Test 2
print("Test Two")
test_2 = is_user_in_group("babiest_user", parent)
print(f"Expected: True. Got {test_2}")

# Test 3
print("Test Three")
test_3 = is_user_in_group("parent_user", sub_child)
print(f"Expected: False. Got {test_3}")

# Test 4
print("Test Four")
test_4 = is_user_in_group("im not a person!", parent)
print(f"Expected: False. Got {test_4}")




