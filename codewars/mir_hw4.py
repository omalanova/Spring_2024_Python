# The 'spiraling' box
# Given two positive integers m (width) and n (height), fill a two-dimensional list (or array) of size m-by-n in the following way:
#
#     (1) All the elements in the first and last row and column are 1.
#
#     (2) All the elements in the second and second-last row and column are 2, excluding the elements from step 1.
#
#     (3) All the elements in the third and third-last row and column are 3, excluding the elements from the previous steps.
#
#     And so on ...
#
# Examples
#
# Given m = 5, n = 8, your function should return
#
# [[1, 1, 1, 1, 1],
#  [1, 2, 2, 2, 1],
#  [1, 2, 3, 2, 1],
#  [1, 2, 3, 2, 1],
#  [1, 2, 3, 2, 1],
#  [1, 2, 3, 2, 1],
#  [1, 2, 2, 2, 1],
#  [1, 1, 1, 1, 1]]
#
# Given m = 10, n = 9, your function should return
#
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
#  [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
#  [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
#  [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
#  [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
#  [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
#  [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
#
# Bird mountain generalizes this kata in a fun way.

# def create_box(m, n):  ## m and n positive integers
#     res = []
#     for i in range(n):
#         inner = []
#         for j in range(1, m):
#             minIndex = min(i, j, n-i-1, m-j-1) + 1
#             inner.append(minIndex)
#         res.append(inner)
#     return res
# # best practice
# # def create_box(m, n):  ## m and n positive integers
# #     return [[min([x+1, y+1, m-x, n-y]) for x in range(m)] for y in range(n)]
#
# print(create_box(7,8))

# Running out of space
# Kevin is noticing his space run out! Write a function that removes the spaces from the values and returns an array showing the space decreasing.
# For example, running this function on the array ['i', 'have','no','space'] would produce ['i','ihave','ihaveno','ihavenospace']

def spacey(array):
    new_array = []
    new_str = ''
    for word in array:
        new_str += word
        new_array.append(new_str)
    return new_array

# best practice
# def spacey(array):
#     return [''.join(array[:i+1]) for i in range(len(array))]
# from itertools import accumulate
#
# def spacey(a):
#     return list(accumulate(a))
print(spacey(['kevin', 'has','no','space']))