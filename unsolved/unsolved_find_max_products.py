# def findMaxProducts(products):
#     # Write your code here
#     """
#     Notes
#     stack products
#     n piles = length of products
#     amount in each pile is the values in the list products
#     get any sub array
#     okay I see
#
#     Find the largest continuous sublist in the list where we can get the total number of products
#
#     so given 2,9,4,7,5,2
#     we can try doing 2,3,4,7
#     so we want to sum from left to right
#     to get all possible combinations we want to start with 1 and increase?
#     """
#
#     print(products)
#     maxProducts = max(products)  # get easiest case first
#     counts = [max(products)]
#     index = 0
#     index1 = 1
#     best_count = products[0]
#     while index < (len(products) - 2):
#         col_left = products[index]
#         col_mid = products[index + 1]
#         col_right = products[index + 2]
#         """
#         we pick 2
#         then 2,9
#         then 2,3,4,7
#         then 1,2,3,4,5
#         then 2 (last one)
#         """
#         while index1 < len(products) - 1:
#             if col_mid > col_left:
#                 best_count += col_mid
#                 if col_right > col_mid:
#                     best_count += col_right
#                     index1 += 1
#                     col_mid = products[index1+1]
#                     col_right = products[index1 + 2]
#
#                 # col_left = col_mid
#                 # index += 1
#             else:
#                 counts.append(best_count)
#                 best_count -= col_mid
#                 col_mid = col_right - 1
#                 if col_mid <= col_left:
#                     continue
#                 else:
#                     best_count += col_right
#             index1 += 1
#         index += 1
#         print(counts)
def findMaxProducts(products):
    # Write your code here
    """
    Notes
    stack products
    n piles = length of products
    amount in each pile is the values in the list products
    get any sub array
    okay I see

    Find the largest continuous sublist in the list where we can get the total number of products

    so given 2,9,4,7,5,2
    we can try doing 2,3,4,7
    so we want to sum from left to right
    to get all possible combinations we want to start with 1 and increase?
    """
    """
    we pick 2
    then 2,9
    then 2,3,4,7
    then 1,2,3,4,5
    then 2 (last one)
    """
    best = products[0]
    counts = [best]

    while products[0] > 0:
        for i in range(len(products)-2):
            current = products[i]
            next = products[i+1]
            third = products[i+2]
            if next > current:
                counts[-1] += next
            else:
                # if it's not greater, instead, try adding the next number if the next number is valid

                next_num = next - 1
                if next_num > products[i-1]:
                    counts.append(counts[-1] - current)
                    counts[-1] += next_num
        products[0] -= 1
    # return max(counts)
    return counts


products = [2, 9, 4, 7, 5, 2]
result = findMaxProducts(products)
print(result)