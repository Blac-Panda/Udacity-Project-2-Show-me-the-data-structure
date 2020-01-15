﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿# Explanation for Problem 2: File Recursion
**Author:** Moya Richards

This document provides a text explanation of the efficiency of the code and the design choices.

------------

------------


## Project Summary
|  | Summary Details |
| -------------- | --------------- |
| Efficiency | O(d + f) time complexity. d is the total number of directories, and f is the total number of files. <br><br>O(n) space complexity. n is the input size calculated from the total number of files in every directory. <br><br>In this specific directory there are 10 files and 7 directories.




## Design Choices

### Data Structures Used


| Data Structure | Time Complexity | Space Complexity |
| -------------- | --------------- | ---------------- |
| list | O(d + f) | O(n) |


I used recursion to complete this project because it makes it easy to search for files when we don't know how many directories we have to search through.

The project requested a list data structure to hold all the files found.
I did not want to keep passing around the list to the recursive function call. So, I created a class with a list instance variable to store the path of the files found. This allowed me to append to the list, instead of concatenating the list.

**Algorithm:**
- Start the search at the top directory.
- Check the path within a  directory to see if it is directory or a file.
- If the path is a directory, recursively search through all it's subdirectories.
- If the path is a file, and the suffix matches, add it to the list.

------------

------------
## Udacity Project Requirement
> **File Recursion**


### Finding Files

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded here:
<pre>
./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
</pre>

**Python's os module will be useful**—in particular, you may want to use the following resources:
```python
os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)
```
Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem ***you are not allowed to use os.walk()***.


**Here is some code for the function to get you started:**

```python
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    return None

```


OS Module Exploration Code

## Locally save and call this file ex.py ##
**Code to work with  files **
```python


# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))

```














