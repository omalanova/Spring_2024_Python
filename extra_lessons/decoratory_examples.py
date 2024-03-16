def bread(func):
    def wrapper():
        print ("</------\>")
        func()
        print ("<\______/>")

    return wrapper


def ingredients(func):
    def wrapper():
        print ("#помидоры#")
        func()
        print ("~салат~")

    return wrapper


def sandwich(food="--ветчина--"):
    print (food)


sandwich()
# выведет: --ветчина--
sandwich = bread(ingredients(sandwich)) # один способ записи декоратора
sandwich()
# выведет:
# </------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>

@bread
@ingredients
def sandwich(food="--ветчина--"): #еще один способ записи декоратора
    print (food)


sandwich()
# выведет:
# </------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>

@ingredients
@bread
def sandwich(food="--ветчина--"): # порядок декорирования ВАЖЕН
    print (food)


sandwich()
# выведет:
# #помидоры#
# </------\>
# --ветчина--
# <\______/>
# ~салат~