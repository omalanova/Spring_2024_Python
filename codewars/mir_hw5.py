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

# class Person:
#     def __init__(self, my_name):
#         self.name = my_name
#
#     def greet(self, your_name):
#         return f"Hello {your_name}, my name is {self.name}"
#
# jack = Person("Jack")
# jill = Person("Jill")
# print(jack.greet('Jill'))
# print(jack.greet('Mary'))

# These are not my grades! (Revamped !)
# At the end of the last semester, Prof. Joey Greenhorn implemented an online report card for his students in order to save paper. Everything seemed to be working fine back then, but since the start of the new semester he has received several emails from students complaining about erroneous grades showing up in their online report cards. Can you help him correct his implementation of the "Student" class?
#
# The "Student" class should behave like this :
#
# someStudent = Student()
# someOtherStudent = Student()
# someStudent.add_grade(98)
# someOtherStudent.add_grade(77)
# someStudent.grades == [98] # Evaluates to True
# someOtherStudent.grades == [77] # Evaluates to True
#
# But right now, this is happening :
#
# someStudent = Student()
# someOtherStudent = Student()
# someStudent.add_grade(98)
# someOtherStudent.add_grade(77)
# someStudent.grades == [98, 77] # Evaluates to True
# someOtherStudent.grades == [98, 77] # Evaluates to True

# class Student:
#
#     def __init__(self, first_name, last_name, grades=[]):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grades = list(grades)
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#     def get_average(self):
#         return sum(self.grades) / len(self.grades)

# best practice
# class Student:
#
#     def __init__(self, first_name, last_name, grades=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grades = grades or []
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#     def get_average(self):
#         return sum(self.grades) / len(self.grades)

# johnDoe = Student('John', 'Doe')
# janeDoe = Student('Jane', 'Doe')
# jamesSmith = Student('James', 'Smith')
# jennaSmith = Student('Jenna', 'Smith')
# johnDoe.add_grade(63)
# print(johnDoe.grades)
# janeDoe.add_grade(92)
# print(janeDoe.grades)
# jamesSmith.add_grade(82)
# jennaSmith.add_grade(75)
# print(johnDoe.get_average())
# print((63+92+82+75)/4)
# print(johnDoe.grades)
# print(janeDoe.grades)

# Competitive eating scoreboard
# You are the judge at a competitive eating competition and you need to choose a winner!
#
# There are three foods at the competition and each type of food is worth a different
# amount of points. Points are as follows:
#
#     Chickenwings: 5 points
#
#     Hamburgers: 3 points
#
#     Hotdogs: 2 points
#
# Write a function that helps you create a scoreboard.
# It takes as a parameter a list of objects representing the participants, for example:
#
# [
#   {name: "Habanero Hillary", chickenwings: 5 , hamburgers: 17, hotdogs: 11},
#   {name: "Big Bob" , chickenwings: 20, hamburgers: 4, hotdogs: 11}
# ]
#
# It should return "name" and "score" properties sorted by score; if scores are equals,
# sort alphabetically by name.
#
# [
#   {name: "Big Bob", score: 134},
#   {name: "Habanero Hillary", score: 98}
# ]
#
# Happy judging!

# def scoreboard(who_ate_what):
#     # score = {}
#     res = []
#     for i in who_ate_what:
#         score = 0
#         if 'chickenwings' in i:
#             score += i.get('chickenwings') * 5
#         if 'hamburgers' in i:
#             score += i.get('hamburgers') * 3
#         if 'hotdogs' in i:
#             score += i.get('hotdogs') * 2
#         my_dict = dict(name = i.get('name'), score = score)
#         res.append(my_dict)
#
#         res.sort(key=lambda dictionary: dictionary['name'])
#         res.sort(key=lambda dictionary: (dictionary["score"]), reverse=True)
#
#     return res

# best practice
# class Person:
#     def __init__(self, person: dict):
#         self.name = person.get('name')
#         self.chickenwings = person.get('chickenwings',0)
#         self.hamburgers = person.get('hamburgers',0)
#         self.hotdogs = person.get('hotdogs',0)
#
#     def get_score(self):
#         return self.chickenwings * 5 + self.hamburgers * 3 + self.hotdogs * 2
#
# def scoreboard(who_ate_what):
#     scores = []
#     for person in who_ate_what:
#         p = Person(person)
#         scores.append({"name": p.name, "score": p.get_score()})
#     return sorted(scores, key=lambda k: (-k["score"], k['name']))


# print(scoreboard([{"name": "Billy The Beast", "chickenwings": 17 , "hamburgers": 7, "hotdogs": 8},
#                                        {"name": "Habanero Hillary", "chickenwings": 5 , "hamburgers": 17, "hotdogs": 11},
#                                        {"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15},
#                                        {"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]))


# Python's Dynamic Classes #1
# Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers), but starting only with upper case letter. In other case it should raise an exception.
# Disclaimer: there are obviously betters way to check class name than in example cases, but let's stick with that, that Timmy yet has to learn them.

# def class_name_changer(cls, new_name):
#     if new_name[0].isupper() and new_name.isalnum():
#         cls.__name__ = new_name
#     else:
#         raise Exception("error")

# Person Class Bug
# The following code was thought to be working properly, however when the code tries to access the age of the person instance it fails.
#
# person = Person('Yukihiro', 'Matsumoto', 47)
# print(person.full_name)
# print(person.age)
#
# For this exercise you need to fix the code so that it works correctly.
#
# Note: the order of the person's full name is first name and last name.

# class Person():
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full_name = first_name + ' ' + last_name

# best practice
#class Person():

    # def __init__(self, first_name, last_name, age):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.age = age
    #
    # @property
    # def full_name(self):
    #     return f'{self.first_name} {self.last_name}'

# с использованием property and setters
# class Person():
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     @property
#     def first_name(self):
#         return self._first_name
#
#     @first_name.setter
#     def first_name(self, first_name):
#         self._first_name = first_name
#
#     @property
#     def last_name(self):
#         return self._last_name
#
#     @last_name.setter
#     def last_name(self, last_name):
#         self._last_name = last_name
#
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age

# First-Class Function Factory
# Write a function, factory, that takes a number as its parameter and returns another function.
#
# The returned function should take an array of numbers as its parameter, and return an array of those numbers multiplied by the number that was passed into the first function.
#
# In the example below, 5 is the number passed into the first function. So it returns a function that takes an array and multiplies all elements in it by five.
#
# Translations and comments (and upvotes) welcome!
# Example
#
# fives = factory(5)          # returns a function - fives
# my_array = [1, 2, 3]
# fives(my_array)             # returns [5, 10, 15]

# def factory(x):
#     def fives(arr):
#         arr_new = []
#         for i in range(len(arr)):
#             arr_new.append(arr[i] * x)
#         return arr_new
#     return fives

# # best practice1
# def factory(x):
#     # Good Luck!
#     def _factory(y):
#         return [i*x for i in y]
#     return _factory
#
# # best practice2
# def factory(x):
#     return lambda ar: [x*el for el in ar]
#
# # best practice3
# factory=lambda x:lambda a:[x*e for e in a]
#
# #best practice with class
# class factory:
#
#     def __init__(self, num):
#         self.num = num
#
#     def __call__(self, arg):
#         return [i * self.num for i in arg]

# fives = factory(5)  # returns a function - fives
# my_array = [1, 2, 3]
# print(fives(my_array))

# Yoga Class
# Lets imagine a yoga classroom as a Square 2D Array of Integers classroom, with each integer representing a person, and the value representing their skill level.
#
# classroom = [
#             [3,2,1,3],
#             [1,3,2,1],
#             [1,1,1,2],
#             ]
#
# poses = [1,7,5,9,10,21,4,3]
#
# During a yoga class the instructor gives a list of integers poses representing a yoga pose that each person in the class will attempt to complete.
#
# A person can complete a yoga pose if the sum of their row and their skill level is greater than or equal to the value of the pose.
# Task
#
# Your task is to return the total amount poses completed for the entire classroom.
# Example
#
# classroom = [
#             [1,1,0,1], #sum = 3
#             [2,0,6,0], #sum = 8
#             [0,2,2,0], #sum = 4
#             ]
#
# poses = [4, 0, 20, 10]
#
# 3 people in row 1 can complete the first pose
# Everybody in row 1 can complete the second pose
# Nobody in row 1 can complete the third pose
# Nobody in row 1 can complete the fourth pose
#
# The total poses completed for row 1 is 7
#
# You'll need to return the total for all rows and all poses.
#

# def yoga(classroom, poses):
#     total = 0
#     arr_sum_row = []
#     for i in range(len(classroom)):
#         sum_row = 0
#         for j in range(len(classroom[i])):
#             sum_row += classroom[i][j]
#         arr_sum_row.append(sum_row)
#     for i in range(len(classroom)):
#         for j in range(len(classroom[i])):
#             classroom[i][j] += arr_sum_row[i]
#             for n in range(len(poses)):
#                 if classroom[i][j] >= poses[n]:
#                     total += 1
#     return total
# best practice
# def yoga(classroom, poses):
#     total_poses = 0
#     for pose in poses:
#         for row in classroom:
#             for person in row:
#                 if person + sum(row) >= pose:
#                     total_poses += 1
#     return total_poses

#best practice 2
# def yoga(classroom, poses):
#     return sum(1 for r in classroom for v in r for p in poses if p<=v+sum(r))
# print(yoga([
#             [3,2,1,3],
#             [1,3,2,1],
#             [1,1,1,2],
#             ], [1,7,5,9,10,21,4,3]))

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
#     def __init__(self, lst):
#         self.lst = lst
#         self.length = len(self.lst)
#         self.index = 0
#
#     def to_the_right(self):
#         if self.index == 0:
#             self.index = (self.index + 1) % self.length
#             return 1
#         else:
#             index_new = self.index + 1
#             self.index = (self.index + 1) % self.length
#             return index_new
#
#     def to_the_left(self):
#         if self.index == 0:
#             self.index = (self.index - 1) % self.length
#             return -1
#         else:
#             index_new = (self.index - 1) % self.length
#             self.index -= 1
#             return index_new
#
#     def display(self):
#         temp = self.lst.copy()
#         temp[self.index] = [self.lst[self.index]]
#         return str(temp)
#
# #best practice
# # class Menu:
# #     def __init__(self, menu: list) -> None:
# #         self.menu = menu
# #         self.index = 0
# #         self.length = len(menu)
# #
# #     def to_the_right(self) -> None:
# #         self.index = (self.index + 1) % self.length
# #
# #     def to_the_left(self) -> None:
# #         self.index = (self.index - 1) % self.length
# #
# #     def display(self) -> str:
# #         temp = self.menu.copy()
# #         temp[self.index] = [self.menu[self.index]]
# #         return str(temp)
#
#
#
# lst = Menu([1, 2, 3, 4, 5])
#
# print(Menu.display(lst))
# print(Menu.to_the_left(lst))
# print(Menu.display(lst))
# print(Menu.to_the_left(lst))
# print(Menu.display(lst))






# tasks with *
# Anything
# What is the answer to life the universe and everything
#
# Create a function that will make anything true
#
#     anything({}) != [],          'True'
#     anything('Hello') < 'World', 'True'
#     anything(80) > 81,           'True'
#     anything(re) >= re,          'True'
#     anything(re) <= math,        'True'
#     anything(5) == ord,          'True'

# def anything(thing):
#     return Anything('g', 2, False)
# """
#     The "anything" function returns an object that has overloaded magic comparison methods:
#         __lt__(self, other)
#         __le__(self, other)
#         __eq__(self, other)
#         __ne__(self, other)
#         __gt__(self, other)
#         __ge__(self, other)
#     Due to polymorphism, these methods accept objects of any type,
#     because the result of their operation is independent and is always True.
#     Therefore, it does not matter what we pass to the function anything,
#     because it will always return an object for which the comparison operations will give
#     the result True.
#     """
# class Anything:
#     def __lt__(self, *args):
#         return True
#     def __le__(self, *args):
#         return True
#     def __eq__(self, *args):
#         return True
#     def __ne__(self, *args):
#         return True
#     def __gt__(self, *args):
#         return True
#     def __ge__(self, *args):
#         return True

# Make Class
#I don't like writing classes like this:

# class Animal:
#     def __init__(self, name, species, age, health, weight, color):
#         self.name = name
#         self.species = species
#         self.age = age
#         self.health = health
#         self.weight = weight
#         self.color = color
#
# Give me the power to create a similar class like this:
#
# Animal = make_class("name", "species", "age", "health", "weight", "color")


def make_class(*args):
    class Animal:
        def __init__(self, *values):
            self.__dict__ = {args[i]: values[i] for i in range(len(values))}
    return Animal

# best practice
# def make_class(*args):
#     class MyClass:
#         def __init__(self, *vals):
#             self.__dict__ = {x:y for x,y in zip(args, vals)}
#     return MyClass

#best pactice 2
# from dataclasses import make_dataclass
#
# def make_class(*args):
#     return make_dataclass('Animal', args)


Animal1 = make_class("name", "species", "age", "health", "weight", "color")
dog1 = Animal1("Bob", "Dog", 5, "good", "50lb", "brown")
# print(Animal1.keys)
print(dog1.__dict__.items())
print(dog1.__dict__.keys())
print(dog1.__dict__.values())