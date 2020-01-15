import os

class FileRecursion:
 
    def __init__(self):
        self.list = []

    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories.

    Args:
      suffix(str): the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    def find_files(self,suffix, path):
      self._find_files_helper(suffix, path)
      return self.list


    def _find_files_helper(self,suffix, path):
        dirListing = os.listdir(path)

        if(path == None):
            return

        for entry in dirListing:
            entryPath = os.path.join(path, entry)

            if os.path.isdir(entryPath):
                self._find_files_helper(suffix,entryPath)

            elif os.path.isfile(entryPath) and (suffix is None or entry.endswith(suffix)):
                self.list.append(entryPath)



#------------------------------------------
if __name__ == "__main__":
    

    """
        verify the data
    """
    def run_example_verify_data():
        path   = "./testdir";
        suffix = ".c"


        ff = FileRecursion();
        files = ff.find_files(suffix, path)

        print(*files, sep='\n')

    """
        Uncomment the run_example_verify_data function to view the data,
        run by calling the command below
    """
    run_example_verify_data()


    #------------------------------------------

    """
        run test cases by calling the commands below:
        --basic testing mode
        python tests_2.py

        --Verbose testing mode
        python -m unittest -v tests_2.TestFileRecursion
    """