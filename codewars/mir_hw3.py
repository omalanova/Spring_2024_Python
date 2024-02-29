# Converting 12-hour time to 24-hour time
# Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!
#
# You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either a.m. or p.m.) as input.
#
# Your task is to return a four-digit string that encodes that time in 24-hour time.
# Notes
#
#     By convention, noon is 12:00 pm, and midnight is 12:00 am.
#     On 12-hours clock, there is no 0 hour, and time just after midnight is denoted as, for example, 12:15 am. On 24-hour clock, this translates to 0015.

# def to24hourtime(hour, minute, period):
#     result = ('')
#     if period == 'am':
#         result = (result
#                   + str(hour % 12).rjust(2, '0')
#                   + str(minute).rjust(2, '0'))
#         return result
#     elif hour == 12:
#         result = (result
#                   + str((hour) % 24).rjust(2, '0')
#                   + str(minute).rjust(2, '0'))
#         return result
#     else:
#         result = (result
#                   + str((hour + 12) % 24).rjust(2, '0')
#                   + str(minute).rjust(2, '0'))
#         return result

# best practice
# def to24hourtime(hour, minute, period):
#     return '%02d%02d' % (hour % 12 + 12 * (period == 'pm'), minute)
#
# print(to24hourtime(1, 0, 'pm'))

# Selective fear of numbers
# I've got a crazy mental illness. I dislike numbers a lot. But it's a little complicated:
# The number I'm afraid of depends on which day of the week it is...
# This is a concrete description of my mental illness:
#
# Monday --> 12
#
# Tuesday --> numbers greater than 95
#
# Wednesday --> 34
#
# Thursday --> 0
#
# Friday --> numbers divisible by 2
#
# Saturday --> 56
#
# Sunday --> 666 or -666
#
# Write a function which takes a string (day of the week) and an integer (number to be tested)
# so it tells the doctor if I'm afraid or not. (return a boolean)

# def am_I_afraid(day,num):
#     return True if day == 'Monday' and num == 12 or day == 'Tuesday' and num > 95 or day == 'Wednesday' and num == 34 or day == 'Thursday' and num == 0 or day == 'Friday' and num % 2 == 0 or day == 'Saturday' and num == 56 or day == 'Sunday' and num in [666, -666] else False

# best practice
# def am_I_afraid(day,num):
#     return {
#         'Monday':  num == 12,
#         'Tuesday': num > 95,
#         'Wednesday': num == 34,
#         'Thursday': num == 0,
#         'Friday': num % 2 == 0,
#         'Saturday': num ==  56,
#         'Sunday': num == 666 or num == -666,
#     }[day]
#
# print(am_I_afraid('Monday', 13))

# Jaden Casing Strings
# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.
#
# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
#
# Example:
#
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

# def to_jaden_case(string):
#     jaden_string = ''
#     sentence = string.split()
#     for word in sentence:
#         if "'" in word:
#             jaden_string = jaden_string + word.capitalize() + ' '
#         else:
#             jaden_string = jaden_string + word.title() + ' '
#     return jaden_string.strip()

# best practice
# def to_jaden_case(string):
#     return ' '.join(word.capitalize() for word in string.split())
#
# # import string
# # toJadenCase = string.capwords
#
# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

# NATO Phonetic Alphabet (retired)
# Complete the function nato that takes a word in parameter and returns a string that spells the word using the NATO phonetic alphabet.
#
# There should be a space between each word in the returned string, and the first letter of each word should be capitalized.
#
# For those of you that don't want your fingers to bleed, this kata already has a dictionary typed out for you.
# Examples
#
# "hi"      -->  "Hotel India"
# "abc"     -->  "Alpha Bravo Charlie"
# "babble"  -->  "Bravo Alpha Bravo Bravo Lima Echo"
# "Banana"  -->  "Bravo Alpha November Alpha November Alpha"

# https://www.codewars.com/kata/54530f75699b53e558002076/train/python

# ls =  {
#     "A": "Alpha",  "B": "Bravo",   "C": "Charlie",
#     "D": "Delta",  "E": "Echo",    "F": "Foxtrot",
#     "G": "Golf",   "H": "Hotel",   "I": "India",
#     "J": "Juliett","K": "Kilo",    "L": "Lima",
#     "M": "Mike",   "N": "November","O": "Oscar",
#     "P": "Papa",   "Q": "Quebec",  "R": "Romeo",
#     "S": "Sierra", "T": "Tango",   "U": "Uniform",
#     "V": "Victor", "W": "Whiskey", "X": "X-ray",
#     "Y": "Yankee", "Z": "Zulu"
#   }
# def nato(word):
#     return ' '.join([ls[c.upper()] for c in word])

# Dropcaps -> https://www.codewars.com/kata/559e5b717dd758a3eb00005a
# DropCaps means that the first letter of the starting word of the paragraph should be in caps and the remaining lowercase, just like you see in the newspaper.
#
# But for a change, let"s do that for each and every word of the given String. Your task is to capitalize every word that has length greater than 2, leaving smaller words as they are.
#
# *should work also on Leading and Trailing Spaces and caps.
#
# "apple"            => "Apple"
# "apple of banana"  => "Apple of Banana"
# "one   space"      => "One   Space"
# "   space WALK   " => "   Space Walk   "
#
# Note: you will be provided atleast one word and should take string as input and return string as output.

def drop_cap(words):
    res = ''
    for word in words.split(' '):
        if len(word) > 2:
            res = res + word.capitalize() + ' '
        else:
            res = res + word + ' '
    return res[0:len(res) - 1]

# best practice
# def drop_cap(str_):
#     return ' '.join( w.capitalize() if len(w) > 2 else w for w in str_.split(' ') )

print(drop_cap('apple      of banana'))