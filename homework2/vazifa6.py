"""6. 1·1+2·2+3·3+...+n·n yig’indini hisoblang."""

class Hisoblash:
    def __init__(self, n):
        self.n = n
    
    def yigindini_hisoblash(self):
        return sum(i * i for i in range(1, self.n + 1))

n = int(input("n ni kiriting : "))
hisoblash = Hisoblash(n)
natija = hisoblash.yigindini_hisoblash()
print(f"{n} gacha sonlar ko'paytmasi va yig'indisi : ", natija)