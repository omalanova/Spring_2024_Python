# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private.
#     Соответственно, для получения значений этого атрибута нужно использовать методы get и set
# class Plant:
#     def __init__(self, type, name, area, __industrial_use):
#         self.type = type
#         self.name = name
#         self.area = area
#         self.__industrial_use = __industrial_use
#
#     def hello(self):
#         return f'{self.name} belongs to the {self.type} and grows in the {self.area}'

    # @property
    # def cultivation(self, growth):
    #     self.growth = growth
    #     return f'Cultivation of {self.name} is {self.growth}'

# plant1 = Plant('flower', 'rose', 'Europe', False)
# plant2 = Plant('conifers', 'pine', 'North hemisphere', True)
#
# print(plant1.hello())
# print(plant2.hello())
# print(plant2.cultivation)

# 5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий

# создание классов с группой
# class Pet:
#
#     def __init__(self, name, paws, ears, tail, speak):
#         self.name = name
#         self.paws = paws
#         self.ears = ears
#         self.tail = tail
#         self.speak = speak
#
#     def speaking(self):
#         return f'{self.name} {self.speak}s'
#
# class Cat(Pet):
#
#     def __init__(self, name, paws, ears, tail, speak, hobbie):
#         super().__init__(name, paws, ears, tail, speak)
#         self.hobbie = hobbie
#
#     def fav_habbit(self):
#         return f'{self.name} likes to do {self.hobbie}'
#
#
#
# cat1 = Cat('Peach', 4, 2, True, 'meow', 'scratching')
# print(cat1.__dict__)
# print(cat1.speaking())
# print(cat1.fav_habbit())
#
#
# class Pet:
#
#     def __init__(self, name, paws, ears, tail, speak):
#         self.name = name
#         self.paws = paws
#         self.ears = ears
#         self.tail = tail
#         self.speak = speak
#
#     def speaking(self):
#         return f'{self.name} {self.speak}s'
#
#
# class Cat(Pet):
#
#     def __init__(self, name, paws, ears, tail, speak, hobbie):
#         super().__init__(name, paws, ears, tail, speak)
#         self.hobbie = hobbie
#
#     def fav_habbit(self):
#         return f'{self.name} likes to do {self.hobbie}'
#
#
# cat1 = Cat('Peach', 4, 2, True, 'meow', 'scratching')
# print(cat1.__dict__)
# print(cat1.speaking())
# print(cat1.fav_habbit())
#
# class Cow(Pet):
#
#     def __init__(self, name, paws, ears, tail, feed, color="Brown"):
#         super().__init__(name, paws, ears, tail, speak='MOOOOO')
#         self.feed = feed
#         self.color = color
#
#
#     def feeding(self):
#         return f'The cow {self.name} with {self.paws} {self.color} is give us a tasty {self.feed}'
#
# cow = Cow("Burka", "hooves", 'curly', 'long brown', 'utilizion grass')
# print(cow.feeding())
# print(cow.speaking())