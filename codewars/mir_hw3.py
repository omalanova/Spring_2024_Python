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