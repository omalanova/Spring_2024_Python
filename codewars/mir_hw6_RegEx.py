import re
# Filter the number
# Oh, no! The number has been mixed up with the text.
# Your goal is to retrieve the number from the text,
# can you return the number back to its original state?
# Task
#
# Your task is to return a number from a string.
# Details
#
# You will be given a string of numbers and letters mixed up,
# you have to return all the numbers in that string in the order they occur.
# def filter_string(st):
#     return re.findall(r'0-9',st)
#
# print(filter_string("123"))
# print(filter_string("a1b2c3"))

# Regex count lowercase letters
# Your task is simply to count the total number of lowercase letters in a string.
# Examples
#
# "abc" ===> 3
#
# "abcABC123" ===> 3
#
# "abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3
#
# "" ===> 0;
#
# "ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0
#
# "abcdefghijklmnopqrstuvwxyz" ===> 26

def lowercase_count(strng):
    return len(re.findall(r'[a-z]',strng))

#best practice
# def lowercase_count(strng):
#     return len(re.findall(r'[a-z]',strng))
# def lowercase_count(str):
#     return sum(1 for c in str if c.islower())
print(lowercase_count("abc"))
print(lowercase_count("abcABC123"))
print(lowercase_count("abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"))

# Regexp Basics - is it a digit?
# Implement String#digit? (in Java StringUtils.isDigit(String)),
# which should return true if given object is a digit (0-9), false otherwise.
def is_digit(n):
    return bool(re.fullmatch(r'\d',n))
#best practice
# def is_digit(n):
#     return n.isdigit() and len(n)==1
