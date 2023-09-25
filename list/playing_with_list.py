arr = [5, 7, 9, 30, 10, 11, 20, 25]
arr2 = [1, 2, 3, 4, 5]


# find the max element from the array

def get_max(array):
    temp = array[0]
    for i in range(1, len(array)):
        if array[i] > temp:
            temp = array[i]
    print(temp)


get_max(arr)


# find the second-highest element of a list

def get_second_highest_element(array):
    f_largest = 0
    s_largest = 0
    if len(array) <= 1:
        f_largest = array[0]
        s_largest = None
    for i in array[1:]:
        if i > f_largest:
            s_largest = f_largest
            f_largest = i
        elif i != f_largest:
            if s_largest is None or s_largest < i:
                s_largest = i
    print(s_largest)


get_second_highest_element(arr)


# find a list is sorted in ascending order or not, return result with yes or no

def get_a_list_is_sorted_or_not(array):
    checker = True
    temp = array[0]
    for i in range(1, len(array)):
        if temp > array[i]:
            checker = False
            break
        else:
            temp = array[i]
    if checker is True:
        print("Yes")
    else:
        print("No")


get_a_list_is_sorted_or_not(arr)
get_a_list_is_sorted_or_not(arr2)

# find the only odd from the list
arr_odd = [10, 20, 10, 30, 30]


def find_only_odd(array):
    res = None
    for i in array:
        count = array.count(i)
        if count % 2 != 0:
            res = i
            break
    print(res)


find_only_odd(arr_odd)
