# https://docs.python.org/3/library/unittest.html
import os

import unittest
from problem_2 import FileRecursion

class TestFileRecursion(unittest.TestCase):
    def test_file_ends_withwith_suffix_py(self):
        path   = "./testdir";
        suffix = ".py"


        # Locally save and call this file
        filename = "ex.py"
        filePath = os.path.join(path, filename)
        text = "#this is a temp file"
        with open(filePath, 'w') as temp_file:
            temp_file.write(text)

        

        # Let us print the files in the directory in which you are running this script
        # print (suffix, path, os.listdir(path))

        # Let us check if this file is indeed a file!
        self.assertTrue(os.path.isfile(filePath))

        # Does the file end with .py?
        self.assertTrue(filePath.endswith(suffix))

        os.remove(filePath);



    def test_get_list_of_all_file_and_dir(self):

        path   = "./testdir";
        suffix = None

        ff    = FileRecursion();
        files = ff.find_files(suffix, path)


        self.assertEqual(10, len(files))


    def test_get_list_of_all_files_with_suffix_c(self):

        path   = "./testdir";
        suffix = ".c"

        ff    = FileRecursion();
        files = ff.find_files(suffix, path)


        self.assertEqual(4, len(files))




#----------------------------------------------------
if __name__ == '__main__':
    unittest.main()