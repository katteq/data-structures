def sort_012(input_list):
    """
    The idea is to put 0 and 2 in their correct positions, which will make sure
    all the 1s are automatically placed in their right positions
    """
    # initialize pointers for next positions of 0 and 2
    front_position = 0
    end_position = len(input_list) - 1

    current_index = 0
    while current_index <= end_position:
        if input_list[current_index] == 0:
            input_list[current_index] = input_list[front_position]
            input_list[front_position] = 0
            front_position += 1
            current_index += 1
        elif input_list[current_index] == 2:
            input_list[current_index] = input_list[end_position]
            input_list[end_position] = 2
            end_position -= 1
        else:
            current_index += 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
