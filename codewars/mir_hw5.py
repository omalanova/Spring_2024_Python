# Color Ghost
#
# Create a class Ghost
#
# Ghost objects are instantiated without any arguments.
#
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
#
# ghost = Ghost()
# ghost.color  #=> "white" or "yellow" or "purple" or "red"

import random
class Ghost(object):
    def __init__(self):
        self.color = random.choice(['white', 'yellow', 'purple', 'red'])
ghost1 = Ghost()
print(ghost1.color)


# Menu Display
# Create a class that imitates a select screen. The cursor can move to left or right!
#
# In the display method, return a string representation of the list, but with square brackets around the currently selected element. Also, create the methods to_the_right and to_the_left which moves the cursor.
#
# The cursor should start at index 0.
# Examples
#
# menu = Menu([1, 2, 3])
#
# menu.display() ➞ "[[1], 2, 3]"
#
# menu.to_the_right()
# menu.display() ➞ "[1, [2], 3]"
#
# menu.to_the_right()
# menu.display() ➞ "[1, 2, [3]]"
#
# menu.to_the_right()
# menu.display() ➞ "[[1], 2, 3]"
#
# menu.to_the_left()
# menu.display() ➞ "[1, 2, [3]]"
#
# menu.to_the_left()
# menu.display() ➞ "[1, [2], 3]"

# class Menu:
#     # add an __init__ method
#
#     def to_the_right(self):
#
#     # write code here!
#
#     def to_the_left(self):
#
#     # write code here!
#
#     def display(self):
# write code here