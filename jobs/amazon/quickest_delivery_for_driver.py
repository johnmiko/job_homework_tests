#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY area as parameter.
#
from collections import defaultdict
from collections import deque


def minimumDistance(area):
    print(area)
    q = deque()
    q.append((0, 0))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    steps = 0
    visited = set()
    visited.add((0, 0))
    while q:
        for i in range(len(q)):
            node = q.popleft()
            x, y = node[0], node[1]

            if area[x][y] == 9:
                return steps
            for direction in directions:
                newX, newY = x + direction[0], y + direction[1]
                # Check if new location is on the map
                if newX >= 0 and newX <= len(area) - 1 and newY >= 0 and newY <= len(area[0]) - 1:
                    # Check if new location is a road
                    if area[newX][newY] != 0:
                        # record new location if it hasn't been visited before
                        # if it has been visited, then this is a longer route that we shouldn't be taking
                        if (newX, newY) not in visited:
                            # Add new location to queue
                            q.append((newX, newY))
                            visited.add((newX, newY))
        steps += 1
    return -1


inputs = [[1, 0, 0], [1, 0, 0], [1, 9, 1]]
answer = 3

inputs = [[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 0, 1], [1, 1, 9, 1], [0, 0, 1, 1]]
answer = 5
