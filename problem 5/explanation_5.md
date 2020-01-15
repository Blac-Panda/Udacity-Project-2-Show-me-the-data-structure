# Explanation for Problem 5: Blockchain
**Author:** Moya Richards

This document provides a text explanation of the efficiency of the code and the design choices.

------------

------------


## Project Summary
|  | Summary Details |
| -------------- | --------------- |
| Efficiency | O(n) time complexity, and O(n) space complexity  |





## Design Choices


### Data Structures Used


| Data Structure | Time Complexity | Space Complexity |
| -------------- | --------------- | ---------------- |
| dictionary  |O(1) | O(n) |

This project is about building a blockchain.

A blockchain is made up of blocks.
A block for a blockchain is designed similar to that of a Node in a LinkedList link. However, there is a major difference. A Node has a next property which is a pointer to another Node, while the block has a previousHash property.

The block constructor accepts the parameters: data, timestamp,and the previousHash. The previousHash is the hash of the previous block in the chain and is used to verify the integrity of blocks in the chains. The block also contains a hash property which is automatically calculated from the parameters passed to the block's constructor when the block is created.

The blockchain is created with a head and tail property to store blocks. The head tracks the first block in the chain, and the tail tracks the last block added to the chain. 
The head is the genesis block. This is a block which does not have a reference to a previous block therefore it's previousHash property is arbitrarily set to 0 (zero)
The tail block exists to make inserting data into the chain faster; without it, insertion would have taken O(n) time, but now it takes O(1) constant time.

The blockchain also contains the chainDict dictionary property,  which stores all the blocks in the chain. An entry in this dictionary contains a block's hash as the key and the block as the value. This dictionary is utilized when the integrity of the blockchain is verified using the verifyChain() method. Without this dictionary we would have to traverse the entire chain to find the block containing the hash we were searching for. This dictionary provides O(1) constant time lookup for finding a block in the chain.


Verifying the data in the chain takes O(n) time (n = The number of blocks in the chain).
The chain is verified by visiting the tail first, then checking the previous blocks in the chain to make sure they were not tampered with.
The verifying function utilizes an __iter__ (iterator function) to traverse the blockchain. 

------------

------------
## Udacity Project Requirement
> **Blockchain**

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation. 

We can break the blockchain down into three main parts.


### First is the information hash:


```python
import hashlib

def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

```
We do this for the information we want to store in the block chain such as transaction time, data, and information like the previous chain. 

### The next main component is the block on the blockchain:



```python
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

```
Above is an example of attributes you could find in a Block class. 



### link all of this together in a block chain:


Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list. All of this will help you build up to a simple but full blockchain implementation! 



