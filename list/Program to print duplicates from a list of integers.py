import numpy as np

array = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]


def find_duplicate_using_single_loop():
    u_list = []
    dup_list = []
    for i in array:
        if i not in u_list:
            u_list.append(i)
        elif i not in dup_list:
            dup_list.append(i)
    print(dup_list)


# complexity > time O(n), space O(n)


def def_find_duplicate_using_enumerate_method():
    print(list(set([x for i, x in enumerate(array) if array.count(x) > 1])))


# complexity > time O(n), auxiliary space O(1)

def_find_duplicate_using_enumerate_method()


# let's use numpy for reducing the time complexity

# Algorithm:
#
# Initialize the list l1 with some values.
# Import the numpy library.
# Use numpy.unique() to get the unique values and their counts in the list l1.
# Use numpy.where() to get the indices of the elements in the counts array that are greater than 1.
# Use these indices to get the corresponding elements from the unique array


def find_dup_using_numpy():
    unique, counts = np.unique(array, return_counts=True)
    dup_element_list = unique[np.where(counts > 1)]

    print(dup_element_list)
    print(counts)


find_dup_using_numpy()
# Time Complexity:
#
# numpy.unique() has a time complexity of O(nlogn) due to the sorting step, where n is the length of the input array.
# numpy.where() has a time complexity of O(n), where n is the length of the input array.
# Indexing an array takes constant time O(1).
# Therefore, the time complexity of this numpy code is O(nlogn), dominated by numpy.unique().
#
# Auxiliary Space:
#
# The space complexity of this numpy code is O(n), since we are storing the input list l1 and the output list
# new_list. numpy.unique() and numpy.where() internally create intermediate arrays, but they are not included in the
# space complexity of this code because they are temporary and not stored in memory.
