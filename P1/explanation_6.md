The python set data structure has been used here to build the `union` and `intersection` functions. Set has a constant lookup time. Therefore, the complexity of both tasks which have to iterate over two linked lists one by one is O(n + m), where `n` is the length of the first list, and, `m`  length of the second list, simplified O(n).

*Union* time complexity explanation:

The union function gathers the new linked list looping through each of the element in both input linked lists. Therefore, if the first list has N elements and the second list has the M elements, the function has to run N+M times to compile the union list, O(N+M), or simplified O(n).

*Intersection* complexity explanation:

The first step of the algorithm is to convert the first linked list onto a set data structure which guarantees the uniqueness of the element. This is a linear time complexity O(N). After that,the function loops through the second linked list to reveal if some of the elements belong to the first linked list as well, also with the linear time O(M), given that the second list has M elements.

Therefore the complexity would be O(N+M), or O(n)
