The count_phone_numbers function loops over the list of phone records and constructs the dictionary with the keys which are a distinct set of the phone numbers.

The function's loop executes 4 lines of the code, two of which is the dictionary key lookup.

The Python dictionary implementation uses a hashmap implementation https://docs.python.org/3.7/library/stdtypes.html#mapping-types-dict, which has an average O(1) runtime complexity for the key lookup operation https://wiki.python.org/moin/TimeComplexity, and the worst case scenario is O(n). The worst case scenario happens under the condition of having keys collisions, which should not occur with string keys, or happen very rarely if keys are not of a string type and hash function produces hashes with collisions.

So taking into account the average case scenario for the dictionary key lookup O(1), each line would take O(1), four lines run - O(4), but since it happens for each loop cycle, it would be O(4n) in total.

Therefore, one run of the function would have the order of O(4n). Since we are running the function twice for the calls data and the texts data records, the run time should be doubled - O(8n). And after approximation, it is O(n).
