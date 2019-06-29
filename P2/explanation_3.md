In this task, I used a maxheap data structure to find two numbers, such as their sun is maximum. The complexity of the maxheap building is algorithm using arrays would be O(log(n))(insert operation).

When the tree is ready, the construction of the numbers goes from the top removing the max element on each step. On the first step, the heap max value would be the first digit of the first number. On the second step, the heap max would be the first digit of the second number.  On the third step, the heap max would be the second digit of the first number, on the fourth step the heap max would be the second digit of the second number, and so on, until we remove all the element from the tree.

Each step requires the element remove and heapify, which would have O(log(n)) complexity as well, so the resulting complexity for the tree of n elements would be O(nlog(n))
