"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
"""

from euler3 import is_prime
import math

number = int(input("Enter number(from 1 to n): "))


def list_of_prime_numbers(n):  # returns list of prime numbers
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result


def least_common_multiple(n):
    result = 1
    for el in list_of_prime_numbers(n):
        result *= el ** math.floor(math.log(n, el))
    return result


print(least_common_multiple(number))

"""
    Import Libraries: Import the necessary libraries. In this case, the code imports a function is_prime from a module named euler3, and the math library.

        1)Input: Prompt the user to input a number (number) from 1 to n.

        2)Define Function list_of_prime_numbers: This function generates a list of prime numbers up to the input number n. It initializes an empty list result. Then, it iterates through numbers from 2 to n - 1. For each number i in this range, it checks if i is prime using the is_prime function. If i is prime, it appends it to the result list. Finally, it returns the list of prime numbers.

        3)Define Function least_common_multiple: This function calculates the least common multiple (LCM) of a number n. It initializes a variable result to 1. Then, it iterates through each prime number (el) obtained from the list_of_prime_numbers function. For each prime number el, it multiplies result by el raised to the power of the floor of the logarithm base el of n. This effectively calculates the highest power of each prime number that is less than or equal to n. The result is the LCM of all prime numbers up to n.

        4)Print LCM: Print the least common multiple calculated by calling the least_common_multiple function with the input number.

    This algorithm computes the least common multiple of all prime numbers up to a given input number n.
    """
