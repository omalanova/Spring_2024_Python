# Beginner Series #1 School Paperwork
# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
#
# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
# Example:
#
# n= 5, m=5: 25
# n=-5, m=5:  0

# def paperwork(n, m):
#     if n <= 0 or m <= 0:
#         return 0
#     else:
#         return n * m

# def paperwork(n, m):
#     return 0 if n <= 0 or m <= 0 else n * m
# print(paperwork(-5, 5))

# Even or Odd
# Create a function that takes an integer as an argument
# and returns "Even" for even numbers or "Odd" for odd numbers.
# def even_or_odd(number):
#     return 'Odd' if number % 2 else 'Even'
# print(even_or_odd(2))

# Gravity Flip
# If you've completed this kata already and want a bigger challenge, here's the 3D version
#
# Bob is bored during his physics lessons so he's built himself a toy box to help pass the time. The box is special because it has the ability to change gravity.
#
# There are some columns of toy cubes in the box arranged in a line. The i-th column contains a_i cubes.
# At first, the gravity in the box is pulling the cubes downwards. When Bob switches the gravity,
# it begins to pull all the cubes to a certain side of the box, d, which can be either 'L' or 'R' (left or right).
# Below is an example of what a box of cubes might look like before and after switching gravity.
# Given the initial configuration of the cubes in the box,
# find out how many cubes are in each of the n columns after Bob switches the gravity.
# Examples (input -> output:
#
# * 'R', [3, 2, 1, 2]      ->  [1, 2, 2, 3]
# * 'L', [1, 4, 5, 3, 5 ]  ->  [5, 5, 4, 3, 1]
def flip(d, a):
    return sorted(a) if d == 'R' else sorted(a, reverse=True)
print(flip('R', [3, 2, 1, 2]))
print(flip('L', [1, 4, 5, 3, 5 ]))