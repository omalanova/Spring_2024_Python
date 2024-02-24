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