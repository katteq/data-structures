The `find_files` was written using recursion to check over the nested directories and files.


Time complexity explanation:

The algorithm of the file search uses the recursion to check through all the folders' files. The structure of the directories and files resembles the tree structure where the directories are nodes and files are leaves. So whatever the size of the tree, we have to visit every node to check it's leaves(files) to match the search criteria. The tree traversal has a time complexity of O(n).
