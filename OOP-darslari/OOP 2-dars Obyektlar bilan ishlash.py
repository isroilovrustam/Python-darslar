""" OOP 2-dars Obyektlar bilan ishlash """

""" Talabaning xususiyatlariga metodlar orqali murojat qilish """


class Talaba:  # Klass
    """Talaba nomli klass yaratamiz"""

    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        """ standart qiymatli xususiyat """
        self.bosqich = 1

    # talaba1 = Talaba("Alijon", "Valiyev", 2000)
    # print(talaba1.get_info())


    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

    def get_name(self):
        """ Talabaning ismini qaytaruvchi Metod """
        return self.ism

    def get_lastname(self):
        """ Talabaning familiyasini qaytaruvchi Metod """
        return self.familiya

    def set_bosqich(self, bosqich):
        """ Talabaning kursini yangilovchi metod """
        self.bosqich = bosqich

    def update_bosqich(self):
        """ Talabanining bosqichini 1taga ko'paytirish """
        self.bosqich += 1

    def get_bosqich(self):
        """ Talabaning bosqichini qaytaruvchi Metod """
        return self.bosqich

talaba1 = Talaba("Alijon", "Valiyev", 2000)
# talaba1.bosqich = 2
# talaba1.set_bosqich(3)
print(talaba1.get_info())


class Talaba:  # Klass
    """Talaba nomli klass yaratamiz"""

    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}."



class Fan:  # Fan degan Klass
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_students(self):
        talabalar = []
        # for talaba in self.talabalar:
        #     talabalar.append(talaba.get_info())
        # return talabalar
        return [talaba.get_info() for talaba in self.talabalar]


# Agar OOP bo`lmaganda
# talaba1_ism = 'Alijon'
# talaba1_familiya = 'Valijonov'

matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon", "Valiyev", 2000)
talaba2 = Talaba("Hasan", "Alimov", 2001)
talaba3 = Talaba("Akrom", "Boriyev", 2001)

matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

print(matematika.get_students())

print(f'Oliy Matematika fanini o`qidigon Talabalar soni {matematika.talabalar_soni}')


"""Qisqa qo`shimcha ma'lumotlar"""
# print(dir(Talaba))
# """ __init__ shunga o`xshash metodlar Dunder metodlar (Dander) """
#
#
# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]
#
# print(see_methods(Talaba))
