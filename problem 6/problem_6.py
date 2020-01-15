class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

    
  def __repr__(self):
    return f"Node(data: {self.data})"

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def append(self, data):
    
    node = Node(data)
    if(self.head == None):
      self.head = node
      self.tail = self.head
    else:
      self.tail.next = node
      self.tail = node

    self.size +=1

  def getSize(self):
    return self.size

  """
  Create an object generator to return a node when a loop is used
  The loop starts at head of the linkedlist
  """
  def __iter__(self):
    if self.size == 0:
      return

    node = self.head

    while node:
      yield node
      node = node.next


  """
  Use to get the entire list by looping through the link list
  @see __iter__
  """
  def getList(self):
    elem = []
    for n in self:
      elem.append(n.data)
    return elem


  def __repr__(self):
      output = ''
      for n in self:
          output += str(n) + "\n"
      return output

  def __str__(self):
      output = ''
      for n in self:
          output += str(n) + "\n"
      return output




#--------------------------
def intersection(lnk1,lnk2):
  mapData = {}
  intrsectLnkLst = LinkedList()

  """
  Ensure that intersection is only performed when both LinkedList contains data
  """
  if lnk1 and lnk2 :

    fst, snd = (lnk1, lnk2) if lnk1.getSize() < lnk2.getSize() else (lnk2, lnk1)

    """
    Traverse the first list, had all the data to a map
    False indicates that this data has not been found in another list
    """
    for node in fst:
      mapData[node.data] = False


    for node in snd:
      data = node.data

      # Returns None when a key does not exist
      isDuplicate = mapData.get(node.data)

      # If the data does not exist in the map, skip it because it does not exist in the first list either.
      if isDuplicate != None and not isDuplicate:

        """
        Traverse the second list, check if data is in the map
        If data exists in the map, mark it as a duplicate, by changing its value to True, so that it is not added to the list again
        """

        intrsectLnkLst.append(data)
        mapData[data] = True

    return intrsectLnkLst


"""
A helper inner function to add data to the new linkedList - (variable unionLnkLst)
Uses the variable mapData to keep track of duplicated data
"""
def appendListStripDuplicates(lnkedList,mapData,unionLnkLst):
  if lnkedList : 
    for node in lnkedList:
      data = node.data
      duplicate = mapData.get(node.data, False)
      if not duplicate:
        unionLnkLst.append(data)
        mapData[data] = True

  return (mapData,unionLnkLst)

def union(lnk1,lnk2):
  mapData = {}
  unionLnkLst = LinkedList()
  #-----------------------------------------
  #Traverse the first list, add all the data to the new linkedList
  mapData,unionLnkLst = appendListStripDuplicates(lnk1,mapData,unionLnkLst)
  #Traverse the send list, add all the data to the new linkedList
  mapData,unionLnkLst = appendListStripDuplicates(lnk2,mapData,unionLnkLst)
  #return the new linkedList
  return unionLnkLst




if __name__ == "__main__":















    #------------------------------------------
    """
        verify the data
    """
    def run_example_verify_data():


      #-----------------------------
      # Test case 1

      linked_list_1 = LinkedList()
      linked_list_2 = LinkedList()

      element_1 = [3,2,4,35,6,65,6,4,3,21]
      element_2 = [6,32,4,9,6,1,11,21,1]

      for i in element_1:
          linked_list_1.append(i)

      for i in element_2:
          linked_list_2.append(i)


      u1 = union(linked_list_1,linked_list_2) #combined - duplicates removed - [3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21]
      
      i1 = intersection(linked_list_1,linked_list_2) #intersection


      
      print ("linkedList1 SIZE: ", linked_list_1.getSize()," | content: ",linked_list_1.getList() )
      print ("linkedList2 SIZE: ", linked_list_2.getSize()," | content: ",linked_list_2.getList() )

      print("--------------------------------------------")
      print ("\nunion - linkedList1 U linkedlist2 - SIZE: ", u1.getSize()," | content : ", u1.getList())
      print (u1)

      print("--------------------------------------------")
      print ("\nintersection - linkedList1 U linkedlist2 - SIZE: ", i1.getSize()," | content : ", i1.getList())  
      print (i1)


      #-----------------------------
      # Test case 2

      linked_list_3 = LinkedList()
      linked_list_4 = LinkedList()

      element_1 = [3,2,4,35,6,65,6,4,3,23]
      element_2 = [1,7,8,9,11,21,1]

      for i in element_1:
          linked_list_3.append(i)

      for i in element_2:
          linked_list_4.append(i)


      
      u2 = union(linked_list_3,linked_list_4) #combined - duplicates removed - [3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21]
      
      i2 = intersection(linked_list_3,linked_list_4) #no intersection


      print("\n\n\n*******************************************")
      print ("linkedList3 SIZE: ", linked_list_3.getSize()," | content: ",linked_list_3.getList() )
      print ("linkedList4 SIZE: ", linked_list_4.getSize()," | content: ",linked_list_4.getList() )

      print("--------------------------------------------")
      print ("\nunion - linkedList3 U linkedlist4 - SIZE: ", u2.getSize()," | content : ", u2.getList())
      print (u2)

      print("--------------------------------------------")
      print ("\nintersection - linkedList3 U linkedlist4 - SIZE: ", i2.getSize()," | content : ", i2.getList())  
      print (i2)

      


    #--------------------------------------------

    """
        Uncomment the run_example_verify_data function to view the data,
        run by calling the command below
    """

    run_example_verify_data()


    #------------------------------------------

    """
    python problem_6.py

    run test cases by calling the commands below:
    --basic testing mode
    python tests_6.py

    --Verbose testing mode
    python -m unittest -l -v tests_6.TestBlockchain
    """