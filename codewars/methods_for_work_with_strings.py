# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# Examples
#
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
#
# Notes
#
#     All numbers are valid Int32, no need to validate them.
#     There will always be at least one number in the input string.
#     Output string must be two numbers separated by a single space, and highest number is first.
# def high_and_low(numbers):
#     list_of_numbers = numbers.split(' ')
#     array = [int(elem) for elem in list_of_numbers]
#     max_of_list = max(array)
#     min_of_list = min(array)
#     return str(max_of_list) + ' ' + str(min_of_list)

# best practice
# def high_and_low(numbers):
#   numbers = [int(c) for c in numbers.split(' ')]
#   return f"{max(numbers)} {min(numbers)}"

# def high_and_low(numbers):
#     nums = sorted(numbers.split(), key=int)
#     return '{} {}'.format(nums[-1], nums[0])

# print(high_and_low("1 2 3 4 5"))
# print(high_and_low("10 3 -5 42 -1 0 0 -9 4 7 4 -4"))

# Convert a string to an array
# Write a function to split a string and convert it into an array of words.
# Examples (Input ==> Output):
#
# "Robin Singh" ==> ["Robin", "Singh"]
#
# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

def string_to_array(s):
    return s.split(' ')