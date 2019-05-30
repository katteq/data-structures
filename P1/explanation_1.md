LRU cache has been implemented using a linked list data structure which keeps track of both head and tail nodes to enqueue and dequeue nodes efficiently. Since linked list doesn't provide insert operation, it's nodes is naturally ordered from the eldest to the most recently added values. Therefore, if cache size reaches the limit, it dequeues the nodes from the beginning of the linked list. Adding and removing data from the linked list has a constant time `O(1)`.

LRU cache supports `get` and `set` operations. The python set data structure is used to preserve the key-value pairs and have a constant lookup time.

Time complexity explanation:

The LRU cache performs two primary operations get and set when adding a new value. The data structure used internally is a linked list. Therefore, to set value a new value we enqueue it to the tail of the list, the operation is a constant time O(1). Also, we have to maintain the key-value dictionary for efficient access to value be its key. If the cache limit reached, before enqueueing the new node we should remove the one from the head of the list, dequeue operation is O(1).

get: O(1)
set: O(1) + O(1) = O(2), ~O(1)

