# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from timeit import default_timer as timer


def solution1(N, A, B):
    cons = []
    for i in range(len(A)):
        if A[i] < B[i]:
            cons.append([A[i], B[i]])
        else:
            cons.append([B[i], A[i]])

    for i in range(1, N):
        line = [i, i + 1]
        if line in cons:
            continue
        else:
            return False
    return True


def solution2(N, A, B):
    cons = list(zip(A, B))
    for i in range(1, N):
        line1 = (i, i + 1)
        line2 = (i + 1, i)
        if (line1 in cons) or (line2 in cons):
            continue
        else:
            return False
    return True


def solution3(N, A, B):
    cons = list(zip(A, B))
    for i in range(1, N):
        line1 = (i, i + 1)
        line2 = (i + 1, i)
        if (line1 in cons) or (line2 in cons):
            continue
        else:
            return False
    return True


import random

# Generate 5 random numbers between 10 and 30
M = 10000
N = 8000
A = [random.randrange(1, M, 1) for i in range(M)]
B = [random.randrange(1, M, 1) for i in range(M)]
# N, A, B = (4, [1, 2, 4, 4, 3], [2, 3, 1, 3, 1])
start = timer()
answer = solution1(N, A, B)
end = timer()
print(f'solution1: {end - start}')
start = timer()
answer = solution2(N, A, B)
end = timer()
print(f'solution2: {end - start}')
