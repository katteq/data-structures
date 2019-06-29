This problem solved via building the Trie data structure to search for the matching routes where instead of the characters in words the route names are used to construct the nodes split by the route separator `/`. The space complexity of building a Trie is `O(n*m)`, where `n` is the number of the handlers, and` is the length of the route( `/home/about` would have length 2).

The route lookup would have a constant time O(m) complexity.
