# Convert a Number to a String!
#
# We need a function that can transform a number (integer) into a string.
#
# What ways of achieving this do you know?
# Examples (input --> output):
#
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"
from array import array


# def number_to_string(num):
#     return str(num)
#
# print(number_to_string(123))

# Jenny's secret message

# Jenny has written a function that returns a greeting for a user.
# However, she('s in love with Johnny, and would like to greet him '
# 'slightly different. She added a special case to her function, but she made a mistake.)
#
# Can you help her?

# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)
#
# print(greet('Johnny'))

# Convert boolean values to strings 'Yes' or 'No'.

# Complete the method that takes a boolean value and
# return a "Yes" string for true, or a "No" string for false.

# def bool_to_word(boolean):
#     # TODO
#     if boolean:
#         return "Yes"
#     else:
#         return "No"
#
# print(bool_to_word(True))

# Are You Playing Banjo?

# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
#
# The function takes a name as its only argument, and returns one of the following strings:
#
# name + " plays banjo"
# name + " does not play banjo"
#
# Names given are always valid strings.

# def are_you_playing_banjo(name):
#     # Implement me!
#     if name.lower()[0] == "r":
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"
#
# print(are_you_playing_banjo("om"))

# Counting sheep...

# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
#
# For example,
#
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
#
# The correct answer would be 17.
#
# Hint: Don't forget to check for bad values like null/undefined

# def count_sheeps(sheep):
#     # TODO May the force be with you
#     count = 0
#     for i in sheep:
#         if i == True:
#             count += 1
#     return count
#     # pass
#
#
# print(count_sheeps([True, True, True, False,
#                     True, True, True, True,
#                     True, False, True, False,
#                     True, False, False, True,
#                     True, True, True, True,
#                     False, False, True, True]))

# Convert number to reversed array of digits

# Convert number to reversed array of digits
#
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# Example(Input => Output):
#
# 35231 => [1,3,2,5,3]
# 0 => [0]

# def digitize(n):

# Вариант 1. int - функция, которую map применит к каждому символу
# в итерабельной последовательности n (строка - итерабельная последовательность))
#     return(list(map(int, str(n))))  # -> [1, 2, 3, 4, 5]
#     return list(map(int, str(n)))[::-1] # в обратном порядке

# map, filter - эти встроенные функции можно переписать
# с помощью генераторов списка. Например, так:
#     return([int(x) for x in str(n)])  # -> [1, 2, 3, 4, 5]
#     return([int(x) for x in str(n)])[::-1] # в обратном порядке

# Вариант 2. Пройтись циклом по всем цифрам числа начиная с конца
#     a = []
#     if n == 0:
#         return [n]
#     else:
#         while n > 0:
#             a.append(n % 10)  # берем последнюю цифру числа и добавляем ее в список
#             n //= 10  # убираем последнюю цифру числа
#         return a
# то же самое, но с другим условием
#     result = []
#     while n >= 1:
#         result.append(n%10)
#         n //= 10
#     return result


# вариант3
# def digitize(n):
#     mylist = [int(i) for i in str(n)]
#     mylist.reverse()
#     return mylist

# print(digitize(52321))

# A Needle in the Haystack
# Can you find the needle in the haystack?
#
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
#
# After your function finds the needle it should return a message( as a string) that says:
#
# "found the needle at position " plus the index it found the needle, so:
#
# Example(Input --> Output)
#
# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"
#
# Note: In COBOL, it should return "found the needle at position 6"

# my solution
# def find_needle(haystack):
#     index = 0
#     for i in haystack:
#         if i == "needle":
#             return "found the needle at position " + str(index)
#         index += 1

# best practice
# def find_needle(haystack):
#     return f'found the needle at position {haystack.index("needle")}'

# A function within a function

# Given an input n, write a function always that returns a function which returns n.
# three = always(3)
# three() / * returns 3 * /

# def always(n=0):
#     return lambda: n

# A lambda function is a small anonymous function.
#
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax
# lambda arguments : expression
#
# The expression is executed and the result is returned:

# Sum Arrays

# Write a function that takes an array of numbers and returns the sum of the numbers.The numbers
# can be negative or non - integer.If the array does not contain any numbers then you should return 0.
# Examples
#
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2
#
# Input: []
# Output: 0
#
# Input: [-2.398]
# Output: -2.398

# def sum_array(a):
#     summ = 0
#     for i in a:
#         summ += i
#     return summ
# # best practice
# def sum_array(a):
#   return sum(a)

# This code does not execute properly.Try to figure out why.

# Write a function that returns the total surface area and volume of a box as an array: [area, volume]

# def get_size(w, h, d):
#     return [2 * (w * h + h * d + d * w), w * h * d]

# Rock Paper Scissors
# my solution
#
# def rps(p1, p2):
#     if p1 == p2:
#         return "Draw!"
#     if p1 == "scissors":
#         if p2 == "rock":
#             return "Player 2 won!"
#         else:
#             return "Player 1 won!"
#     if p1 == "rock":
#         if p2 == "paper":
#             return "Player 2 won!"
#         else:
#             return "Player 1 won!"
#     if p1 == "paper":
#         if p2 == "scissors":
#             return "Player 2 won!"
#         else:
#             return "Player 1 won!"
#
# #best practice1
#
# def rps(p1, p2):
#     beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
#     if beats[p1] == p2:
#         return "Player 1 won!"
#     if beats[p2] == p1:
#         return "Player 2 won!"
#     return "Draw!"

# #best practice2
#
# def rps(p1, p2):
#     hand = {'rock':0, 'paper':1, 'scissors':2}
#     results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
#     return results[hand[p1] - hand[p2]]
#
# #best practice3
#
# def rps(p1, p2):
#     if p1 == p2:
#         return 'Draw!'
#     elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (
#             p1 == 'paper' and p2 == 'rock'):
#         return 'Player 1 won!'
#     else:
#         return 'Player 2 won!'

# Formatting decimal places  # 0

# Each number should be formatted that it is rounded to two decimal places.You don 't need to check whether the input is a valid number because only valid numbers are used in the tests.
#
# Example:
# 5.5589 is rounded 5.56
# 3.3424 is rounded 3.34

# #my solution https://www.codewars.com/kata/reviews/564220d56003fa369c000036/groups/65d0b4cb468ac100010eaeeb
# def two_decimal_places(n):
#     # raise NotImplementedError("TODO: two_decimal_places")
#     if int(abs(n) * 1000) % 10 >= 5:
#         if n < 0:
#             return ((int(abs(n) * 1000) // 10 + 1) / 100) * (-1)
#         else:
#             return ((int(n * 1000) // 10 + 1) / 100)
#     else:
#         if n < 0:
#             return (int(abs(n) * 1000) // 10 / 100 * (-1))
#         else:
#             return (int(n * 1000) // 10 / 100)
#
# #best practice
#
# def two_decimal_places(n):
#     return round(n, 2)

# Formatting decimal places #1

# Each floating-point number should be formatted that only the first two decimal places are returned. You don't need to check whether the input is a valid number because only valid numbers are used in the tests.
#
# Don't round the numbers! Just cut them after two decimal places!
#
# Right examples:
# 32.8493 is 32.84
# 14.3286 is 14.32
#
# Incorrect examples (e.g. if you round the numbers):
# 32.8493 is 32.85
# 14.3286 is 14.33

# my solution

# def two_decimal_places(number):
#     return int(number * 100) / 100.0

# Stringy Strings

# write me a function stringy that takes a size and returns a string of alternating 1s and 0s.
#
# the string should start with a 1.
#
# a string with size 6 should return :'101010'.
#
# with size 4 should return : '1010'.
#
# with size 12 should return : '101010101010'.

# def stringy(size):
#     str1 = ''
#     for i in range(size):
#         if i % 2 == 0:
#             str1 = str1 + '1'
#         else:
#             str1 = str1 + '0'
#     return str1
# print(stringy(6))

#my solution
# def most_frequent_item_count(collection):
#     maxcount = 0
#     for i in range(0, len(collection)):
#         count = 0
#         for j in range(0, len(collection)):
#             if (collection[i] == collection[j]):
#                 count += 1
#         if (count > maxcount):
#             maxcount = count
#
#     return maxcount

# best practice 1

# def most_frequent_item_count(collection):
#     if collection:
#         return max([collection.count(item) for item in collection])
#     return 0

# best practice 2

# def most_frequent_item_count(collection):
#     # Do your magic. :)
#     counts = []
#     if collection ==[]:
#         return 0
#     else:
#         for i in collection:
#             counts.append(collection.count(i))
#     return max(counts)
# collection = [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
# print(most_frequent_item_count(collection)) # 5 -> число -1 встречается 5 раз

# Dollars and Cents

# The company you work for has just been awarded a contract to build a payment gateway. In order to help move things along, you have volunteered to create a function that will take a float and return the amount formatting in dollars and cents.
#
# 39.99 becomes $39.99
#
# The rest of your team will make sure that the argument is sanitized before being passed to your
# function although you will need to account for adding trailing zeros if they are missing
# (though you won't have to worry about a dangling period).
#
# Examples:
#
# 3 needs to become $3.00
# 3.1 needs to become $3.10

# def format_money(amount): # https://pythoner.name/formatted-output
#     return f'${amount:.2f}'
#
# print(format_money(3.1))

# Get Planet Name By ID

# The function is not returning the correct values. Can you figure out why?
#
# Example (Input --> Output ):
#
# 3 --> "Earth"

# def get_planet_name(id):
#     # This doesn't work; Fix it!
#     name=""
#     match id:        # switch -> match
#         case 1: name = "Mercury"
#         case 2: name = "Venus"
#         case 3: name = "Earth"
#         case 4: name = "Mars"
#         case 5: name = "Jupiter"
#         case 6: name = "Saturn"
#         case 7: name = "Uranus"
#         case 8: name = "Neptune"
#     return name

# best practice

# def get_planet_name(id):
#     return {
#         1: "Mercury",
#         2: "Venus",
#         3: "Earth",
#         4: "Mars",
#         5: "Jupiter",
#         6: "Saturn",
#         7: "Uranus",
#         8: "Neptune",
#     }.get(id, None)

#best practice 2

def get_planet_name(id):
    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }
    return planets[id]
print(get_planet_name(1))