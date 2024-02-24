# Miles per gallon to kilometers per liter
# Sometimes, I want to quickly be able to convert miles per imperial gallon (mpg) into kilometers per liter (kpl).
#
# Create an application that will display the number of kilometers per liter (output) based on the number of miles per imperial gallon (input).
#
# Make sure to round off the result to two decimal points.
#
# Some useful associations relevant to this kata:
#
#     1 Imperial Gallon = 4.54609188 litres
#     1 Mile = 1.609344 kilometres

# def converter(mpg):
#     return round(mpg / 4.54609188 * 1.609344, 2) # kpl
# print(converter(10))

# Lario and Muigi Pipe Problem

# Issue
#
# Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.
#
# The pipes connecting your level's stages together need to be fixed before you receive any more complaints.
#
# The pipes are correct when each pipe after the first is 1 more than the previous one.
# Task
#
# Given a list of unique numbers sorted in ascending order, return a new list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included).
# Example
#
# Input:  1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8

# def pipe_fix(nums):
#     return list(range(min(nums), max(nums) + 1))
# print(pipe_fix([6, 9]))

# Basic Mathematical Operations
# Your task is to create a function that does four basic mathematical operations.
#
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.
# Examples(Operator, value1, value2) --> output
#
# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7

# my solution
# def basic_op(operator, value1, value2):
#     if operator == '+':
#         return value1 + value2
#     if operator == '-':
#         return value1 - value2
#     if operator == '*':
#         return value1 * value2
#     if operator == '/':
#         return value1 / value2

# best practice

# def basic_op(operator, value1, value2):
#     return eval(f'{value1}{operator}{value2}')

# Training JS #18: Methods of String object--concat() split() and its good friend join()

# Implement a function which accepts 2 arguments: string and separator.
#
# The expected algorithm: split the string into words by spaces, split each word into separate characters and join them back with the specified separator, join all the resulting "words" back into a sentence with spaces.
#
# For example:
#
# splitAndMerge("My name is John", " ")  ==  "M y n a m e i s J o h n"
# splitAndMerge("My name is John", "-")  ==  "M-y n-a-m-e i-s J-o-h-n"
# splitAndMerge("Hello World!", ".")     ==  "H.e.l.l.o W.o.r.l.d.!"
# splitAndMerge("Hello World!", ",")     ==  "H,e,l,l,o W,o,r,l,d,!"

# def split_and_merge(string_, separator):
#     words = string_.split(' ')
#     result = []
#     for i in words:
#         i = separator.join(i)
#         result.append(i)
#     return ' '.join(result)
#
# print(split_and_merge('My name is John', '-'))

# Sum of Multiples
# Your Job
#
# Find the sum of all multiples of n below m
# Keep in Mind
#
#     n and m are natural numbers (positive integers)
#     m is excluded from the multiples
#
# Examples
#
# sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
# sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
# sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
# sumMul(4, -7)  ==> "INVALID"

# my solution
# def sum_mul(n, m):
#     if (n > 0 and m > 0):
#         sum = 0
#         for i in range(n, m):
#             if i % n == 0:
#                 sum += i
#         return sum
#     else:
#         return 'INVALID'

# best practice
# def sum_mul(n, m):
#     return sum(range(n, m, n)) if n > 0 and m > 0 else "INVALID"
#
# print(sum_mul(4, 123))

# Who is going to pay for the wall?
# Don Drumphet lives in a nice neighborhood, but one of his neighbors has started to let his house go. Don Drumphet wants to build a wall between his house and his neighbor’s, and is trying to get the neighborhood association to pay for it. He begins to solicit his neighbors to petition to get the association to build the wall. Unfortunately for Don Drumphet, he cannot read very well, has a very limited attention span, and can only remember two letters from each of his neighbors’ names. As he collects signatures, he insists that his neighbors keep truncating their names until two letters remain, and he can finally read them.
#
# Your code will show Full name of the neighbor and the truncated version of the name as an array.
# If the number of the characters in name is less than or equal to two, it will return an array
# containing only the name as is"

# def who_is_paying(name):
    # solution 1
    # if len(name) <= 2:
    #     return [name]
    # else:
    #     return [name, name[0] + name[1]]
    # solution 2
#     return [name, name[0:2] if len(name) > 2 else name]
# print(who_is_paying("Mexico"))

# Reverse List Order
# In this kata you will create a function that takes in a list and returns a list with the reverse order.
# Examples (Input -> Output)
#
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]

# def reverse_list(l):
#     return l[::-1]
#     # return list(reversed(l)) # -> solution 2
#     # l.reverse()              #-> solution 3
#     #   return l
# print(reverse_list([1,2,3,4]))

# Will there be enough space?

# The Story:
#
# Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.
# Task Overview:
#
# You have to write a function that accepts three parameters:
#
#     cap is the amount of people the bus can hold excluding the driver.
#     on is the number of people on the bus excluding the driver.
#     wait is the number of people waiting to get on to the bus excluding the driver.
#
# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
# Usage Examples:
#
# cap = 10, on = 5, wait = 5 --> 0 # He can fit all 5 passengers
# cap = 100, on = 60, wait = 50 --> 10 # He can't fit 10 of the 50 waiting

# def enough(cap, on, wait):
#     if on == wait and cap == on + wait:
#         return f'He can fit all {wait} passengers'
#     elif cap > on + wait:
#         return f'He can fit all {wait} passengers'
#     else:
#         return f'He can\'t fit {wait - cap + on} of the {wait} waiting'
#
# # best practice
# # def enough(cap, on, wait):
# #     return max(0, wait - (cap - on))
# print(enough(20, 5, 5))

# MakeUpperCase
# Write a function which converts the input string to uppercase.

# def make_upper_case(s):
#     # s1 = s.upper()
#     # return s1
#     return s.upper()
#
# print(make_upper_case('hello'))

# How good are you really?
# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
#
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
#
# Return True if you're better, else False!
# Note:
#
# Your points are not included in the array of your class's points.
# For calculating the average point you may add your point to the given array!

# def better_than_average(class_points, your_points):
#     average_of_class = sum(class_points) / len(class_points)
#     return your_points >= average_of_class
# print(better_than_average([2, 3], 5))
# print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))
# print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))

# Find the position!
# When provided with a letter, return its position in the alphabet.
#
# Input :: "a"
#
# Ouput :: "Position of alphabet: 1"

def position(alphabet):
    if 97 <= ord(alphabet) <= 122:
        return f'Position of alphabet: {ord(alphabet) - 96}'
    if 65 <= ord(alphabet) <= 90:
        return f'Position of alphabet: {ord(alphabet) - 64}'
print(position('B'))