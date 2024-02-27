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

def create_box(m, n):  ## m and n positive integers
    res = []
    for i in range(n):
        inner = []
        for j in range(1, m):
            minIndex = min(i, j, n-i-1, m-j-1) + 1
            inner.append(minIndex)
        res.append(inner)
    return res
# best practice
# def create_box(m, n):  ## m and n positive integers
#     return [[min([x+1, y+1, m-x, n-y]) for x in range(m)] for y in range(n)]

print(create_box(7,8))