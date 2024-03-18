"""
11. Ixtiyoriy n (0≤n≤9) raqamni switch operatoridan
foydalanib, so’zlar bilan ifodalaydigan, ixtiyoriy hafta kuni m (1≤m≤7) nimos haftaning kuni (dushanba, seshanba va h.k.) orqali ifodalaydigan,
ixtiyoriy oy nomeri k (1≤k≤12) ni oy nomlari orqali ifodalaydigan
parametri va uchta metodli klass yarating. Asosiy programmada bu klass
turidagi obyekt hosil qiling. Masalalar yeching.
Klass konstruktoriga doir misollar
"""

class Kalendar:
    def __init__(self):
        pass

    def day_of_week(self, d):
        switcher = {
            1: "Dushanba",
            2: "Seshanba" ,
            3: "Chorshanba",
            4: "Payshanba",
            5: "Juma",
            6: "Shanba",
            7: "Yakshanba"
        }
        return switcher.get(d, "Noto'g'ri hafta kuni kiritildi.")

    def month_of_year(self, m):
        switcher = {
            1: "Yanvar",
            2: "Fevral",
            3: "Mart",
            4: "Aprel",
            5: "May",
            6: "Iyun",
            7: "Iyul",
            8: "Avgust",
            9: "Sentyabr",
            10: "Oktuabr",
            11: "Noyabr",
            12: "Dekabr"
        }
        return switcher.get(m, "Notog'ri oy raqami kiritildi!")

# Test qilish
kalendar = Kalendar()

d = int(input("Kun raqamini kiriting : "))
m = int(input("Oy raqamini kiriting : "))

print(f"{d}-raqamdagi kun = {kalendar.day_of_week(d)}")
print(f"{m}-raqamdagi oy = {kalendar.month_of_year(m)}")
