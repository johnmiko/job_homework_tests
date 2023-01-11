# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y):
    # write your code in Python 3.8.10
    """
    given array of fractions, convert to floats, count occurences?
    need to round the floats I guess
    just check if they are almost equal
    or round to like 7 decimal places
    which fraction occurs most often    
    """
    fractions = [round(x / y, 12) for x, y in zip(X, Y)]
    unique_fractions = list(set(fractions))
    max_count = 1
    for fraction in unique_fractions:
        cur_max = fractions.count(fraction)
        if cur_max > max_count:
            max_count = cur_max
    return max_count

