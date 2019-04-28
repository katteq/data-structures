The find_recepients_area_codes function has a loop over 5213 number of records, each loop iteration is executed approximately 8 lines of the code intstruciton. So the phone area search run time should be about O(8 * 5213), or O(8 * n), or after approximation - O(n).

There are additional code which run sorting of the phone numbers list, prints statements and calculates the percent of calls from fixed lines in Bangalore.

So there will be an addition to the mentioned run-time:

- the runtime of the sort function is O(n log n), according to the python documentation it's worth case scenario
- prints and percent calculation  O(1)

The resulting runtime is O(n + n log n + 1), or after the approximation O(n + n log n), and we could even neglect the n addition part saying that the order would be O(n log n).
