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
#
# import random
# class Ghost(object):
#     def __init__(self):
#         self.color = random.choice(['white', 'yellow', 'purple', 'red'])
# ghost1 = Ghost()
# print(ghost1.color)

# Building blocks
# Write a class Block that creates a block (Duh..)
# Requirements
#
# The constructor should take an array as an argument, this will contain 3 integers of the form [width, length, height] from which the Block should be created.
#
# Define these methods:
#
# `get_width()` return the width of the `Block`
#
# `get_length()` return the length of the `Block`
#
# `get_height()` return the height of the `Block`
#
# `get_volume()` return the volume of the `Block`
#
# `get_surface_area()` return the surface area of the `Block`

class Block:
    def __init__(self, array):
        self.width = array[0]
        self.length = array[1]
        self.height = array[2]
    def get_width(self):
        return self.width
    def get_length(self):
        return self.length
    def get_height(self):
        return self.height
    def get_volume(self):
        return self.get_width() * self.get_length() * self.get_height()
    def get_surface_area(self):
        return 2 * (self.get_width() * self.get_length() + self.get_width() * self.get_height() + self.get_length() * self.get_height())

# best practice
#class Block(object):
    # def __init__(self, wlh):
    #     self.w, self.l, self.h = w,l,h = wlh
    #     self.v = w*h*l
    #     self.a = 2 * (w*l + w*h + l*h)
    #
    # def get_width(self):        return self.w
    # def get_length(self):       return self.l
    # def get_height(self):       return self.h
    # def get_volume(self):       return self.v
    # def get_surface_area(self): return self.a

block1 = Block([2,2,2])
print(block1.get_width(), block1.get_length(), block1.get_height())
print(block1.get_volume(), block1.get_surface_area())

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