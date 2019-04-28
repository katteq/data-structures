The find_markering_phones function has two loops over 5213 number of records of the phone calls and 9072 records of the texts records: O(2 * 9072) + O(8 * 5213) ~ O(n). Which means that run time increases linearly to the amount of the data records in both data sets in total.

But in addition to this, the algorithm executes the key lookup twice per loop cycle, and one time deletes the element from the dictionary. Each lookup and removal from a hashtable has a complexity of O(n); therefore for the entire loop this would add the order
O(3n^2) in a worst case scanario.

Also, since the requirement of the task is to print the records in lexicographical order, the function performs the list sort which complexity is O(n log n). And print statements run time is O(1)

The resulting runtime is O(n + 3n^2 + n log n + 1), or after the approximation O(n + n log n + n^2), or O(n^2).
