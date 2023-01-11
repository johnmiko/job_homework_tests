#!/bin/python3

import os

#
# Complete the 'deliveryPlan' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY allLocations
#  2. INTEGER numDeliveries
#
import math


def deliveryPlan(allLocations, numDeliveries):
    # print(allLocations)
    # print(numDeliveries)
    # Write your code here
    distances = []
    for location in allLocations:
        squares_sum = location[0] ** 2 + location[1] ** 2
        # print('squares_sum')
        # print(squares_sum)
        root = math.sqrt(squares_sum)
        # print(root)
        distances.append(root)
        # print(distances)
    # have distances, need to return the smallest distance
    locationsSorted = [x for _, x in sorted(zip(distances, allLocations))]
    # print(locationsSorted)
    return locationsSorted[:numDeliveries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    allLocations_rows = int(input().strip())
    allLocations_columns = int(input().strip())

    allLocations = []

    for _ in range(allLocations_rows):
        allLocations.append(list(map(int, input().rstrip().split())))

    numDeliveries = int(input().strip())

    result = deliveryPlan(allLocations, numDeliveries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
"""
answers and inputs
[[1, -3], [1, 2], [3, 4]]
1
expected output 1 2

[[3, 6], [2, 4], [5, 3], [2, 7], [1, 8], [7, 9]]
3
exepcted output
2 4
3 6
5 3
"""
