"""
5. 1+2+3+…+n yig’indini va 1·2·3·...·n ko’paytmani
hisoblashni o’z ichiga ilgan parametrili va bir nechta metodli klass yarating .
Asosiy programmada bu klass turidagi obyekt hosil qiling. Masalalar
yeching.
"""

class Hisoblash:
    def __init__(self, n):
        self.n = n
    
    def yigindi(self):
        return sum(range(1, self.n + 1))
    
    def kopaytma(self):
        result = 1
        for i in range(1, self.n + 1):
            result *= i
        return result

n = int(input("n ni kiriting: "))

hisoblash_obj = Hisoblash(n)
yigindi = hisoblash_obj.yigindi()
kopaytma = hisoblash_obj.kopaytma()

print(f"{n} gacha sonlar yig'indisi:", yigindi)
print(f"{n} gacha sonlar ko'paytmasi:", kopaytma)