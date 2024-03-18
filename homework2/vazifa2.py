"""
2. Tomonlarining uzunligi ma‟lum bo’lgan
uchburchakka tegishli masalalarni yechish metodlarini o’z ichiga olgan
klass yarating. Asosiy programmada klass turidagi obyektlar hosil qiling.
Ulardan foydalanib, masalalarni yeching.
"""

import math
class Uchburchak:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetr(self):
        return self.a + self.b + self.c
    
    def yuza(self):
        s = self.perimetr() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

a = int(input("Uchburchakning 1-tomonini kiriting : "))
b = int(input("Uchburchakning 2-tomonini kiriting : "))
c = int(input("Uchburchakning 3-tomonini kiriting : "))

uchburchak = Uchburchak(a, b, c)
perimetr = uchburchak.perimetr()
yuza = uchburchak.yuza()

print("Uchburchak  perimetri:", perimetr)
print("Uchburchak  yuzasi:", yuza)