In this problem, I have utilized all my knowledge about the blockchain to build the trivial its version using a linked list and python hashing library. Each block hash value is constructed of the several information pieces: data itself, previous block hash and timestamp of the new block. The blockchain class keeps the chain of all the blocks, reference to the last block and the chain size.

I had added two tests to test a blockchain hash function and test verification of the data by recalculation of the hashes when the data of one of the blocks has been tampered

Time complexity explanation:

The blockchain uses list data structure internally to store all the blocks. Adding a new block to a blockchain is a constant time operation O(1) since it's always added to the end of the list. However, if there is a need to verify whether one of the blocks data has tampered we need to recalculate the hashes of all the blocks in the chain and compare the resulting value to a current last block hash. This operation has linear complexity O(N) since we have to loop through the chain of N size.
