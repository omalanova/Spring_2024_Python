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

# def spacey(array):
#     new_array = []
#     new_str = ''
#     for word in array:
#         new_str += word
#         new_array.append(new_str)
#     return new_array

# best practice
# def spacey(array):
#     return [''.join(array[:i+1]) for i in range(len(array))]
# from itertools import accumulate
#
# def spacey(a):
#     return list(accumulate(a))
# print(spacey(['kevin', 'has','no','space']))

# All Star Code Challenge #3
# This Kata is intended as a small challenge for my students
#
# Create a function that takes a string argument and returns that same string with all vowels removed (vowels are "a", "e", "i", "o", "u").
#
# Example (Input --> Output)
#
# "drake" --> "drk"
# "aeiou" --> ""
#
# remove_vowels("drake") // => "drk"
# remove_vowels("aeiou") // => ""

# def remove_vowels(strng):
#     new_string = ''
#     for letter in strng:
#         if letter in 'aeiou':
#             continue
#         else:
#             new_string += letter
#     return new_string

#best practice
# def remove_vowels(strng):
#     return ''.join([i for i in strng if i not in 'aeiou'])

#def remove_vowels(strng):
    # str = ['a','i','u','e','o']
    # for i in str:
    #     strng = strng.replace(i, "")
    # return strng
# print(remove_vowels('dark'))

# The old switcheroo 2
# This is a follow up from my kata The old switcheroo
#
# Write the function :
#
# def encode(str)
#
# that takes in a string str and replaces all the letters with their respective positions in the English alphabet.
#
# encode('abc') == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
# encode('codewars') == '315452311819'
# encode('abc-#@5') == '123-#@5'
#
# String are case sensitive.

# def encode(string):
#     new_str = ''
#     for i in string.lower():
#         if i.isalpha():
#             new_str += str(ord(i) - 96)
#         else:
#             new_str += i
#     return new_str
#
# print(encode('abc'))

# Thinkful - String Drills: Jedi name
# You just took a contract with the Jedi council. They need you to write a function, greet_jedi(), which takes two arguments (a first name and a last name), works out the corresponding Jedi name, and returns a string greeting the Jedi.
#
# A person's Jedi name is the first three letters of their last name followed by the first two letters of their first name. For example:
#
# >>> greet_jedi('Beyonce', 'Knowles')
# 'Greetings, master KnoBe'
#
# Note the capitalization: the first letter of each name is capitalized. Your input may or may not be capitalized. Your function should handle it and return the Jedi name in the correct case no matter what case the input is in:
#
# >>> greet_jedi('grae', 'drake')
# 'Greetings, master DraGr'
#
# You can trust that your input names will always be at least three characters long.
#
# If you're stuck, check out the python.org tutorial section on strings and search "slice".

# def greet_jedi(first, last):
#     return f'Greetings, master {last[0:3].capitalize() + first[0:2].capitalize()}'

# Tidy Number (Special Numbers Series #9)
# A Tidy number is a number whose digits are in non-decreasing order.
# Task
#
# Given a number, Find if it is Tidy or not .

# def tidyNumber(n):
#     while n > 0:
#         if n%10 >= (n//10)%10:
#             n = n//10
#         else:
#             return False
#     return True
# best practice
# def tidyNumber(n):
#     s = list(str(n))
#     return s == sorted(s)

# def tidyNumber(n):
#     n = str(n)
#     for i in range(0, len(n) - 1):
#         if n[i] > n[i + 1]:
#             return False
#
#     return True
# print(tidyNumber(2222))

# Thinkful - Logic Drills: Graceful addition
# You like the way the Python + operator easily handles adding different numeric types, but you need a tool to do that kind of addition without killing your program with a TypeError exception whenever you accidentally try adding incompatible types like strings and lists to numbers.
#
# You decide to write a function my_add() that takes two arguments. If the arguments can be added together it returns the sum. If adding the arguments together would raise an error the function should return None instead.
#
# For example, my_add(1, 3.414) would return 4.414, but my_add(42, " is the answer.") would return None.
#
# Hint: using a try / except statement may simplify this kata.

# def my_add(a, b):
#     try:
#         if type(a + b) in [int, float, complex]:
#             return a + b
#     except:
#            return None

# def my_add(a, b):
#     try:
#         return a + b
#     except TypeError:
#         return None
# print(my_add(1, 3.141))
# print(my_add(42, " is the answer."))

# Log without dates
# You will be given an array of events, which are represented by strings. The strings are dates in HH:MM:SS format.
#
# It is known that all events are recorded in chronological order and two events can't occur in the same second.
#
# Return the minimum number of days during which the log is written.
# Example:
#
# Input -> ["00:00:00", "00:01:11", "02:15:59", "23:59:58", "23:59:59"]
# Output -> 1
#
# Input -> ["12:12:12"]
# Output -> 1
#
# Input -> ["12:00:00", "23:59:59", "00:00:00"]
# Output -> 2
#
# Input -> []
# Output -> 0

# def check_logs(log):
#     if len(log) == 0:
#         return 0
#     if len(log) == 1:
#         return 1
#     count_days = 1
#     for k in range(1, len(log)):
#         if log[k-1] >= log[k]:
#             count_days += 1
#
#     return count_days
# print(check_logs(["00:00:00", "00:01:11", "02:15:59", "23:59:58", "23:59:59"]))
# print(check_logs(["12:12:12"]))
# print(check_logs(["12:00:00", "23:59:59", "00:00:00"]))
# print(check_logs([]))

# Return substring instance count
# Complete the solution so that it returns the number of times the search_text is found within the full_text. Overlap is not permitted : "aaa" contains 1 instance of "aa", not 2.
#
# Usage example:
#
# full_text = "aa_bb_cc_dd_bb_e", search_text = "bb"
#     ---> should return 2 since "bb" shows up twice
#
#
# full_text = "aaabbbcccc", search_text = "bbb"
#     ---> should return 1

# def solution(full_text, search_text):
#     count = 0
#     for i in range(0, len(full_text)+1):
#         if full_text[i:i+len(search_text)] == search_text:
#             count += 1
#             # print(full_text[i:i+len(search_text)])
#     return count
#
# # best practice
# #def solution(full_text, search_text):
# #    return full_text.count(search_text)
# print(solution('abcdeb','b'))
# print(solution('abc','b'))
# print(solution('abbc','bb'))
# print(solution('abcdeb','b'))
# print(solution('abcdeb', 'a'))

# Vowel Count
# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    count = 0
    for i in range(len(sentence)):
        if sentence[i] in 'aeiou':
            count += 1
    return count
# best practice
#def getCount(s):
    # return sum(c in 'aeiou' for c in s)
print(get_count('aeiou'))