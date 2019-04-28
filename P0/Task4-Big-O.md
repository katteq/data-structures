The find_markering_phones function has two loops over 5213 number of records of the phone calls and 9072 records of the texts records.

But in addition to this, the algorithm executes the key lookup twice per loop cycle, and twice time deletes the element from the dictionary.

The Python dictionary implementation uses a hashmap implementation https://docs.python.org/3.7/library/stdtypes.html#mapping-types-dict, which has an average O(1) runtime complexity for the key lookup operation https://wiki.python.org/moin/TimeComplexity, and the worst case scenario is O(n). The worst case scenario happens under the condition of having keys collisions, which should not occur with string keys, or happen very rarely if keys are not of a string type and hash function produces hashes with collisions http://lewk.org/blog/python-dictionary-optimizations. The same complexity is for the deletion operation https://wiki.python.org/moin/TimeComplexity. The total complexity of the dictionary operations is after approximation is O(1).

O(find_markering_phones) = O(9072 + 5213 + O(1)) ~ O(n).

Also, since the requirement of the task is to print the records in lexicographical order, the function performs the list sort which complexity is O(n log n). And print statements run time is O(1)

The resulting runtime is O(n + n log n + 1), or after the approximation O(n + n log n).
