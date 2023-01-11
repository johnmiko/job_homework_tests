"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network
that uses the Internet Protocol for communication. There are two versions of the Internet protocol,
and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
solution(inputString) = true;

For inputString = "172.316.254.1", the output should be
solution(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
solution(inputString) = false.

There is no first number.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of digits, full stops and lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 30.

[output] boolean

true if inputString satisfies the IPv4 address naming rules, false otherwise.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name

"""
import ipaddress


def solution(inputString):
    # Question is tricky to answer because it does not specify what a valid IPv4 address is
    # Googling what the format should be makes me think that inputString: "64.233.161.00" is valid
    # So, bad question
    # Because of this, I'm going to rely on a python library as I don't know what makes an IPv4 address valid or not
    #
    # From google, but the test fails for inputString: "64.233.161.00".... so not sure what's going on
    # An IPv4 address has the following format: x . x . x . x
    # where x is called an octet and must be a decimal value between 0 and 255.
    try:
        ipaddress.IPv4Network(inputString)
        return True
    except ValueError:
        return False

    # parts = inputString.split('.')
    # if len(parts) != 4:
    #     return False
    # for part in parts:
    #     if not part.isdigit():
    #         return False
    #     if int(part) < 0:
    #         return False
    #     if int(part) > 255:
    #         return False
    # return True
