The find_markering_phones function  has two loops over 5213 number of records of the phone calls and 9072 records of the texts records: O(2 * 9072) + O(8 * 5213) ~ O(n). Which means that run time increases linearly to the amount of the data records in both data sets in total.

However, since the requirement of the task is to print the records in lexicographical order, the fucntion performs the list sort which complexity is O(n log n). And print statements run time is O(1)

The resulting runtime is O(n + n log n + 1), or after the approximation O(n + n log n), and we could even neglect the n addition part saying that the order would be O(n log n).
