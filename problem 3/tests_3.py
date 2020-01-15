# https://docs.python.org/3/library/unittest.html
import unittest
from problem_3 import HuffmanCoding

class TestHuffmanCoding(unittest.TestCase):

	"""
	The final node frequency/priority will equal the total number of characters in the string
	"""
	def test_tree_root_priority_same_as_length_of_data(self):
		#--------------------------------------------
		hc = HuffmanCoding()

		data = "The bird is the word"
		

		#build frequency map
		freqMap = hc.createFrequencyMap(data)

		#create hoffman Tree
		tree = hc.huffman_tree(freqMap)



	
		codeMap = hc.mapCode(tree)

		#print("\nFrequencyMap:\n{\n" + "\n".join("{!r}: {!r}".format(k, v) for k, v in freqMap.items()) + "\n}")
		#print("\nCodeMap:\n{\n" + "\n".join("{!r}: {!r}".format(k, v) for k, v in codeMap.items()) + "\n}")

		print ("\n\n\n\n{:<12} {:<13} {:<20}".format('Character','Frequency','Binary Code'))
		print ("{:<12} {:<13} {:<20}".format('_________','_________','____'))
		for k, v in codeMap.items():
			frequency = freqMap[k]
			print ("{:<12} {:<13} {:<20}".format(k, frequency, v))


		#--------------------------------------------
		root = tree.peekTop()
		self.assertEqual(len(data),root.get_priority())		

		#print a diagram of the tree
		print ("\n\n\n\n")
		root.printTree()



	"""
	The binary code created for characters with the same set of frequency will be the same.
	"""
	def test_different_data_same_frequency_count(self):
		hc = HuffmanCoding()

		data1 = "dog"
		data2 = "cat"
		
		#build frequency map
		freqMap1 = hc.createFrequencyMap(data1)

		#create hoffman Tree
		tree1 = hc.huffman_tree(freqMap1)

		#create code map
		codeMap1 = hc.mapCode(tree1)


		#build frequency map
		freqMap2 = hc.createFrequencyMap(data2)

		#create hoffman Tree
		tree2 = hc.huffman_tree(freqMap2)

		#create code map
		codeMap2 = hc.mapCode(tree2)


		root1 = tree1.peekTop()
		root2 = tree2.peekTop()

		#print a diagram of the tree
		print ("\n\n\n\n")
		root1.printTree()

		print ("\n\n\n\n")
		root2.printTree()

		self.assertEqual(codeMap1.values(),codeMap2.values())


#----------------------------------------------------
if __name__ == '__main__':
    unittest.main()