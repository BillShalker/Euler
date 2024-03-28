import time

results = {}


def is_double(n):
    return True if n % 2 == 0 else False


for i in range(1, 1000000):
    n = i
    doubles = []
    while n != 1:
        if n in results:
            for j in results[n]:
                doubles.append(j)
                n = 1
        elif is_double(n):
            n /= 2
            doubles.append(n)
        elif not is_double(n):
            n = 3 * n + 1
            doubles.append(n)
    results[i] = doubles

for i in results:
    print(f"{i}: {int(len(results[i])) + 1}")
