"""
1. Ixtiyoriy ikkita son berilgan. Bu sonlar ustida
bajarilishi mumkin bo’lgan masalalarni yechish metodlarini o’z ichiga
olgan klass tuzing. Masalan, bu sonlarning yig’indisini, ayirmasini,
ko’paytmasini, nisbatini, maksimumini, mininumini, o’rta arifmetik
qiymatini, o’rta geometrik qiymatini va h.k.larni toping. Asosiy
programmada klass turidagi obyektlar hosil qiling. Ulardan foydalanib,
masalalarni yeching.
"""

import math
class Supercalc : 
  def __init__(self , son1 , son2):
    self.son1 = son1 
    self.son2 = son2
    
  def qoshish(self): 
    return self.son1 + self.son2
    
  def ayirish(self): 
    return self.son1 - self.son2
    
  def kopaytirish(self): 
    if self.son1 == 0 or self.son2 == 0: 
      print("Sonni nolga koʻpaytirib boʻlmaydi")
    else:
      return self.son1 * self.son2
      
  def bolish(self):  
    if self.son1 == 0 or self.son2 == 0: 
      print("Sonni nolga boʻlib boʻlmaydi !")
    else:
      return self.son1 / self.son2
      
  def maximum(self): 
    if self.son1 > self.son2: 
      return self.son1
    else:
      return self.son2
      
  def minimum(self): 
    if self.son1 > self.son2 : 
      return self.son2
    else:
      return self.son1    
        
  def ortaArifmetik(self) : 
    return (self.son1 + self.son2) / 2
    
  def ortaGeometrik(self) : 
    return (self.son1 * self.son2) ** 0.5
  
son1 = int(input("1-sonni kiriting : "))
son2 = int(input("2-sonni kiriting : "))

hisob = Supercalc(son1 , son2)

print("Birlashmasi = ", hisob.qoshish())
print("Ayirmasi = ", hisob.ayirish())
print("Ko'paytmasi = ", hisob.kopaytirish())
print("Bo'linmasi = ", hisob.bolish())
print("Kattasi = ", hisob.maximum())
print("Kichigi = ", hisob.minimum())
print("O'ta arifmetik = ", hisob.ortaArifmetik())
print("O'rta geometrik = ", hisob.ortaGeometrik())