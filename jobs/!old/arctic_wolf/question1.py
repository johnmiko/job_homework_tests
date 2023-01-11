"""
Question 1 of 5
5:59:46
DESC
RULES
README
SETTINGS
Codewriting

Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
solution(time) = true;
For time = "25:51", the output should be
solution(time) = false;
For time = "02:76", the output should be
solution(time) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string time

A string representing time in HH:MM format. It is guaranteed that the first two characters, as well as the last two characters, are digits.

[output] boolean

true if the given representation is correct, false otherwise.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
"""


def solution(time):
    if int(time[0]) > 2:
        return False
    if (int(time[0]) == 2) and (int(time[1]) > 3):
        return False
    if int(time[3]) > 5:
        return False
    return True
