def closest_to_zero(ints):
    # Your code goes here
    # John Miko's answer
    if ints is None:
        return 0
    if not ints:
        return 0
    answers = [ints[0]]
    for i in ints[1:]:
        if abs(i) < abs(answers[0]):
            answers = [i]
        elif abs(i) == abs(answers[0]):
            answers.append(i)
    answer = max(answers)
    print(answer)
    return answer


# Question, write a function, given a list of numbers, that returns the number closest to 0
# Edge cases: return 0 if input is None, return 0 if list is empty
ab = closest_to_zero([1, 2])
ab = closest_to_zero([3, 2])
ab = closest_to_zero([-1, 2])
ab = closest_to_zero([-2, 2, -2])
ab = closest_to_zero([4, 4, 3])
