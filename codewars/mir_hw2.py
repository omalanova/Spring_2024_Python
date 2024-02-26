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
# def flip(d, a):
#     return sorted(a) if d == 'R' else sorted(a, reverse=True)
# print(flip('R', [3, 2, 1, 2]))
# print(flip('L', [1, 4, 5, 3, 5 ]))

# Who ate the cookie?
# For this problem you must create a program that says who ate the last cookie.
# If the input is a string then "Zach" ate the cookie.
# If the input is a float or an int then "Monica" ate the cookie.
# If the input is anything else "the dog" ate the cookie.
# The way to return the statement is: "Who ate the last cookie? It was (name)!"
#
# Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach! (The reason you return Zach is because the input is a string)
#
# Note: Make sure you return the correct message with correct spaces and punctuation.

# def cookie(x):
#     return f'Who ate the last cookie? It was {"Zach" if type(x) is str else "Monica" if type(x) in [int, float] else "the dog"}!'
# print(cookie(2.3))

# Filter the number
# Oh, no! The number has been mixed up with the text. Your goal is to retrieve the number from the text, can you return the number back to its original state?
# Task
#
# Your task is to return a number from a string.
# Details
#
# You will be given a string of numbers and letters mixed up,
# you have to return all the numbers in that string in the order they occur.

# def filter_string(st):
#     num = ''
#     for i in st:
#         if i.isdigit():
#             num += i
#     return int(num)

# Sentence Smash
#
# Write a function that takes an array of words and smashes them together into a sentence
# and returns the sentence. You can ignore any need to sanitize words or add punctuation,
# but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning
# or the end of the sentence!
# Example
#
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

# def smash(words):
#     return ' '.join(words)