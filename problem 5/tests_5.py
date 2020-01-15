# https://docs.python.org/3/library/unittest.html

import sys
import logging       
import argparse


import unittest
from problem_5 import *




class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.bc = Blockchain();

        for n in range(10):
          #Get the hash for the previous block in the chain
          previous_hash = self.bc.tail.hash

          self.bc.insert('Block-data: {}'.format(n),previous_hash)
   
    """
    tamper with block, validation should fail
    """
    def test_invalidate_block(self):
        #make a new block chain since it will be modified
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

        log.debug("\nThe entire blockchain:\n%r" % bc)# Should print the entire blockchain.
        log.debug("\nBlock is valid? %r" % bc.verifyChain()) #check if the block is valid

        #Block is not valid
        self.assertTrue(bc.verifyChain() == False)

    """
    Pick two blocks in the chain, then check if the hash of one matches the previous hash of the other
    """
    def test_previous_block_linked_to_current_block(self):
  
        it = iter(self.bc)
        #Skip 3 blocks
        next(it)
        next(it)
        next(it)
        block1  = next(it)
        block2  = next(it)
        

        block2 = self.bc.chainDict[block2.hash]
        if(block2.calc_hash() == block1.previous_hash):
          log.debug("The previous hash for block1 matches the hash for the current block (block2)")

        log.debug("Block is valid?  %r" % self.bc.verifyChain()) #check if the block is valid
        
        self.assertTrue(self.bc.verifyChain())

    def test_has_genesis_block(self):
        self.assertEqual(self.bc.head.previous_hash,0)


#----------------------------------------------------
if __name__ == '__main__':

    """
    --------------------------------------------
    run code with log command:

    python tests_5.py  --loglevel="DEBUG"

    """

    parser = argparse.ArgumentParser(description='Blockchain')
    parser.add_argument("--loglevel", default='NOTSET', choices=["CRITICAL","ERROR","WARNING","INFO","DEBUG","NOTSET"],type=str, help="The level of logging captured is set to ``logging.NOTSET``by default. You may override this using the console setting ``loglevel`` (which is set to a level name")
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()

    loglevel = getattr(logging, args.loglevel.upper())
    logging.basicConfig(stream=sys.stderr, level=loglevel)
    log = logging.getLogger("Blockchain")



    """
    sys.argv.pop() works with the command:
    python tests_5.py  --loglevel="DEBUG"

    sys.argv.pop() does not work with the command line arguments to show details about the test

    python -m unittest  -v tests_5.TestSequenceFunctions --loglevel="DEBUG"  
      
    the command caused the error:
    error: unrecognized arguments: --loglevel=DEBUG
    """

    sys.argv.pop()
    #--------------------------------------------



    unittest.main()