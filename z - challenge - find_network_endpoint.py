# Question: Given a network of nodes, find the endpoint
# Note: I believe I wasn't able to solve this one in 30 minutes
# Can't remember the edge case conditions exactly, this was one of them
# Edge cases
# - If a circle, report the last item in the circle
# The inputs say, starting at node 1, what is the endpoint?
# 1 is connected to 3, 3 is connected to 4, 4 is connected to 6, answer should be
# In this example, the line that connects node 7 to 3 is not used
# find_network_endpoint(1,[1,7,3,4],[3,3,4,6])

def find_network_endpoint(start_node_id, from_ids, to_ids):
    the_index = from_ids.index(start_node_id)
    visited = [start_node_id]
    went_to = the_index
    while True:
        try:
            went_to = to_ids[the_index]
            the_index = from_ids.index(went_to)
            if the_index in visited:
                return went_to
            visited.append(the_index)
        except ValueError:
            return went_to
    return went_to


# Ignore and do not change the code below
result = find_network_endpoint(1, [1, 7, 3, 4], [3, 3, 4, 6])
print(result)
