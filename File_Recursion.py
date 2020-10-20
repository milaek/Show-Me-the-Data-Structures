import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """
    if not os.path.isdir(path):
        if os.path.isfile(path):
            if path.endswith(suffix):
                return [path]
            else:
                return []
        else:
            print("Not a valid path")
            return []
    paths_list = []

    for item in os.listdir(path=path):
        # make a string of the full path to item
        full_path = os.path.join(path, item)
        # if the item is a file, check for the suffix
        if os.path.isfile(full_path):
            if item.endswith(suffix):
                # end of recursion, appends file to path
                paths_list.append(full_path)
        if os.path.isdir(full_path):
            # recursive call
            paths_to_add = find_files(suffix, full_path)
            # merge lists of paths into one list
            if paths_to_add is not None:
                paths_list += paths_to_add

    # return list of paths to suffix containing items
    return paths_list


#    TEST    #
# please input the location of testdir your directory
test_dir = r"C:\Users\milae\Desktop\testdir"

# Test 1: find .c
print("Test 1")
test_1 = sorted(find_files(".c", test_dir))
print("Your found locations are: " + str(test_1))
expected_1 = [test_dir+r"\subdir1\a.c", test_dir+r"\subdir3\subsubdir1\b.c", test_dir+r"\subdir5\a.c",
              test_dir+r"\t1.c"]
print("Expected locations are: " + str(expected_1))
if test_1 == expected_1:
    print("Pass")
else:
    print("Fail")
# expected: [test_dir+r"\subdir1\a.c", test_dir+r"\subdir3\subsubdir1\b.c", test_dir+r"\subdir5\a.c",
#               test_dir+r"\t1.c"]

# Test 2: find .h
print("Test 2")
test_2 = sorted(find_files(".h", test_dir))
print("Your found locations are: " + str(test_2))
expected_2 = [test_dir+r"\subdir1\a.h", test_dir+r"\subdir3\subsubdir1\b.h", test_dir+r"\subdir5\a.h", test_dir+r"\t1.h"]
print("Expected locations are: " + str(expected_2))
if test_2 == expected_2:
    print("Pass")
else:
    print("Fail")
# expected: [test_dir+r"\subdir\a.h", test_dir+r"\subdir3\subsubdir1\b.h", test_dir+r"\subdir5\a.h", test_dir+r"\t1.h"]

# Test 3: find .z
print("Test 3")
test_3 = find_files(".z", test_dir)
print("Your found locations are: " + str(test_3))
expected_3 = []
print("Expected locations are: []")
if test_3 == expected_3:
    print("Pass")
else:
    print("Fail")
# expected: []
