""" OOP 1-dars KLASS va OBYEKT  (Class and Oject) """



"""                            OBYEKT NIMA?
 Object oriented dasturlashda o’zaro bo’gliq bo’lgan o’zgaruvchilar va
 funksiyalar bitta konteynerga jamlanadi va bunday konteynerlar obyekt deb ataladi.
 Bir obyektga tegishli o’zgaruvchilar uning xususiyatlari, unga tegishli funksiyalar esa metodlari deb ataladi. """

"""                             KLASS NIMA?
 Object oriented programming haqida gaplashar ekanmiz uning fundamental tushunchalaridan
 biri - klass haqida gapirib o’tmaslikning iloji yo’q.
 Klass bu obyekt yaratish uchun shablon yoki qolipdir.
 Bitta klassdan biz istalgancha nusxa olishimiz va yangi obyektlar yaratishimiz mumkin.
 Demak obyekt bu biror klassning xususiy ko’rinishi.
 Odatda klasslarning nomi o’zgarmas, undan yaratilgan obyektlar esa istalgancha nomlanishi mumkin."""


 x = 10
 print(type(x))      # <class 'int'>
# matn = "salom"
# print(type(matn))   # <class 'str'>

# def salom_ber():
#     print("Assalom alaykum")
#
# print(type(salom_ber))  # <class 'function'>

# class Person:        # Person Klacc
#     pass

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self, ism, familiya):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya

"""Obyekt xususiyatlarini kiritamiz"""
talaba1 = Talaba('Odil', "Hasanov")

print(talaba1.ism, talaba1.familiya)


class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self, ism, familiya, yil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.yil = yil

    def get_info(self):
        """Talaba haqida malumot qaytaruvchi metod"""
        return f"Ismim {self.ism} {self.familiya}. {self.yil} yilda tu'gilganman"

talaba1 = Talaba('Olim', 'Olimov', 2002)
talaba2 = Talaba("Olim", "Olimov", 1995)
talaba3 = Talaba("Husan", "Akbarov", 2004)
talaba4 = Talaba("Hasan", "Akbarov", 2004)


"""" --> Misol <-- """

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self, ism, yil, mat, fiz, das):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.yil = yil
        self.mat = mat
        self.fiz = fiz
        self.das = das
        self.av = (mat + fiz + das)/3


"""Talabalar ro`yxatini saqlash uchun list hosil qilib olamiz"""
talabalar = []

"""Obyekt hosil qilish uchun for siklidan foydalanamiz va yaratgan obyektni royxatga qo`shib boramiz"""
for i in range(3):
    print(f"{i+1} - Talabaning malumotlarini kiriting")
    talaba = Talaba(input('Ismi --> '), int(input('Yoshi --> ')), int(input('mat --> ')), int(input('fiz --> ')), int(input('das --> ')))
    talabalar.append(talaba)


"""Talabalar royxati va fanlardan olgan o`rtacha baholarini chiqarish uchun for ishlatamiz"""
for i in range(3):
    print(f"{i+1}-talaba {talabalar[i].ism}. O`rtacha bahosi -- > {int(talabalar[i].av)}")


"""Bu kod bizga max ball to`plagan talabani chiqarib beradi"""
max1 = talabalar[0].av
a = 1
for i in range(3):
    if talabalar[i].av > max:
        max1 = talabalar[i].av
        a = i+1
print(f'{a} - o`rinlik talaba {talabalar[a].av} ball olib 1-o`rini egaladi')
