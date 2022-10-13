# 3 - dars Matnlar bilan ishlash (STRING)

# Unicode-table.com

# ism = "Rustam"
# viloyat = "Farg`ona"
# shahar = "Qo`qon"
# matn = "Men yangi 🚗 oldim"
# smayl = "😀"

""" STRING ustida amallar bajarish"""

# ism = "Rustam"
# print("Mening ismim " + ism)

# ism = "Muhammad"
# familiya = "Isroilov"
# print(familiya + ' ' + ism)

""" f-STRING # matinlarni birlashtirish uchun """

# ism = "Rustam"
# familiya = "Isroilov"
# ism_familiya = f"{familiya} {ism}"
# print(ism_familiya)

# ism = "Rustam"
# print(f"Mening ismim {ism} sz bilan tanishganimdan hursandman")

""" MAXSUS BELGILAR """

# print("Hello World")

""" \t bilgidan keyin (tab) tashlanadi """
# print("Hello \tWorld")

""" \n belgidan keyin keyingi qatorga o`tadi """
# print("Hello \nWorld")

""" STRING METODLAR """

# ism = "jems"
# familiya = "bond"
# ism_familiya = f"{ism} {familiya}"

""" upper() -> Barcha harflarni kota qiladi """
# print(ism_familiya.upper())

""" lower() -> Barcha harflarni kichkina qiladi """
# print(ism_familiya.lower())

""" title() -> Har bir so`zni 1 harfini kota qiladi """
# print(ism_familiya.title())

""" capitalize() -> Matindagi 1 harfni kota qiladi """
# print(ism_familiya.capitalize())

""" STRING INPUT() """

# ism = input("Ismingizni kiriting? ")
# print("Assalom alaykum " + ism)

""" Foydalanuvchi nomini keyingi qatordan yozish """
# ism = input("Ismingizni kiriting?\n")
# print("Assalom alaykum " + ism.title())

