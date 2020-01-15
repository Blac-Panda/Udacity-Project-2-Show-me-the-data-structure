# https://docs.python.org/3/library/unittest.html
import unittest
from problem_6 import *




class TestUnionIntersection(unittest.TestCase):
    def setUp(self):
        #--------------------------
        self.lst_a = [1,2,3,4,5,5]
        self.lst_b = [4,4,5,6,6]


        self.lnk1 = LinkedList()
        for item in self.lst_a:
            self.lnk1.append(item)


        self.lnk2 = LinkedList()
        for item in self.lst_b:
            self.lnk2.append(item)




    def test_intersection_both_contains_data(self):
        """
        Do intersection when linkedList 1 and linkedList 2 contains data
        """

        #  [4,5]
        intrsectLnkLst = intersection(self.lnk1,self.lnk2) 

        lst = intrsectLnkLst.getList()
        lst.sort()
        self.assertEqual([4,5],lst)


    def test_intersection_first_list_empty(self):
        """
        Do intersection when linkedList 1 is empty
        """

        #empty list
        intrsectLnkLst = intersection(LinkedList(),self.lnk2) 
        print(intrsectLnkLst)

        self.assertEqual(len(intrsectLnkLst.getList()) , 0)


    def test_intersection_second_list_empty(self):

        """
        Do intersection when linkedList 2 is empty
        """
        #empty list
        intrsectLnkLst = intersection(self.lnk1,LinkedList())
        print(intrsectLnkLst)

        self.assertEqual(len(intrsectLnkLst.getList()) , 0)


    def test_union_both_contains_data(self):
        """
        Do union when linkedList 1 and linkedList 2 contains data
        """

        # [1, 2, 3, 4, 5, 6]
        unionLnkLst = union(self.lnk1,self.lnk2)

        lst = unionLnkLst.getList()
        lst.sort()
     
        self.assertEqual([1, 2, 3, 4, 5, 6],lst)



#add union test soon
   
#----------------------------------------------------
if __name__ == '__main__':
    unittest.main()