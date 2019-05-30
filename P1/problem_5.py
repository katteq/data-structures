import hashlib
import time


class Block:
    def __init__(self, data="Geneis block", previous_hash="0"):
        self.timestamp = time.time()
        self.data = data.encode("utf-8")
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(previous_hash)

    def calc_hash(self, previous_hash):
        data_hash = hashlib.sha256()
        data_hash.update((str(self.data) +
                          str(self.timestamp) + str(previous_hash)).encode('utf-8'))
        return data_hash.hexdigest()

    def get_hash(self):
        return self.hash


class Blockchain:
    def __init__(self):
        """ Initialize a new blockchain with the first genesis block. """
        self.last = Block()
        self.chain = [self.last]
        self.size = 1

    def new_block(self, value):
        """ Adds a new block to the blockchain. """
        self.size += 1
        new_block = Block(value, self.last.get_hash())
        self.last = new_block
        self.chain.append(new_block)

    def get_size(self):
        """ Return the size or length of the blockchain list. """
        return len(self.chain)

    def get_last_block(self):
        """ Return the last block in the chain. """
        return self.last

    def to_list(self):
        """ Return the list of the blocks. """
        return self.chain


blockchain = Blockchain()
blockchain.new_block("1")
blockchain.new_block("2")
blockchain.new_block("3")
blockchain.new_block("4")

l = blockchain.to_list()

for block in l:
    print(block.hash, block.previous_hash)


def test_add_new_block(l):
    blockchain = Blockchain()
    for e in l:
        blockchain.new_block(e)

    if blockchain.size != len(l)+1:
        print("Fail")
        return

    res = True
    for i in range(1, len(l) + 1):
        if l[i-1].encode("utf-8") != blockchain.chain[i].data:
            res = False
            break
    print("Pass" if res else "Fail")


def test_blockchain_hash():
    blockchain = Blockchain()
    blockchain.new_block("1")
    blockchain.new_block("2")
    blockchain.new_block("3")
    blockchain.new_block("4")

    blockchain.chain[2].data = "12123"

    verify_last = 0
    for block in blockchain.chain:
        verify_last = block.calc_hash(verify_last)

    print("Fail" if verify_last == blockchain.get_last_block().hash else "Pass")


test_add_new_block(["1", "2", "3", "4", "5", "6", "6", "7"])
test_add_new_block([])
test_blockchain_hash()
