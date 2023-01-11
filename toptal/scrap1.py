def solution(A, B, P):
    matches = [s for s in B if P in s]
    indices = [i for i, x in enumerate(B) if x in matches]
    if not indices:
        return "NO CONTACT"
    else:
        smallest = A[indices[0]]
    for index in indices:
        if A[index] < smallest:
            smallest = A[index]
    return smallest


# assert solution(['pim', 'pom'], ['999999999', '777888999'], '88999') == 'pom'
assert solution(['sander', 'amy', 'ann', 'michael'], ['123456789', '234567890', '789123456', '123123123'],
                '1') == 'ann'
assert solution(['adam', 'eva', 'leo'], ['121212121', '111111111', '444555666'], '112') == 'NO CONTACT'
