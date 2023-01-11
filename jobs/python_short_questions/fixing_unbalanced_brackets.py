def solution(angles):
    # Type your solution here
    """
    Need to match brackets, cases
    < - immediately insert >
    > - before
    oh can only add to start and end
    so question is how many to add to start and how many to add to end
    Go through angles, find imbalance, calculate it
    check bracket, see if it is balanced, if not need to adjust
    we know if it's balanced if it has a corresponding closing tag
    > - insert <
    < - append to end
    <<
    <> it's recursive
    < - check if next is >
        if <, check if next is >

    """
    new_angles = angles[:]
    try:
        add_to_start = angles.index('<')
    except ValueError:
        add_to_start = len(angles)
    r_angles = angles[::-1]
    try:
        add_to_end = r_angles.index('>')
    except ValueError:
        add_to_end = len(angles)
    if add_to_end == 0:
        unbalanced = angles[add_to_start:]
    else:
        unbalanced = angles[add_to_start:-1 * add_to_end]
    balance = 0
    i = 0
    if (angles == '<') or (angles == '>'):
        return '<>'
    while i < len(unbalanced) - 1:
        # print(unbalanced[i:])
        if (unbalanced[i] == '<') and (unbalanced[i + 1] == '<'):
            balance += 1
        elif (unbalanced[i] == '>') and (unbalanced[i + 1] == '>'):
            balance -= 1
        i += 1
    if balance > 0:
        add_to_end += balance
    else:
        add_to_start += abs(balance)
    new_angles = add_to_start * '<' + new_angles + add_to_end * '>'
    return new_angles


print(f'solution("<") == "<>": {solution("<") == "<>"}')
print(f'solution(">") == "<>": {solution(">") == "<>"}')
print(f'{solution("<>") == "<>"}')
print(f'{solution("<<") == "<<>>"}')
print(f'{solution(">>") == "<<>>"}')
print(f'{solution(">>") == "<<>>"}')
print(f'{solution("<<>") == "<<>>"}')
print(f'{solution("<<>>") == "<<>>"}')
print(f'{solution("<<<>>") == "<<<>>>"}')
print(f'correct: {solution(">><<>>><<<") == "<<<>><<>>><<<>>>"}')
