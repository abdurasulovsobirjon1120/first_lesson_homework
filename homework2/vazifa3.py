"""
3. Ikki sondan eng kattasini va eng kichigini topish
uchun klass yaratining. Asosiy programmada bu klass turidagi obyektlar
yaratining. Klassdan foydalanib, ikkita sonning eng kattasini va eng
kichigini toping. Xuddi shuningdek, uchta sonning maxsimum va
minimumini topishda bu klassdan foydalaning.
Parametrli klasslarga doir misollar
"""

import math
class Maxmin: 
  def __init__(self , a, b):
    self.a = a 
    self.b = b
    
  def minimum(self): 
    return min(self.a , self.b)
    
  def maximum(self): 
    return max(self.a , self.b)
    
a = int(input("1-sonni kiriting : "))
b = int(input("2-sonni kiriting : "))

result = Maxmin(a,b)
minimum = result.minimum()
maximum = result.maximum()

print("min = ", minimum)
print("max = ", maximum)