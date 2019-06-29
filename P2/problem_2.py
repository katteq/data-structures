def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    if len(array) == 0:
        return -1
    if len(array) == 1:
        return -1 if array[0] != target else 0
    index = int(len(array)/2)

    element = array[index]
    if element == target:
        return index
    else:
        return binary_search(array[index:], target) + index if target > element else binary_search(array[:index], target)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1
    if len(input_list) == 1:
        return 0 if input_list[0] == number else -1

    middle = int(len(input_list)/2)
    left = input_list[:middle]
    right = input_list[middle:]

    if len(left) == 1 and left[0] == number:
        return 0

    if len(right) == 1 and right[0] == number:
        return middle

    if left[len(left)-1] >= number:
        index = binary_search(left, number)
        if index > -1:
            return index

    if right[len(right)-1] >= number:
        index = binary_search(right, number)
        if index > -1:
            return index + middle

    if left[0] > left[len(left)-1]:
        index = rotated_array_search(left, number)
        if index > -1:
            return index

    if right[0] > right[len(right)-1]:
        index = rotated_array_search(right, number)
        if index > -1:
            return index + middle

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    actual = rotated_array_search(input_list, number)
    expected = linear_search(input_list, number)
    if expected == actual:
        print("Pass")
    else:
        print("Fail", expected, actual)


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
