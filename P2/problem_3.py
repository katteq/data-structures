class MaxHeap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        if self.size() == 0:
            return None
        to_remove = self.cbt[0]
        self.next_index -= 1
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # # we do not remove the element, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = None

        self._down_heapify()
        return to_remove

    def size(self):
        return self.next_index

    def is_empty(self):
        return self.size() == 0

    def _up_heapify(self):
        # print("inside heapify")
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element < child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            max_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                max_element = max(parent, left_child)

            # compare with right child
            if right_child is not None:
                max_element = max(right_child, max_element)

            # check if parent is rightly placed
            if max_element == parent:
                return

            if max_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = max_element
                parent = left_child_index

            elif max_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = max_element
                parent = right_child_index

    def get_maximum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    heap = MaxHeap(len(input_list))

    for element in input_list:
        heap.insert(element)

    first_number = ''
    second_number = ''

    current = heap.remove()
    i = 1
    while current:
        if i == 1:
            first_number += str(current)
            i = 2
        else:
            second_number += str(current)
            i = 1
        current = heap.remove()
    return [int(first_number), int(second_number)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail", output)


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[9, 2, 1 , 4, 3, 9], [942, 931]])
