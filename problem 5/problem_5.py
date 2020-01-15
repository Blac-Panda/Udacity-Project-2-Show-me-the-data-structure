import hashlib
import datetime

import sys
import logging
import argparse






class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next=None

    #Creates the hash of the block
    def calc_hash(self):
        sha = hashlib.sha256()

        #hash_str = "We are going to encode this string of data!".encode('utf-8')
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')

        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return f"Block(data: {self.data},hash:{self.hash},previous_hash:{self.previous_hash})"

    def __str__(self):
        return f"Block(data: {self.data},hash:{self.hash},previous_hash:{self.previous_hash})"


class Blockchain:
    def __init__(self):
        self.chain = []
        self.chainDict = {}
        """
        Create a genesis block
        This is the first block of the chain 
        It cannot point to a previous block because it is the first one!
        """
        block = Block(datetime.datetime.now(), "Genesis block", 0)
        self.head = block
        self.tail = block

        self.chainDict[block.hash] = block
        self.chain.append(block)



        """
        --------------------------------------------
        run code with log command:

        python problem_5.py  --loglevel="DEBUG"

        """
        parser = argparse.ArgumentParser(description='Blockchain')
        parser.add_argument("--loglevel", default='NOTSET', choices=["CRITICAL","ERROR","WARNING","INFO","DEBUG","NOTSET"],type=str, help="The level of logging captured is set to ``logging.NOTSET``by default. You may override this using the console setting ``loglevel`` (which is set to a level name")


        args = parser.parse_args()

        loglevel = getattr(logging, args.loglevel.upper())
        logging.basicConfig(stream=sys.stderr, level=loglevel)
        self.log = logging.getLogger("Blockchain")
        #--------------------------------------------



    def insert(self,data,previous_hash):

        """
        UTC is Coordinated Universal Time (formerly known as Greenwich Mean Time, or GMT). 
        The acronym UTC is not a mistake but a compromise between English and French.
        @see https://docs.python.org/3/library/time.html
        """
        timestamp = datetime.datetime.now()

        #Add a new block to the chain - make it the tail of the linked list
        block = Block(timestamp,data,previous_hash)


        """
        chainDict are linked using previous hashes and not by pointers(like a linked list)  
        therefore a dictionary will be used to link the hash to the block in the computer's memory
        """
        self.chainDict[block.hash] = block


        #set the last block
        self.tail = block


        #------------------------------------
        self.chain.append(block)
        #------------------------------------
        





    """
    Create an object generator to return a block when a for loop is used
    The loop starts at the last block in the chain
    """
    def __iter__(self):
        if len(self.chainDict) == 0:
            return

        block = self.chainDict[self.tail.previous_hash]
        while block:
            yield block

            # stop loop after genesis block is printed
            if block.previous_hash == 0:
                break
            
            #make sure that the next block for the loop exists in the list. If it does not exists, quit the while loop
            if block.previous_hash not in self.chainDict:
                break
            block = self.chainDict[block.previous_hash]
    

    """
    Use to print the entire block chain by looping through the link list
    @see __iter__
    """
    def __repr__(self):
        output = ''
        for block in self:
            output += str(block) + "\n"
        return output

    def __str__(self):
        output = ''
        for block in self:
            output += str(block) + "\n"
        return output

    """
    Detect changes to a single block
    Recalculate the hash of the block and see if all the hashes match up.
    """
    def verifyChain(self):
        block = self.tail
        while block:
            previous_hash  = block.previous_hash


            previous_block = self.chainDict.get(previous_hash)

            #The previous block for the genesis block does not exist in the chain
            if previous_hash == self.head.previous_hash:
               break;

            """
            - make sure that the next block for the loop exists in the list.
            - if block does not exists block is not valid
            """
            if not previous_block:
                return False

            #recalculate the hash to make sure that it hasn't changed
            if (block.hash != block.calc_hash()):
                self.log.debug("\n\nBlock is not valid? %r \n\n" % block) #check if the block is valid
                #print("--1------------------------",block)
                return False;

            #make sure data in the previous block was not tampered with by recalulating the hash
            if (previous_hash != previous_block.calc_hash()):
                self.log.debug("\nPrevious_block is not valid? %r \n\n" % previous_block) #check if the block is valid
                return False
               
            block = previous_block
        return True

if __name__ == "__main__":
    #------------------------------------------
    """
        verify the data
    """
    def run_example_verify_data():
            
        bc = Blockchain();

        for n in range(10):
                    #Get the hash for the previous block in the change
          previous_hash = bc.tail.hash    
          bc.insert('Block-data: {}'.format(n),previous_hash)
   
        print(bc)# Should print the entire blockchain.
        print("\n\nChain valid: ", bc.verifyChain())

    #--------------------------------------------

    """
        Uncomment the run_example_verify_data function to view the data,
        run by calling the command below
    """
    #run_example_verify_data()


    #------------------------------------------

    """
        run test cases by calling the commands below:
        --basic testing mode
        python tests_5.py
    """
    
    def test_invalidate_block():
        bc = Blockchain();

        for n in range(10):
          #Get the hash for the previous block in the chain
          previous_hash = bc.tail.hash

          bc.insert('Block-data: {}'.format(n),previous_hash)
   

        it = iter(bc)
        next(it)
        next(it)

        #tamper with a block in the chain by changing its data
        block = next(it)
        block.data = "New data: I am changed ,  Previous data: " + block.data

        print("\nThe entire blockchain",bc)# Should print the entire blockchain.
        print("\nBlock is valid? ",bc.verifyChain()) #check if the block is valid




    test_invalidate_block()