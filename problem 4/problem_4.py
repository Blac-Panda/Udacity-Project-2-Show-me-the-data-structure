class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)
        
    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __repr__(self):
        return f"Group(name: {self.name},\n\tusers: {self.users},\n\tgroups:{self.groups})"



def findUser(user, group):
    """Checks if the user is in the group. If found, returns; else, recursively calls subgroups."""

    if user in group.get_users():
        return True


    for subgroup in group.get_groups():
        #print("checking group-- ", subgroup.get_name())
        return findUser(user, subgroup)
        

    return False


def is_user_in_group(user, group):
    return findUser(user, group)




#------------------------------------------
"""
    verify the data
"""
def run_example_verify_data():


  """
        (parent)
        /        \
      [None]      (child)
                  /      \
                [None]    (sub_child)
                          /          \
                    sub_child_user   (None)
  """



  parent = Group("parent")
  child = Group("child")
  sub_child = Group("subchild")
  sub_child_user = "sub_child_user"
  sub_child.add_user(sub_child_user)

  child.add_group(sub_child)
  parent.add_group(child)

  print("\nIs user in group?\n")
  print(is_user_in_group(sub_child_user, parent)) #true

  print("\nParent Group:")
  print(parent)

"""
    Uncomment the run_example_verify_data function to view the data,
    run by calling the command below
"""
run_example_verify_data()


#------------------------------------------

"""
    run test cases by calling the commands below:
    --basic testing mode
    python tests_4.py

    --Verbose testing mode
    python -m unittest -v tests_4.TestGroup
"""