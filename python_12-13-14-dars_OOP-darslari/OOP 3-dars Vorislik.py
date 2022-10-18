""" OOP 3-dars VORISLIK """

"""Super klass"""


class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


# inson = Shaxs("Hasan", "Alimov", "FB001122", 1995)
# print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")


"""Talaba degan Voris klass"""


class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)  # super() operatoridan foydalanamiz
        self.idraqam = idraqam
        self.manzil = manzil
        self.bosqich = 1

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich


# talaba = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012")
# print(talaba.get_info())
# print(f"{talaba.get_info()}. ID raqami:{talaba.get_id()}")

""" OBYEKT ICHIDA OBYEKT """


class Manzil:
    """Manzil saqlash uchun klass"""

    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil


talaba_manzil = Manzil(12, 'Olmazor', "Bog'bon", "Samarqand")
talaba = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012", talaba_manzil)
print(talaba.manzil.get_manzil())

"""
Talaba klassiga yana bir, fanlar degan xususiyat qo`shing.
Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo`sh ro`yxatdan iborat bo`lsin (self.fanlar=[])
"""
