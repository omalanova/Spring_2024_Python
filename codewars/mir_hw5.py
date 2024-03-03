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

# class Block:
#     def __init__(self, array):
#         self.width = array[0]
#         self.length = array[1]
#         self.height = array[2]
#     def get_width(self):
#         return self.width
#     def get_length(self):
#         return self.length
#     def get_height(self):
#         return self.height
#     def get_volume(self):
#         return self.get_width() * self.get_length() * self.get_height()
#     def get_surface_area(self):
#         return 2 * (self.get_width() * self.get_length() + self.get_width() * self.get_height() + self.get_length() * self.get_height())

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

# block1 = Block([2,2,2])
# print(block1.get_width(), block1.get_length(), block1.get_height())
# print(block1.get_volume(), block1.get_surface_area())

# Building Spheres
# Now that we have a Block let's move on to something slightly more complex: a Sphere.
# Arguments for the constructor
#
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)
#
# Methods to be defined
#
# get_radius()       =>  radius of the Sphere (do not round it)
# get_mass()         =>  mass of the Sphere (do not round it)
# get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
# get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
# get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)
#
# Example
#
# ball = Sphere(2,50)
# ball.get_radius() ->       2
# ball.get_mass() ->         50
# ball.get_volume() ->       33.51032
# ball.get_surface_area() -> 50.26548
# ball.get_density() ->      1.49208
#
# Any feedback would be much appreciated

# from math import pi
# class object:
#     def __init__(self):
#         self.object = object
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#
#     def get_radius(self):
#         return self.radius
#     def get_mass(self):
#         return self.mass
#     def get_volume(self):
#         return round(4 / 3 * pi * self.get_radius()**3, 5)
#     def get_surface_area(self):
#         return round(4 * pi * self.get_radius() ** 2, 5)
#     def get_density(self):
#         return round(self.get_mass() / self.get_volume(), 5)

# best practice
# from math import pi
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#         self.volume = 4*pi * self.radius**3 / 3
#         self.surface = 4*pi* self.radius**2
#     def get_radius(self):
#         return self.radius
#     def get_mass(self):
#         return self.mass
#     def get_volume(self):
#         return round(self.volume,5)
#     def get_surface_area(self):
#         return round(self.surface,5)
#     def get_density(self):
#         return round(self.mass/self.volume, 5)

# class Sphere:
#     def __init__(self, radius, mass):
#         self.radius, self.mass = radius, mass
#         self.area = __import__('math').pi*4*radius**2
#         self.volume = self.area/3*radius
#         self.density = mass/self.volume
#     _get = lambda x: lambda self, decimal=5: round(getattr(self, x), decimal)
#     get_surface_area = _get('area')
#     get_density = _get('density')
#     get_radius = _get('radius')
#     get_volume = _get('volume')
#     get_mass = _get('mass')


# ball = Sphere(2, 50)
# print(ball.get_radius())
# print(ball.get_mass())
# print(ball.get_volume())
# print(ball.get_density())

# OOP: Object Oriented Piracy

# Task
#
# You have access to the ship "draft" and "crew". "Draft" is the total ship weight and "crew" is the number of humans on the ship.
#
# Each crew member adds 1.5 units to the ship draft. If after removing the weight of the crew, the draft is still more than 20, then the ship is worth looting. Any ship weighing that much must have a lot of booty!
#
# Add the method
#
# is_worth_it
#
# to decide if the ship is worthy to loot. For example:
#
# Titanic.is_worth_it()
# False

# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew
#     def is_worth_it(self):
#         return self.draft - 1.5 * self.crew > 20
#
# Titanic = Ship(15, 10)
# print(Titanic.is_worth_it())
# worthy_ship = Ship(100,20)
# print(worthy_ship.is_worth_it())

# Double value every next call
# This kata is about static method that should return different values.
#
# On the first call it must be 1, on the second and others - it must be a double from previous value.
#
# Look tests for more examples, good luck :)

# class Class:
#     number = 1
#     @staticmethod
#     def get_number():
#         if Class.number == 1:
#             Class.number *= 2
#             return 1
#         else:
#             number_new = Class.number
#             Class.number *= 2
#             return number_new

# best practice
# class Class:
#     value=1
#     def get_number():
#         result=Class.value
#         Class.value*=2
#         return result

# Class.get_number() # -> 1
# Class.get_number() # -> 2
# Class.get_number() # -> 4
# print(Class.get_number()) # -> 8

# Thinkful - Object Drills: Quarks
# You're modelling the interaction between a large number of quarks and have decided to create a Quark class so you can generate your own quark objects.
#
# Quarks are fundamental particles and the only fundamental particle to experience all four fundamental forces.
# Your task
#
# Your Quark class should allow you to create quarks of any valid color ("red", "blue", and "green") and any valid flavor ('up', 'down', 'strange', 'charm', 'top', and 'bottom').
#
# Every quark has the same baryon_number (BaryonNumber in C#): 1/3.
#
# Every quark should have an .interact() (.Interact() in C#) method that allows any quark to interact with another quark via the strong force. When two quarks interact they exchange colors.
# Example
#
# >>> q1 = Quark("red", "up")
# >>> q1.color
# "red"
# >>> q1.flavor
# "up"
# >>> q2 = Quark("blue", "strange")
# >>> q2.color
# "blue"
# >>> q2.baryon_number
# 0.3333333333333333
# >>> q1.interact(q2)
# >>> q1.color
# "blue"
# >>> q2.color
# "red"

# class Quark(object):
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor
#         self.baryon_number = 1 / 3
#     def interact(self, quark):
#         self.color, quark.color = quark.color, self.color
#
# q1 = Quark("red", "up")
# print(q1.color)
# print(q1.flavor)
# q2 = Quark("blue", "strange")
# print(q2.color)
# print(q2.flavor)
# print(q2.baryon_number)
# q1.interact(q2)
# print(q1.color)
# print(q2.color)

# Refactored Greeting
# The following code could use a bit of object-oriented artistry. While it's a simple method and works just fine as it is, in a larger system it's best to organize methods into classes/objects. (Or, at least, something similar depending on your language)
#
# Refactor the following code so that it belongs to a Person class/object. Each Person instance will have a greet method. The Person instance should be instantiated with a name so that it no longer has to be passed into each greet method call.
#
# Here is how the final refactored code would be used:
#
# joe = Person('Joe')
# joe.greet('Kate') # should return 'Hello Kate, my name is Joe'
# joe.name          # should == 'Joe'

class Person:
    def __init__(self, my_name):
        self.name = my_name

    def greet(self, your_name):
        return f"Hello {your_name}, my name is {self.name}"

jack = Person("Jack")
jill = Person("Jill")
print(jack.greet('Jill'))
print(jack.greet('Mary'))


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