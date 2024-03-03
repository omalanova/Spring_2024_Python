# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private.
#     Соответственно, для получения значений этого атрибута нужно использовать методы get и set
class Plant:
    def __init__(self, type, name, area, __industrial_use):
        self.type = type
        self.name = name
        self.area = area
        self.__industrial_use = __industrial_use

    def hello(self):
        return f'{self.name} belongs to the {self.type} and grows in the {self.area}'

    # @property
    # def cultivation(self, growth):
    #     self.growth = growth
    #     return f'Cultivation of {self.name} is {self.growth}'

plant1 = Plant('flower', 'rose', 'Europe', False)
plant2 = Plant('conifers', 'pine', 'North hemisphere', True)

print(plant1.hello())
print(plant2.hello())
# print(plant2.cultivation)

# 5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий