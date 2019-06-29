The binary search algorithm was used to solve this problem. Given the condition that the input array is rotated at some random point, we might assume that if we find the rotation pivot, it would be easy to search for a given number in both sorted parts separately.

So the first step starts with breaking the array onto two equal parts taking the middle element as a pivot. If two resulting ranges have only one element, it's checking whether the searchable value is the elements of the array. Otherwise, we have to identify in which part continue the search.

Since the array is rotated the best case scenario would be when we hit the rotation pivot, and two resulting arrays are sorted. If this is the case, we should compare the first and the last elements of the left and right parts to identify which one potentially contains the given input number. If found - continue the binary search in that part.

Another case would be if we do not hit the rotation pivot yet, so one of the parts would be perfectly sorted, the other might still be rotated. In this case, left or right parts of the array should be checked on being the range where the input value would fit into, and if positive continue to search for the index using binary search in that part. If the value is not in the sorted part, the function breaks the rotated part on two arrays again and continue same until the index found.

The complexity of the algorithm is O(log(n)).
