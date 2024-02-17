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

def count_sheeps(sheep):
    # TODO May the force be with you
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count
    # pass


print(count_sheeps([True, True, True, False,
                    True, True, True, True,
                    True, False, True, False,
                    True, False, False, True,
                    True, True, True, True,
                    False, False, True, True]))