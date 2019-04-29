The find_recepients_area_codes function has a loop over 5213 number of records; each loop iteration is executed approximately 8 lines of the code instruction. Also, on line 71 and 73 this function calls twice the get_phone_area_code helper function to get the sending or receiving number area code.

Also, find_recepients_area_codes performs the phone number dictionary lookup operation. The Python dictionary implementation uses a hashmap implementation https://docs.python.org/3.7/library/stdtypes.html#mapping-types-dict, which has an average O(1) runtime complexity for the key lookup operation https://wiki.python.org/moin/TimeComplexity, and the worst case scenario is O(n). The worst case scenario happens under the condition of having keys collisions, which should not occur with string keys, or happen very rarely if keys are not of a string type and hash function produces hashes with collisions http://lewk.org/blog/python-dictionary-optimizations.

O(find_recepients_area_codes) = O(n * (2 * O(get_phone_area_code) + 1))

The get_phone_area_code function performs about 10 instructions, among them, are 2 slice operation, 1 string search and 1 retrieval the char of a string by index. The slice operation has O(k) complexity https://stackoverflow.com/questions/35180377/time-complexity-of-string-slice, where k is the length of the slice, in our case the maximum slice length is 5, and the string characters access by index takes constant time. Although the slice depends on the slice length, it doesn't change only between 3 and 5, for all the possible phone numbers. In addition, the setring char search has a linear complexity O(n) So the order the function should be linear:

O(get_phone_area_code) = O(n)

So the complexity of the find_recepients_area_codes:
O(find_recepients_area_codes) = O(n * (2 * O(n) + 1)) ~ O(n^2)

Also, there is an additional code which runs sorting of the phone numbers list, prints statements and calculates the percent of calls from fixed lines in Bangalore.

So there will be an addition to the mentioned run-time:

- the runtime of the sort function is O(n log n), according to the python documentation https://wiki.python.org/moin/TimeComplexity it's on average and worth case scenario
- prints and percent calculation  O(1)

The resulting runtime of the script is O(n + n log n + n^2), or after the approximation O(n log n + n^2).
