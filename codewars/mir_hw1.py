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

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    if operator == '-':
        return value1 - value2
    if operator == '*':
        return value1 * value2
    if operator == '/':
        return value1 / value2