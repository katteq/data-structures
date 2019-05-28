import sys
import collections
import copy


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        new_node = Node(value)
        self.num_elements += 1
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        elif self.tail is not None:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, value, condition):
        new_node = Node(value)
        self.num_elements += 1
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            current = self.head
            while current.next != None and condition(current.value):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def dequeue(self):
        if self.is_empty():
            return None

        next_head = self.head.next
        self.num_elements -= 1
        res = self.head.value
        self.head = next_head
        return res


class TreeNode:
    def __init__(self, frequency, value=None):
        self.frequency = frequency
        self.value = value
        self.left = None
        self.right = None


class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


def huffman_tree(data):
    entry_map = {}

    for c in data:
        entry = entry_map.get(c)
        entry_map[c] = 1 if entry == None else entry + 1

    entry_map_sorted = sorted(entry_map.items(), key=lambda item: item[1])

    queue = Queue()
    for frequency, value in entry_map_sorted:
        queue.enqueue(TreeNode(value, frequency))

    # start

    tree_head = None

    while queue.size() > 1:
        first = queue.dequeue()
        second = queue.dequeue()

        values_sum = first.frequency + second.frequency
        new_node = TreeNode(values_sum)
        new_node.left = first
        new_node.right = second

        tree_head = new_node

        queue.insert(new_node,
                     lambda n: n.frequency < values_sum)

    return tree_head


def huffman_encoding(data):
    if data == "" or data == None:
        return (None, None)

    tree = huffman_tree(data)
    if tree == None:
        return (None, None)
    codes = {}

    code = ""
    stack = Stack()

    current_node = copy.deepcopy(tree)
    while current_node:
        if current_node == None:
            break
        if current_node.left:
            next_node = current_node.left
            current_node.left = None
            stack.push(current_node)
            current_node = next_node
            code += "0"
            continue
        if current_node.right:
            next_node = current_node.right
            current_node.right = None
            stack.push(current_node)
            current_node = next_node
            code += "1"
            continue
        if current_node.left == None and current_node.right == None:
            codes[current_node.value] = code
            code = code[0:-1]
            current_node = stack.pop()

    res = ""
    for char in data:
        res += codes[char]

    return (res, tree)


def huffman_decoding(data, tree):
    if data == "" or data == None or tree == None:
        return None
    res = ""
    current_node = tree
    current_data = data
    while current_node != None:
        if current_node.left == None and current_node.right == None:
            res += current_node.value
            current_node = tree
        else:
            path = current_data[0:1]
            if path == "":
                break
            current_data = current_data[1:]
            current_node = current_node.right if path == "1" else current_node.left

    return res


def test(data, expected_encoded_data, expected_encoded_size, expected_decoded_size):
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)

    if decoded_data == (data if data else None) \
            and expected_encoded_data == encoded_data \
            and expected_encoded_size == (sys.getsizeof(int(encoded_data, base=2)) if encoded_data else None) \
            and expected_decoded_size == (sys.getsizeof(decoded_data) if decoded_data else None):
        print("Pass")
    else:
        print("Fail")


test("The bird is the word",
     '0110100000110011100111101111110001010011001011000001101010101111101111', 36, 69)
test("The content of the encoded data is: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
     '01011101011000010111011111100100000001010000001111100101111011000101100001011001010010111111010100011010011101011010001101011100011111010110001101011011110100100011001101110001100011111111101001101110101110110011110100100111111110000000111101100110010000101000111011111100100111110011011100000100011110100100111101101010001100010001111110111100001000101010110011100110000000101000111111100110100111010111001100110001111011111100111110101001100000110011110001110100100111000010010111100010101000101011110010000001111110000011110011101101101011101001000101100100001110101110110011110100100010111001111010101010100110101111011100110001011011111101101', 112, 207)

test("",
     None, None, None)
