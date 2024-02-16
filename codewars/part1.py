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

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

print(greet('Johnny'))