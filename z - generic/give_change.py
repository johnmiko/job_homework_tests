# Use print("messages...") to debug your solution.
from math import floor


# Question: Write code that given a value of cash, outputs the number bills that make up that number
# given bills of tens, fives, and twos

def change(cash):
    # Your code goes here
    # John Miko's solution
    tens = floor(cash / 10)
    cash2 = cash - (tens * 10)
    fives = floor(cash2 / 5)
    cash3 = cash2 - (fives * 5)
    twos = floor(cash3 / 2)

    if (tens == 0) and (fives == 0) and (twos == 0):
        print('None')
        return 'None'
    print(f'tens {tens}')
    print(f'fives {fives}')
    print(f'twos {twos}')
    print()
    return {
        'two': twos,
        'five': fives,
        'ten': tens
    }


change(42)
"""
tens 4
fives 0
twos 1
"""
