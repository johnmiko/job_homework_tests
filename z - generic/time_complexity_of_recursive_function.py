def print_all_codes(n, m):
    print(f'n={n},m={m}')

    # iterate thru this 2n times
    def print_01_codes(current, num_digits, prints=[]):
        if num_digits == 0:
            print(current)
            prints.append(current)

        else:

            print_01_codes('0' + current, num_digits - 1, prints)

            print_01_codes('1' + current, num_digits - 1, prints)
        return prints

    upper_bound = 0
    # iterate thru this m times
    # always using n as input,
    while True:

        for i in range(upper_bound):
            prints = print_01_codes('', n)

        if upper_bound > m:
            break

        upper_bound += 1
    print(f'{len(prints)} numbers printed')


# 2^n,m
# 2n,m
# n*O(1) = O(n^2*((m^2+m)/2)
# Number of iterations
# print_all_codes(0, 0)  # nothing
# print_all_codes(1, 0)  # 2
# print_all_codes(2, 0)  # 4
# print_all_codes(3, 0)  # 8
# print_all_codes(0, 1)  # 3 calls the function 3 times, because values are 0, then 0,1,
# print_all_codes(0, 2)  # 6, 0, 0-1, 0,1,2 (m+1)!+ binomial coefficient
# print_all_codes(0, 3)  # 10
# print_all_codes(1, 1)  # 6
# print_all_codes(2, 1)  # 12
# print_all_codes(3, 1)  # 24
# print_all_codes(1, 2)  # 12
# print_all_codes(2, 2)  # 24
# print_all_codes(3, 2)  # 48

"""
O(n^2+((m^2+m)/2)

"""
