from euler3 import is_simple
import math

number = int(input("Enter number(from 1 to n): "))


def list_of_prime_numbers(n):
    result = []
    for i in range(n):
        if is_simple(i):
            result.append(i)
    return result


def least_common_multiple(n):
    result = 1
    for el in list_of_prime_numbers(n):
        result *= math.floor(math.log(n, n))
    return result


print(least_common_multiple(number))
