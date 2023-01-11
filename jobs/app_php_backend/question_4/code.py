def f(first, second):
    print(f'first', first)
    print(f'second', second)
    if first == 0:
        return second
    else:
        return f(first - 1, second + 1)


# Please give an exact definition of what this code does
# The result of this function is that it returns the addition of the first and second integer. How it does this is by recursively calling itself, incrementally subtracting 1 from the first integer and adding 1 to the second until the first integer is 0

print(f(3, 4))
