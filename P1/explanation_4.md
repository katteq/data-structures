To solve the active directory problem I decided to build a cache of users which is a dictionary of users name/id and all the directories list they belong to. The cache is built on the first `is_user_in_group` function execution, used python dictionary to map users to their corresponding sets of the groups. This cache guarantees a constant lookup time on every subsequent function call.


Time complexity explanation:

*Solution with the recursion*: The algorithm of the checking if the user is in the directory uses recursion to check if the user belongs to a group or child groups. The active directory data structure similar to a tree. So performing the child groups search in a recursion identical to a tree traversal. Therefore the complexity of the operation is O(N).

*Solution with the cache*: The algorithm with the cache performs recursion to traverse the tree into a map on the first `is_user_in_group` method invocation, which has O(N) time complexity as explained above. Theoretically, of active directory cache is not mutated, each invocation of the `is_user_in_group` method would have constant time complexity O(1).

