# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.8.10
    unique_chars = list(set(S))
    counts = []
    for character in unique_chars:
        counts.append(S.count(character))
    return max(counts)

    """
    just return length of final array
    I think the answer is to just return the max of count of each char
    
    Given string of letters, find minimum number of strings that have unique letters
    letters cannot be reapeated in string
    
    """
