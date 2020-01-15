import math


"""
                  root at 0       root at 1
Left child        2*index + 1     2*index
Right child       2*index + 2     2*index + 1
Parent            (index-1)/2     index/2
"""

class MinHeap():
  def __init__(self, priorityCallback):
    self.content = []
    self.priorityCallback = priorityCallback


  """
  Insert in the list
    1. Add element at the end of the list.
    2. Move element up (bubble) the list
  """
  def push(self,element):
    self.content.append(element)
    index = len(self.content) - 1
    self.bubbleUp(index)




  """
  Performed after a push
  Move the last element added closer to the top of the list
  """
  def bubbleUp(self,index):
    #get the data for the current element
    element = self.content[index]
    elementPriority = self.priorityCallback(element)

    #Stop bubbling when the root is reached
    while(index > 0):
      #get the parent index
      parentIndex = math.floor((index-1)/2)

      #get parent data
      parent = self.content[parentIndex]

     
      """
      check priority of parent vs current element
      If inserted element is smaller than its parent node in case of Min-Heap OR greater than its parent node in case of Max-Heap, swap the element with its parent.
      Keep repeating the above step, if node reaches its correct position, STOP.
      """

      #minheap priority - check if root element is smaller than parent
      if(elementPriority < self.priorityCallback(parent)):
        #swap the element with its parent
        self.content[parentIndex] = element;
        self.content[index] = parent;
        
        #bubble up by making the parent index the next index 
        index = parentIndex;
      else:
        break

  """
    queue -> back  : lst[0]
    queue -> front : lst[len(lst) -1]
  """
  def pop(self):
    #data is removed from the Back of the queue
    #get the data from the front - the root element at index 0
    front = None

    if not self.isEmpty():
      front = self.content[0]

      #get the data from the Rear - the element in the last position in the list 
      rear = self.content.pop()

      """
        If more than 1 element exist in the list.
        move the last item to the root position
        then push it down the list, until it finds the correct spot
      """
      if(len(self.content)> 0):
        self.content[0] = rear
        self.sinkDown(0);

    return front

  """
  Performed after a pop
  check priority of child elements vs current element
  If root element is larger than a child node in case of Min-Heap OR smaller than a child node in case of Max-Heap, swap the element with the child.
  Keep repeating the above step, if node reaches its correct position, STOP.
  """
  def sinkDown(self,index):
    length = len(self.content);
    element = self.content[index]

    elementPriority = self.priorityCallback(element)

    while(True):
          left = None
          leftPriority = None

          right = None
          rightPriority = None

          #Find the left child
          leftIndex = 2*index + 1

          #find the right child
          rightIndex = 2*index + 2

          swapIndex = None

          if leftIndex < length:
            left = self.content[leftIndex]
            leftPriority = self.priorityCallback(left)

            #minheap priority - check if root element is larger than left child node
            if(elementPriority > leftPriority):
              swapIndex = leftIndex

          if rightIndex < length:
            right = self.content[rightIndex]
            rightPriority = self.priorityCallback(right)

            #minheap priority - check if root element is larger than right child node
            if(elementPriority > rightPriority and rightPriority <leftPriority):
              swapIndex = rightIndex
          
          #Do anything if there is nothing to swap
          if(swapIndex == None):
            break

          #Otherwise, swap and continue.
          self.content[index] = self.content[swapIndex];
          self.content[swapIndex] = element;

          #move down by making the swapindex the new index
          index = swapIndex;
    
  def isEmpty(self):
    return (len(self.content) == 0)

  def size(self):
    return len(self.content)
  
  def getHeap():
    return self.content
  
  def peekTop(self):
    return self.content[0] if not self.isEmpty() else None

  # define __repr_ to decide what a print statement displays for a heap object
  def __repr__(self):
      return f"heap({self.content})"
  
  def __str__(self):
      return f"heap({self.content})"

