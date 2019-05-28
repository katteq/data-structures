class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LRU_Cache:
    def __init__(self, size=15):
        self.cache_size = size if size != None else 15
        self.count = 0
        self.head = None
        self.tail = None
        self.map = {}

    def get(self, key):
        """
        Returns the value from the cache by its key.

        Args:
        key(str): element's key

        Returns: any
        """
        node = self.map.get(key)
        return -1 if node == None else node.value

    def set(self, key, value):
        """
        Adds a new element into the cache. If element with the same key already exists
        it won't be added to the cache.

        Args:
        key(str): element's key
        value: new element value

        Returns: void
        """
        if key == None:
            return
        node = self.map.get(key)
        if node != None:
            return

        else:
            self.enqueue(key, value)

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def enqueue(self, key, value):
        """
        Enqueue the new element into the cache.

        Args:
        key(str): element's key
        value: new element value

        Returns: void
        """
        new_node = Node(key, value)
        self.count += 1
        if self.count > self.cache_size:
            self.dequeue()
        self.map[key] = new_node
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            old_head = self.head
            new_head = self.head.next
            self.head = new_head
            self.count -= 1
            self.map.pop(old_head.key)
            return old_head.value


def test(data, size, expected_output):
    """
    LRU test funstion.

    Args:
      data(list): list of the numbers/elements
      size(int): cache size limit
      expected_output(list): expected output

    Returns: void
    """
    cache = LRU_Cache(size)
    if data == None:
        cache.set(None, None)
    else:
        for el in data:
            cache.set(el, el)

    actual_output = []
    if data != None:
        for el in data:
            actual_output.append(cache.get(el))

    print("Pass" if actual_output ==
          expected_output and cache.size() == (0 if data == None else size if size != None and len(data) > size else len(data)) else "Fail")


test([], 5, [])
test(None, 5, [])
test([1, 2, 3], None, [1, 2, 3])
test([1, 2], 5, [1, 2])
test([1, 2, 3, 4, 5, 6], 5, [-1, 2, 3, 4, 5, 6])
test([1, 2, 3, 4, 5, 6], 3, [-1, -1, -1, 4, 5, 6])
