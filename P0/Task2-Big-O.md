There are approximately 12 lines of the code in total will be executed looping over the list of the phone calls records using function find_number_with_longest_calls_time. There are two lines of code which perform the dictionary key lookup operations.

The Python dictionary implementation uses a hashmap implementation https://docs.python.org/3.7/library/stdtypes.html#mapping-types-dict, which has an average O(1) runtime complexity for the key lookup operation https://wiki.python.org/moin/TimeComplexity, and the worst case scenario is O(n). The worst case scenario happens under the condition of having keys collisions, which should not occur with string keys, or happen very rarely if keys are not of a string type and hash function produces hashes with collisions.

So taking into account the average case scenario for the dictionary key lookup O(1), given that the number of records in total 5213, we could assume that the order of the algorithm is O(12*5213), or O(12*n).So

After the approximation, it would be O(n), which means the run-time of the algorithm increases linearly to the amount of the call records.
