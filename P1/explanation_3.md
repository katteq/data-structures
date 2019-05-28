Several data structured were used to implement Huffman coding algorithm: Stack, LinkedList, and Tree. The Huffman encoding function starts with counting the frequency of the characters in the input data using the python dictionary. After the frequency map is constructed, the function builds the queue of the tree nodes that would become a Hoffman tree leaves.

When the Huffman tree ready, a stack data structure is used to traverse the tree and build the map of the data characters and their corresponding binary codes. The `huffman_encoding` function uses the codes map to encode the data string and returns the Huffman tree and the resulting compressed value tuple.

The tree is necessary to decode the value back into an initial value in the `huffman_decoding` function.
