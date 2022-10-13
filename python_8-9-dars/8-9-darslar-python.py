#  8 - 9 - darslar LIST lar bilan ishlash


""" Mevalar ro`yxati (matnlar) """
# mevalar = ['olma', 'anjir', 'shaftoli', 'o`rik']

# narhlar ro`yxati (raqamlar)
# narhlar = [12000, 25000, 14000, 20000]

""" Aralash ro`yxat """
# aralash = ['olma', 1200, 'banan', 20]

""" Bo`sh ro'yxat """
# ismlar = []

# print("Birinchi meva:", mevalar[0])
# print("Ikkinchi meva:", mevalar[2])
# print("Ohirgi meva:", mevalar[-1])
# print("Birinchi meva:", mevalar[0].title())
# print("Ikkinchi meva:", mevalar[2].upper())

# print(narhlar[0] + narhlar[2])

""" Qiymatni o`zgartirish """
# print(narhlar[1] + 10000)


""" .append() Mevalar royxatiga qo`shish """
# mevalar.append("uzuzm")
# print(mevalar)


""" .insert() Mevalar royxatini istalgan joytidan qo`shish """
# mevalar.insert(2, "banan")
# print(mevalar)


""" .del() indexdagi elementni olip tashlash 
.remove() aytilgan elementni o`chiradi """
# cars = []
# cars.append("Lasetti")
# cars.append("Nexia")
# cars.append("Cobalt")
# cars.append("Damas")
# print(cars)
# del cars[0]
# cars.remove("Cobalt")
# print(cars)


""" .sort() Alfabit bo`yicha sartirofka """
# cars = ['Bmw', 'mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
# cars.sort()
# print(cars)


""" .sort(reverse=True Alfabit bo`yicha teskari sartirofka """
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)



""" .sort() metodi ro'yxatni tartiblaydi.
Ba'zida asl ro'yxat ichidagi elementlarning ketma-ketligini
buzmagan holda ro'yxatni tartiblash talab qilinishi mumkin.
Buning uchun sorted() funktsiyasidan foydalanamiz: """

# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)

# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
""" sorted() funktsiyasi yordamida teskari tartiblash uchun ham reverse=True argumentini beramiz: """
# print(sorted(ages, reverse=True))

""" .pop()    royxatdan elementni sug`urib olish """

# bozorlik = ['yog`', 'un', 'piyoz', 'sabzi', 'go`sht']
# mahsulot = bozorlik.pop(3)
# print(mahsulot)
# print(bozorlik)
# print('Men', mahsulot, 'sotib oldim')
# print('Shu maxsulotlar qoldi', bozorlik)

""" .len() Ro`yxatning uzunligi
Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun len() funktsiyasidan foydalanamiz:  """
# cars = ['bmw', 'mercedes_benz', 'volvo', 'general_motors', 'tesla', 'audi']
# uzunligi = len(cars)
# print(uzunligi)

""" range() Funksiyasi
 Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin.
 list() funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz: """
# sonlar = list(range(0,10))
# print(sonlar)


# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)



""" Ro`yxat ustida xar-xil amallar bajarish """

# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)    # eng kichigi
# qimmat = max(narhlar)   # eng kotasi
# jami = sum(narhlar)     # jami narhlar yig`indisi
# print("Eng arzon narh ", arzon, "\nEng qimmati ", qimmat, "\nJami: ", jami)

""" Ro`yxatni kesish """

# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# print(cars[0:3])       # 0-indeskdan boshlab 3 ta element ajratib olamiz
# print(cars[2:5])       # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)
# print(cars[:4])        # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(cars[2:])        # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi
#
"""       a = [int(i) for i in input().split()]   """

# a = "salom__python__men__developerman"
# b = a.split('__')
# print(b)
# print(*b)

# a = '1 2 3 4 5 6 7 8 9'
# b = a.split()
# print(b)
# for i in range(len(b)):
#     b[i] = int(b[i])
# print(b)
# print(sum(b))

# b = input().split()
# print(b)
# for i in range(len(b)):
#     b[i] = int(b[i])
# print(b)
# print(sum(b))

# b = input().split()
# print(b)
# a = []
# for i in b:     # b = input().split()
#     a.append(int(i))
# print(sum(a))

# a = [int(i) for i in input().split()]

""" .join() Teskarisiga qaytarish """

# string = '1__2__3__4__5__6'
# print(string)
# massiv = string.split('__')
# print(massiv)
# amal = massiv[::-1]
# print(amal)
# qayt = '__'.join(amal)
# print(qayt)

