# 7-Dars While()


# son = 1
"""toki 10 dan kichik yoki teng ekan..."""
# while son <= 10:

"""soni konsolga chiqaramiz"""
    # print(son, end=' ')

""" songa 1 qo`shamiz """
    # son += 1


"""While() and input()"""

# print('Kiritilgan soni kvadratini qaytaruvchi dastur.')
# savol = "Istalgan soni kiriting "
# savol += "(dasturni to`xtatish uchun exit deb yozing) --> "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat) ** 2)
# print('Dastur to`xtadi__')

""" Ishora """

# print('Kiritilgan son kvadratini qaytaruvchi dastur.')
# savol = "Istalgan soni kiriting "
# savol += "(dasturni to`xtatish uchun exit deb yozing) --> "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(int(qiymat) ** 2)
# print('Dastur to`xtadi__')

""" While() and break """

# print('Kiritilgan son kvadratini qaytaruvchi dastur.')
# savol = "Istalgan soni kiriting "
# savol += "(dasturni to`xtatish uchun exit deb yozing) --> "
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat) ** 2)
# print('Dastur to`xtadi__')

""" CONTINUE """

# son = 0
# while son <= 10:
#     son += 1
#     if son % 2 != 0:
"""if dan o`tgan son ni tashlab ketadi"""
#         continue
#     else:
#         print(son, end=' ')

# sonlar = list(range(1, 10))
# for son in sonlar:
#     if son == 5:
"""5 ni tashlab ketadi"""
#         continue
#     print(son ** 2, end=' ')


"""Abadi sikil"""

# son = 1
# while son >= 0:
#     son += 1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son, end=' ')
