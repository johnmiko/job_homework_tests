########## Start ##########
"""
take a list/array of user objects
return a list of the ids of the user admins
object
    - id
    - admin - boolean
"""
obj_list = []
admins = []


def get_ids_given_admin_objs(obj_list):
    return [obj.id if obj.admin for obj in obj_list]


obj_list = None
admins = get_ids_given_admin_objs(obj_list)
with Exception():
    assert get_ids_given_admin_objs(obj_list)


class Obj:
    def __init__(self, id, admin):
        self.id = id
        self.admin = admin


obj1 = Obj(None, None)
obj1 = Obj('invalid id', None)
obj1 = Obj()
obj_list = [obj1]


########## End   ##########

########## Start ##########
# Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13….
#
# It is created by adding together the two previous numbers in the sequence.
#
# Write a function that takes position/index and returns the value at that point in the sequence
#
# fibonacci(0) = 1
# fibonacci(1) = 1
# fibonacci(2) = 2
# fibonacci(4) = 5
# fibonacci(6) = 13

def fibonacci(index):
    # Give me the 0th element, the 6th element
    # So if I pass in 0, need to return 1
    # Then 1 is 1
    # 2 is 2
    # 3 is 3
    # 4 is 5
    # prev_2 = 1
    # prev_1 = 1
    prev = [1, 1]
    if index == 0:
        return 1
    if index == 1:
        return 1
    # It is created by adding together the two previous numbers in the sequence.
    for i in range(2, index + 1):
        print(prev[-1])
        prev = [prev[0], prev[0] + prev[1]]
    return prev[-1]


val = fibonacci(0)
assert val == 1
val = fibonacci(1)
assert val == 1
val = fibonacci(2)
assert val == 2
val = fibonacci(4)
assert val == 5

########## End   ##########
########## Start ##########
########## End   ##########
########## Start ##########
########## End   ##########
