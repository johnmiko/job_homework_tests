# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# Just strip out the "dashes and spaces"

def solution(S):
    s1 = S.replace(' ', '').replace('-', '')
    # Last block has to be 2 or 3 digits long
    # Can not be 1 digit long
    # Try splitting every 3 characters, if the last digit is 1 long, then group te last 2 and split again
    n = 3
    s2 = [s1[i:i + n] for i in range(0, len(s1), n)]
    if len(s2[-1]) < 2:
        s3 = s3 = s2[0:-2] + [s2[-2][0:2]] + [s2[-2][2] + s2[-1]]
    else:
        s3 = s2
    return '-'.join(s3)


# question: Put the below strings in to correct phone number formats

s = '00-44  48 5555 8361'
s = '0 - 22 1985--324'
s = '01'
answer = solution(s)
print(answer)
