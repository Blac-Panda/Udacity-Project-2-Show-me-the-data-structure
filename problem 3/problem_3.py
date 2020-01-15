import sys
from minHeap import MinHeap
from node import Node


class HuffmanCoding():

  """
  Create a nap with the  character as the key and the frequency as the value
  Set the initial frequency to 1
  Add 1 to the count each time the same character is found
  """
  def createFrequencyMap(self,data):
    freqMap = {}
    for character in data:
      if(not character in freqMap ):
        freqMap[character] = 1
      else:
        freqMap[character] += 1
    
    return freqMap

  """
  A callback function used to return the priority from the Node object
  """
  def priorityCallback(self,node):
    return node.priority


  """
  Use a priority queue, specifically a binary min heap, to prioritize/sort the data from the map
  -  create a priority queue then fill it with nodes containing the data from the map. 
  The nodes with the lowest frequencies has the highest priority

  Use the priority queue(min heap), to build a huffman tree(a binary min heap) from the queue:
  remove 2 of the lowest frequency node at a time from the queue.
  then add their frequencies together to produce the frequency for a new node
  Next, add the first node removed as the left child of the new node
  then add the second node removed as the right child of the new node.
  then reinsert the new node into the list. Repeat these steps until only one node remains in the priority queue.

  Note: it takes 0(1) time to add a node to the back of the queue, and  0(1) time to delete a node from the front of the queue, but because the tree has to rebalance itself, insertion and deletion actually takes O(log n) time to complete.

  """
  def huffman_tree(self,frequencyMap):
    #--------------------------------------------
    #build a priority queue - a min Heap of all characters and their frequencies, the min heap will sort the data
    minh = MinHeap(self.priorityCallback)
    for char, freq in frequencyMap.items():
      minh.push(Node(char,freq))


    #--------------------------------------------
    #Merge sets of nodes in heap to create a huffman tree, Repeat until only one node remains in the priority queue.

    while( minh.size()>1):
      #extract two minimum frequency node from min heap
      node1 = minh.pop()
      node2 = minh.pop()

      """
      Create a new internal node with a frequency equal to the sum of the two nodes frequencies. Set the first extracted node as its left child and the other extracted node as its right child. Add this node to the min heap. 
      """

      #create newNode
      newNode = Node()


      #set frequency equal to the sum of the two nodes frequencies
      nPriority = ( node1.get_priority() if node1  else 0) + ( node2.get_priority() if node2  else 0)

      if(nPriority>0):
        newNode.set_priority(nPriority)

        #Set the first extracted node as the left child 
        newNode.set_left_child(node1)

        #Set the other extracted node as the right child
        newNode.set_right_child(node2)

        #add newNode to the min heap. 
        minh.push(newNode)

    return minh


  """
  Create the binary pattern for each character by tracing a path to its node from the root
  """
  def mapCode(self, tree):
    root = tree.peekTop()
    current_code = ""
    codes={}
    self.mapCodeFun(root, current_code,codes)

    return codes
  

  #--------------------------------------------
  """
  Create the encoding for each character by tracing a path to its node from the root 
    • Starting from the root, trace the path to each leaf
    • Everytime a left node is found, append a 0
    • Everytime a right node is found, append a 1
    • Stop creating the code when a leaf node is reached. 
  The result at each leaf is its Huffman encoding

  @param Node node The Node
  @param str current_code The string used to build the code for the leaf node
  @param dict codes The master dictionary of codes
  """
  def mapCodeFun(self, node, current_code,codes):
    if(node == None):
      return
    #only leaf nodes are assigned a code
    if(node.isLeaf()):
      codes[node.value] = current_code
      return

    self.mapCodeFun(node.left, current_code + "0",codes)
    self.mapCodeFun(node.right, current_code + "1",codes)

  def switchCharWithBinaryCode(self,data,heap):
    codeMap = self.mapCode(heap)

    encoding = ''
    for char in data:
        encoding += codeMap[char]
    return encoding

  def huffman_encoding(self,data):

    #build frequency map
    freqMap = self.createFrequencyMap(data)

    #create hoffman Tree
    tree = self.huffman_tree(freqMap)

    encoded_data = self.switchCharWithBinaryCode(data,tree)
    
    return encoded_data, tree


  """
  Use the encoded data to traverse the tree
  Each bit is used to walk the tree until a leaf node is found
  When a leaf is found, a letter is retrieved, and the hunt for another letter begins again starting with the root of the tree

   @param str data The data to be encoded
   @param Minheap tree The tree containing the characters and their frequencies
  """
  def huffman_decoding(self,data,tree):
    decoded_data = ''

    #Start searching the tree at the root node
    node = tree.peekTop()

    """
    loop through all the bits in the data
      when a 0 is found, get the node at the left side
      when a 1 is found, get the node at the right side
      When a leaf node is found, restart the search
    """
    for bit in data:
      if int(bit) == 0:
        if node.left :
          node = node.left
      else:
        if node.right :
          node = node.right

      #Stop searching the tree, a character is found
      if node.isLeaf():
        #A leaf node is found, retrieve the character stored in the node
        decoded_data += node.value
        
        #Go back to the root of tree - the search for another charcter is about to start
        node = tree.peekTop()

    return decoded_data






if __name__ == "__main__":
    #------------------------------------------
    """
        verify the data
    """
    def run_example_verify_data():

        hc = HuffmanCoding()

        a_great_sentence = "The bird is the word"


        print ("\n\nThe size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = hc.huffman_encoding(a_great_sentence)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is:\n{}\n".format(encoded_data))

        decoded_data = hc.huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is:{}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
        #--------------------------------------------



    """
        Uncomment the run_example_verify_data function to view the data,
        run by calling the command below
    """
    run_example_verify_data()


    #------------------------------------------

    """
        run test cases by calling the commands below:
        --basic testing mode
        python tests_3.py

        --Verbose testing mode
        python -m unittest -v tests_3.TestHuffmanCoding
    """