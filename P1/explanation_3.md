Several data structured were used to implement Huffman coding algorithm: Stack, LinkedList, and Tree. The Huffman encoding function starts with counting the frequency of the characters in the input data using the python dictionary. After the frequency map is constructed, the function builds the queue of the tree nodes that would become a Hoffman tree leaves.

When the Huffman tree ready, a stack data structure is used to traverse the tree and build the map of the data characters and their corresponding binary codes. The `huffman_encoding` function uses the codes map to encode the data string and returns the Huffman tree and the resulting compressed value tuple.

The tree is necessary to decode the value back into an initial value in the `huffman_decoding` function.

The Huffman coding algorithm works with the Huffman tree for the encoding and decoding.

*COMPLEXITY OF THE HUFFMAN TREE CONSTRUCTION*:

The `huffman_tree` function performs the following steps:

1)  build the map of the characters frequency O(N), which corresponds to a simple loop through every character in the input data, and completing the dictionary value;

2)  The frequency map has to be sorted by a frequency value, the python sorting complexity is O(n log n). Also,  in my implementation, I 've constructed a queue of the sorted data Tree nodes, the time complexity of this operation is O(N)

3) Tree construction performs while loop N - 1 times, taking each time 2 nodes from the queue until the queue left with just one node.

On each cycle, we construct a new tree node and insert it in the already ordered queue using the frequency condition. To insert a new tree node I look through the queue nodes until the condition returns `True`, as soon as this happened, the new node inserted into the place between the current nodes.

So per each cycle, the worst case scenario we have to loop M time, where M is the size of the queue. For example, if the initial queue size is 5, on the first iteration, the algorithm has to iterate over the (5-2) elements queue to search for a new node place, on the second iteration: (4-2) elements queue, and so on until the queue size is 1. So if the initial queue has size of N elements, then to insert a new tree node complexity:

iteration 1: insert complexity O(N - 2)
iteration 2: insert complexity O(N - 3)
iteration 3: insert complexity O(N - 4)
...
iteration N-1: O(1)

or O( (N-1) * Sum( (N-2) + (N-3) + ...+1)) ) ~ O(n^2).

Therefore my Huffman tree building function has a time complexity: O(N) + O(N) +O(N^2) => ~ O(n^2)

*THE COMPLEXITY OF THE HUFFMAN TREE ENCODING:*

The Huffman encoding uses the Huffman tree traversal algorithm to build a compressed data value. The tree traversal complexity id O(n), where n is a number of the tree nodes.

*THE COMPLEXITY OF THE HUFFMAN TREE DECODING:*

The Huffman decoding uses the Huffman tree walk until the leaf with appropriate character has been reached. So the complexity of the decoding would be O(n), where n is the length of the encoded data.


