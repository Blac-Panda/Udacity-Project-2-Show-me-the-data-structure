# Explanation for Problem 6: Union and Intersection of Two Linked Lists
**Author:** Moya Richards

This document provides a text explanation of the efficiency of the code and the design choices.

------------

------------


## Project Summary
|  | Summary Details |||
| -------------- | --------------- | ---------------- |---------------- |
| Efficiency |time complexity|space complexity|Information|
| Union | O(m+n) | O(m+n) |m is the first list, n is the second list|
| Intersection | O(m+n) | O(s) | where s is the shortest list, and the shortest list is a subset of the longest list|



## Design Choices

- Created a Node class
- Created a LinkedList class which contains a head and tail. 
-- The head tracks the first item added to the list
-- The tail tracks the last item added to the list


### Data Structures Used



#### Union
The Union is about combining both linkedlist into a new list

| Data Structure | Time Complexity | Space Complexity |
| -------------- | --------------- | ---------------- |
| LinkedList |O(m+n)|O(m+n) |
| dictionary |O(1)| O(m+n) | 


 - The LinkedList being joined together are not modified. A new linkedList is created with the data from both list.

 - A dictionary is used to keep track of duplicate data in the list. When data is added to the list, it's value is set to True, so that if it is encountered again, it will be skipped. Note that if the data does not exists in the list it's value is assumed to be false. The order of the items in the list does not matter


**Steps:**
- Create a new LinkedList to store all the data from both list
- Create a dictionary to keep track of duplicates
- If the first list is not empty traverse it  - [ **O(m+n) time complexity** ]
- Remove duplicates - [ **O(1) time complexity** ]
    find the data in the dictionary and get its value
    if data does not exists in the dictionary, its default value is False,this means that the data has not been added to the new LinkedList.
      Add the data to the new LinkedList
      Add the data to the dictionary, set its value to True so that if the same data is being added again to the list it will be skipped.
- Return a combination of both list with duplicates removed.





#### Intersection
This intersection is about finding the list of nodes each linkedlist have in common

| Data Structure | Time Complexity | Space Complexity |
| -------------- | --------------- | ---------------- |
| LinkedList |O(m+n)| O(s) |where s is the shortest list, and the shortest list is a subset of the longest list
| dictionary |O(1)| O(s) |where s is the shortest list, and the shortest list is a subset of the longest list


**Steps:**
- Created a new LinkedList to store the data each list have in common
- Create a dictionary to keep track of common data and duplicates
- Find the shortest and the longest linkedList from the input values
- Traverse the shortest list - [ **O(m) time complexity** ]
    - Add all of its data to a dictionary as the key, set the value to False. False indicate that the data does not exist in the second/longer list
- Traverse the longer list - [ **O(n) time complexity** ]
    - If the data does not exist in the map, skip it because it does not exist in the first list.
- Ignore duplicates - [ **O(1) time complexity** ]
    - If the data exist in the dictionary and the value is False
        - Add the data to the new LinkedList
        - Set the value in the dictionary to True so that if the same data is being added to the list again it will be skipped.
- Return an empty list if there is no intersection or return a list of only common nodes

------------

------------
## Udacity Project Requirement
> **Union and Intersection of Two Linked Lists**

Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:


### Node
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

```

### LinkedList
```python
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    pass

def intersection(llist_1, llist_2):
    # Your Solution Here
    pass


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

```

