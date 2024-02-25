# def create_box(m, n):  ## m and n positive integers
#     res = []
#     inner = []
#     for i in range(1, n):
#         for j in range(1, m):
#             if i == 1 | i == n | j == 1 | j == m:
#                 inner.append('1')
#             inner.append(j)
#             else:
#                 if i < j:
#                     inner.append(j)
#                 else:
#                     inner.append(i)
#         res.append(inner)
#     return res
# print(create_box(4,4))