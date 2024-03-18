"""
10. Berilgan K soniga qoldiqsiz bo’linadigan birinchi N
ta sonni toping.
"""
class Numbers:
    def __init__(self, k):
        self.k = k
    def son(self, N):
        numbers_found = []
        number = 1
        while len(numbers_found) < N:
            if number % self.k == 0:
                numbers_found.append(number)
            number += 1
        return numbers_found

k = 3
N = 5
numbers = Numbers(k)
first_N_numbers = numbers.son(N)
print(f"{N} ta son topildi, ular: {first_N_numbers}")
