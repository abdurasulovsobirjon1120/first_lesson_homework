"""7. 1·n+2·(n ‒1)+3·(n ‒2)+...+n·1 yig’indini hisoblang."""

class Hisoblash:
    def __init__(self, n):
        self.n = n
    
    def yigindini_hisobla(self):
        yigindi = sum(i * (self.n - i + 1) for i in range(1, self.n + 1))
        return yigindi

n = int(input("n ni kiriting : "))
hisoblash_obj = Hisoblash(n)
natija = hisoblash_obj.yigindini_hisobla()
print("Natija = ", natija)