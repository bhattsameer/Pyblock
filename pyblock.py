import datetime
import hashlib
from huepy import *

def banner(): 
    print("\n\n\n")
    print(lightpurple ("\t ####  #     #  ####   #      ###     ####  #   #      "))
    print(lightred    ("\t #   #  #   #   #   #  #     #   #   #      #  #       "))
    print(lightcyan   ("\t ####    ###    ####   #     #   #  #       ##        "))
    print(lightred    ("\t #        #     #   #  #     #   #   #      #  #       "))
    print(lightpurple ("\t #        #     ####   ####   ###     ####  #   #   by @howCodeOrg and @debugger      "))
    print("\n\n\n")
banner()
total = int(input(white("Enter the total number of blocks:")))
diff = int(input(white("Set difficulty from (0,10,20):")))

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return good(lightred("Block Hash: ")) + white(str(self.hash())) + "\n" + good(lightgreen("BlockNo: ")) + white(str(self.blockNo)) + "\n" + good(lightblue("Block Data: ")) + white(str(self.data)) + "\n" + good(lightcyan("Hashes: ")) + white(str(self.nonce)) + "\n--------------"

class Blockchain:
    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()

for n in range(total):
    blockchain.mine(Block("Block " + str(n+1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
