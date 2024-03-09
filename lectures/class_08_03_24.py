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
#         for x in range(len(st)):
#             print(st[x])
#             if letter == st[x]:
#                 list.append(x)
#         return (list[0], list[-1])
# print(first_last('a', 'banana'))

# с использованием функций find, rfind
# def first_last(letter, st):
#     index = st.find(letter)
#     if index < 0:
#         return (None, None)
#     last_index = st.rfind(letter)
#     return index, last_index
#
# print(first_last('a', 'banana'))

# def str_clean(st):
#     l = []
#     for i in st:
#         if i != '@':
#             l.append(i)
#         else:
#             l.pop()
#     return ''.join(l)
# print(str_clean('bt@aw@nw@ad@nb@ai@'))

