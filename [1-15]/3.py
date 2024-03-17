"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def is_simple(n):  # simple solution
    if n % 2 == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def all_dividers(n):
    m = n ** 0.5
    result = []
    for i in range(1, int(m) + 1):
        if n % i == 0:
            result.append(i)
            if n // i != i:
                result.append(n // i)
    return result


number = int(input("Enter number: "))  # 600851475143

for el in all_dividers(number)[::-1]:
    if is_simple(el):
        print(el)  # 6857
        break

"""
def all_dividers(n):
    1)Find the square root of  N and round it down to the nearest whole number, let's denote it as M. 
    2)For each number i in the range from 1 to M, inclusive, perform the following steps:
        -If N is divisible by i without a remainder, then i and / N/i are divisors of N. 
    3)Take into account that if  N is a perfect square, then its square root will be counted twice. In such a case,
        add it to the list of divisors only once.

"""
