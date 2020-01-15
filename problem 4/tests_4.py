# https://docs.python.org/3/library/unittest.html
import unittest
from problem_4 import *

class TestGroup(unittest.TestCase):

  """
        (group:0)
        /         \
    [user-0]    (group:1)
                  /       \
                  [None]   (group:2)
                          /         \
                        [None]       (group:3)
  """
  def test_find_user_in_last_group(self):

    groups = []
    groups.append(Group("group:0"))

    for level in range(1,4):

      grp = Group("group:{}".format(level))
      groups.append(grp)

      #add group as a child of the previous group
      groups[level-1].add_group(grp)

    user0 = "user-0"
    parent = groups[0]
    lastgroup = groups[-1]
    lastgroup.add_user(user0)

    self.assertTrue(is_user_in_group(user0, lastgroup)) #True





  """
        (group:0)
        /         \
      [None]       (group:1)
                  /       \
                  [None]  (group:2)
                          /         \
                        [None]       (group:3)
                                    /        \
                                  [user-0]  (None)
                                  [user-1]
  """
  def test_find_user_in_parent_and_last_group(self):

    groups = []
    groups.append(Group("group:0"))

    for level in range(1,4):
      #create group
      grp = Group("group:{}".format(level))

      #add group to list
      groups.append(grp)

      #add group as a child of the previous group
      groups[level-1].add_group(grp)

    user0 = "user-0"
    user1 = "user-1"
    parent = groups[0]
    lastgroup = groups[-1]
    lastgroup.add_user(user0)
    lastgroup.add_user(user1)

    #print("\n------------------\n",groups)
    self.assertTrue(is_user_in_group(user0, parent)) #True
    self.assertTrue(is_user_in_group(user1, lastgroup)) #True



  """
        (group:0)
        /         \
      [None]      (group:1)
                  /       \
                  [None]   (group:2)
                          /         \
                        [None]       (group:3)
                                    /        \
                                  [user-0]    (group:4)    
                                              /        \
                                             [None]    (None)


  """
  def test_user_not_in_group(self):

    groups = []
    groups.append(Group("group:0"))

    for level in range(1,5):
      #create group
      grp = Group("group:{}".format(level))
      #add group to list
      groups.append(grp)

      #add group as a child of the previous group
      groups[level-1].add_group(grp)

    user0 = "user-0"
    user1 = "user-1"

    parent = groups[0]
    lastgroup = groups[-1]

    groups[2].add_user(user0)
  
    #print("\n------------------\n",groups)
    self.assertEqual(False,is_user_in_group(user1, parent))    #False
    self.assertEqual(False,is_user_in_group(user1, groups[2])) #False
    self.assertEqual(False,is_user_in_group(user1, lastgroup)) #False






#----------------------------------------------------
if __name__ == '__main__':
    unittest.main()