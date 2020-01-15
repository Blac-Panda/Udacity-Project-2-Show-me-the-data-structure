from printBTree import printBTree

class Node:
  def __init__(self, value=None, priority=None):
    self.value = value
    self.priority = priority
    self.left = None;
    self.right = None

  def set_value(self,value):
        self.value = value
        
  def get_value(self):
      return self.value

  def set_priority(self,priority):
        self.priority = priority
        
  def get_priority(self):
      return self.priority 

  def set_left_child(self,left):
      self.left = left
      
  def set_right_child(self, right):
      self.right = right
      
  def get_left_child(self):
      return self.left
  
  def get_right_child(self):
      return self.right

  def has_left_child(self):
      return self.left != None
  
  def has_right_child(self):
      return self.right != None

  def isLeaf(self):
    return self.left is None and self.right is None

  
  # define __repr_ to decide what a print statement displays for a Node object
  def __repr__(self):
      return f"Node(priority: {self.priority},value:{self.get_value()}, left: {self.left}, right: {self.right})"
  
  def __str__(self):
      return f"Node(priority: {self.priority},value:{self.get_value()}, left: {self.left}, right: {self.right})"


  def printTree(self):   
    printBTree(self,lambda n:((str(n.value) if n.value else "") + ("("+ str(n.priority)+")" if n.value else str(n.priority)),n.left,n.right))        