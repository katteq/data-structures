class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


def union(llist_1, llist_2):
    result = LinkedList()
    if llist_1 == None and llist_2 == None:
        return result

    if llist_1 == None or llist_1.size == 0:
        return llist_2

    if llist_2 == None or llist_2.size == 0:
        return llist_1

    union_set = set()

    for lst in [llist_1, llist_2]:
        current_node = lst.head
        while current_node:
            if current_node.value not in union_set:
                union_set.add(current_node.value)
                result.append(current_node.value)
            current_node = current_node.next

    return result


def intersection(llist_1, llist_2):
    result = LinkedList()
    if llist_1 == None or llist_2 == None or llist_1.size == 0 or llist_2.size == 0:
        return result

    l1_set = set()
    l2_set = set()

    current_node = llist_1.head
    while current_node:
        l1_set.add(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node:
        if current_node.value in l1_set and current_node.value not in l2_set:
            result.append(current_node.value)
            l2_set.add(current_node.value)
        current_node = current_node.next

    return result


def create_linked_list(elements):
    """ Helper function creates the linked list for the array. """
    linked_list = LinkedList()
    for i in elements:
        linked_list.append(i)
    return linked_list


# Tests

def test(fn, l1, l2, res):
    linked_list_1 = create_linked_list(l1) if l1 is not None else l1
    linked_list_2 = create_linked_list(l2) if l2 is not None else l2

    actual_res = fn(linked_list_1, linked_list_2).to_list()

    res_sorted = sorted(res)
    actual_res_sorted = sorted(actual_res)

    if sorted(res) == sorted(actual_res):
        print("Pass")
    else:
        print("Fail:")
        print("Expected:", res_sorted)
        print("Actual:", actual_res_sorted)


test(union, [3, 2, 4, 35, 6, 65, 6, 4, 3, 21], [6, 32, 4, 9,
                                                6, 1, 11, 21, 1], [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11])

test(union, [1, 2, 3, 4, 5, 6, 7], [8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

test(intersection, [3, 2, 4, 35, 6, 65, 6, 4, 3, 21], [6, 32, 4, 9, 6,
                                                       1, 11, 21, 1], [6, 4, 21])
test(union, [3, 2, 4, 35, 6, 65, 6, 4, 3, 23], [1, 7, 8, 9,
                                                11, 21, 1], [3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21])
test(intersection, [3, 2, 4, 35, 6, 65, 6, 4, 3, 23],
     [1, 7, 8, 9, 11, 21, 1], [])

test(intersection, None, [1, 7, 8, 9, 11, 21, 1], [])
test(intersection, None, None, [])
test(intersection, [3, 2, 4, 35, 6, 65, 6, 4, 3, 23], None, [])

test(union, None, [1, 7, 8, 9, 11, 21, 1], [1, 7, 8, 9, 11, 21, 1])
test(union, None, None, [])
test(union, [3, 2, 4, 35, 6, 65, 6, 4, 3, 23],
     None, [3, 2, 4, 35, 6, 65, 6, 4, 3, 23])
