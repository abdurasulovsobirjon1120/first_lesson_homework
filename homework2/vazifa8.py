"""
8. Fibonachchi sonlari birinchi n tasining yig’indisini
toping .
"""

class Fibonachchi:
    def __init__(self, n):
        self.n = n

    def calculate_sum(self):
        if self.n <= 0:
            return 0
        elif self.n == 1:
            return 1
        else:
            fib_sequence = [0, 1]
            for i in range(2, self.n + 1):
                fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
            return sum(fib_sequence)

n_son = int(input("n qiymatini kiriting : "))

fib_instance = Fibonachchi(n_son)
result = fib_instance.calculate_sum()
print(f"Birinchi {n_son} Fibonachi sonlarining yig'indisi : {result}")
