﻿Huffman Coding
**Author:** Moya Richards

This document provides a text explanation of the efficiency of the code and the design choices.

------------

------------


## Project Summary
|  | Summary Details |
| -------------- | --------------- |
| Efficiency | O(n logn) time complexity, and O(n) space complexity  |


## Design Choices


### Data Structures Used

| Data Structure | Time Complexity | Space Complexity |
| -------------- | --------------- | ---------------- |
| Priority queue implemented with a min heap binary tree| O(log n) - delete,insert | O(n)|
| dictionary | O(1) | O(1) |

This project is about encoding data with the Huffman coding algorithm. Huffman coding is used to reduce/compress the size of data. A computer reads data in binary, zeros and ones (0,1), therefore uncompressed data, such as ASCII characters in a string normally gets encoded into binary format. Unfortunately every ASCII character in a string gets encoded with the same fixed amount of 8 bits. so this often results in data with large sizes.

Lets look at the size of a string when we multiply the number of characters in the strings by 8 bits. The string "The bird is the word" which has 20 characters, will be encoded as 160 bits (20 * 8) or 20 bytes (since 1 byte = 8 bits, 160 bits/8 bits = 20 bytes). 20 bytes does not seem very big, but the larger the string the more bytes it will use, and the harder it becomes to store that string in a file or transfer it across a computer network. The Huffman coding algorithm was designed to solve this size issue by compressing the data to make it smaller.

To reduce the size of data with Huffman coding, each character is given a binary sequence whose size depends on how often that character appear in the string. The resulting binary sequence which varies in length is then used to encode the string. Because the size of the resulting binary sequence is usually smaller than the fixed 8 bit encoding this produces a compressed binary representation of the string that is significantly smaller than the original. **Note:** for this particular string python's sys.getsizeof() does not really measure the amount of memory used by the string, therefore it will not report 20 bytes for the uncompressed string. sys.getsizeof() is used to show that there is a clear difference between the fixed 8 bits binary encoding and the variable length Hoffman coding.

## **Algorithm**

### **Step 1:**  calculate the frequency of all characters in the string
create a map with the characters as keys and their corresponding frequencies as values.

**Time complexity:**  O(n)
**Space complexity:** O(n)
**Step 2:**  Use a priority queue, specifically a binary minheap, to prioritize/sort the data from the map
-  create a priority queue then fill it with nodes containing the data from the map. 
The nodes with the lowest frequencies has the highest priority.
**Time complexity:** O(log n)
**Space complexity:** O(n)

### **Step 3:**  
Use the priority queue, to build a Huffman tree(a binary min heap) from the queue:

- remove 2 of the lowest frequency node at a time from the queue.
- then add their frequencies together to produce the frequency for a new node
- next, add the first node removed as the left child of the new node
- then add the second node removed as the right child of the new node.
- then reinsert the new node into the list. Repeat these steps until only one node remains in the priority queue.

Note: it takes 0(1) time to add a node to the back of the queue, and  0(1) time to delete a node from the front of the queue, but because the tree has to rebalance itself, insertion and deletion actually takes O(log n) time to complete.
**Time complexity:** O(log n)
**Space complexity:** O(n)


### **Step 4:**
Use the Huffman tree to build the binary sequence for each character
Recursively traverse the tree in search of every leaf node. Each time a leaf node is found, save its binary sequence in a dictionary,

  Create the encoding for each character by tracing a path to its node from the root 
    - Starting from the root, trace the path to each leaf
    - Every time a left node is found, append a 0
    - Every time a right node is found, append a 1
    - Stop creating the code when a leaf node is reached. 
  The result at each leaf is its Huffman encoding

**Time complexity:** O(log n)
**Space complexity:** O(n)

### **Step 5:**
Perform the encoding
- Loop through the original string, search the map for the corresponding character
- replace the character with its binary sequence equivalent, a O(1) lookup for each character). 


**Time complexity:** O(n)
**Space complexity:** O(n)


###**Step5:
Perform the decoding - use the Huffman tree to get the original data.
- create an empty string to store the decoded data
- position the start node of the tree at the root.
- then loop through the binary digits in the decoded data
- for each bit  traverse the tree until a leaf node is found.
A zero bit walks the left of the tree and a 1 bit walks the tree to the right.
- when a leaf node is found, pull the character from it and add it to the decoded data string.
- Then reposition the start node of the tree back to the root, doing so marks the search for the next character to be decoded 

**Time complexity:** O(n log n)
**Space complexity:** O(n)




# What I learned


- The final node frequency/priority in the priority queue will equal the total number of characters in string

- Huffman coding is completely dependent upon the frequency of characters, therefore the binary code created for data with the same set of frequency will be the same. This means that 'abcde' and 'fghij' will produce the same set of binary code sequence. However, this is perfectly ok because the magic takes place when the characters get preserved in the Huffman coding binary tree.

- Another trick that keeps the similar text independent is fact that the order of the characters is saved when the characters are switched with their corresponding binary code. This is part of the reason why Huffman coding is considered to be lossless encoding

- When you remove an item from the min heap, the heap is going to try to balance itself, so the characters in the tree will shift around a bit automatically. Don't get discourage by that. The key thing to remember is that even though the characters associated with a code will be different the Huffman tree is going to produce the same set of binary code.

- Note when we build a combined internal node, it doesn’t represent a character like the leaf nodes do. You can leave the node value empty or add a random character of your choosing. I'll leave that part up to you. Dont worry we won't use the value stored in the combined node when encoding.


------------
------------
------------
## Udacity Project Requirement
### **Huffman Coding**



A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leaf.

There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

        Take a string and determine the relevant frequencies of the characters.
        Build and sort a list of tuples from lowest to highest frequencies.
        Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
        Trim the Huffman Tree (remove the frequencies from the previously built tree).
        Encode the text into its compressed form.
        Decode the text from its compressed form.

You then will need to create encoding, decoding, and sizing schemas.

For Example:

```python
import sys

def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
```

## Resources

[Huffman Visualization!](https://people.ok.ubc.ca/ylucet/DS/Huffman.html "Huffman Visualization!")

[Tree Generator](http://huffman.ooz.ie/ "Tree Generator")

[Additional Explanation](https://www.siggraph.org/education/materials/HyperGraph/video/mpeg/mpegfaq/huffman_tutorial.html "Additional Explanation")




























































