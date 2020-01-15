# https://docs.python.org/3/library/unittest.html
import unittest
from problem_1 import LRU_Cache

class TestLRU_Cache(unittest.TestCase):


    def test_insert_cache_items_added_below_capacity(self):
        """
        """
        our_cache = LRU_Cache(5)

        our_cache.set(1, 1);
        our_cache.set(2, 2);
        our_cache.set(3, 3);
        our_cache.set(4, 4);


        self.assertEqual(4, len(our_cache.cacheStorageMap))
        self.assertTrue(our_cache.capacity > len(our_cache.cacheStorageMap))

    def test_insert_data_in_cache(self):
        our_cache = LRU_Cache(5)

        our_cache.set(1, 1);
        our_cache.set(2, 2);
        our_cache.set(3, 3);
        our_cache.set(4, 4);

        self.assertEqual(1,our_cache.get(1))      # returns 1
        self.assertEqual(2,our_cache.get(2))      # returns 2

    def test_search_cache_nonexistent_data(self):
        our_cache = LRU_Cache(5)

        our_cache.set(1, 1);

        self.assertEqual(-1,our_cache.get(9))     # returns -1 because 9 is not present in the cache


    def test_insert_data_cache_capacity_exceeded(self):
        our_cache = LRU_Cache(5)

        our_cache.set(1, 1);
        our_cache.set(2, 2);
        our_cache.set(3, 3);
        our_cache.set(4, 4);

        #Move items in the cache, so that they are positioned closer to the top if the recently used list
        our_cache.get(1)
        our_cache.get(2)

        our_cache.set(5, 5) 
        our_cache.set(6, 6)

        self.assertEqual(our_cache.get(3),-1)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

        self.assertEqual(list(our_cache.cacheStorageMap.keys()), [1, 2, 4, 5, 6])  # [1, 2, 4, 5, 6] 
#----------------------------------------------------
if __name__ == '__main__':
    unittest.main()