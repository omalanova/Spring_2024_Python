# Напишите функцию search_substr(subst, st), которая принимает 2 строки и определяет,
# имеется ли подстрока subst в строке st.
# В случае нахождения подстроки, возвращается фраза «Есть контакт!», а иначе «Мимо!».
# Должно быть найдено совпадение независимо от регистра обеих строк.

# def search_substr(subst, st):
#     if subst.lower() in st.lower():
#         return "Yes"
#     return "No"
#
# print(search_substr('str', 'ouiyStroka'))

# Требуется определить индексы первого и последнего вхождения буквы в строке.
# Для этого нужно написать функцию first_last(letter, st), включающую 2 параметра:
# letter – искомый символ, st – целевая строка.
# В случае отсутствия буквы в строке, нужно вернуть кортеж (None, None), если же она есть,
# то кортеж будет состоять из первого и последнего индекса этого символа.

# def first_last(letter, st):
#     l = []
#     if not letter in st:
#         return (None, None)
#     else:
#         for index, symbol in enumerate(st):
#             if letter in st:
#                 l.append(index)
#                 print(index)
#         return (l[0], l[-1])
# print(first_last('a', 'banana'))

def first_last(letter, st):
    index = st.find(letter)
    if index < 0:
        return (None, None)
    last_index = st.rfind(letter)
    return index, last_index

print(first_last('a', 'banana'))