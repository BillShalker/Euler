"""
This script calculates the sum of all prime numbers below a given limit.

Args:
    n (int): The upper limit of prime numbers to consider.

Returns:
    int: The sum of all prime numbers below the given limit.

Explanation:
    The function `sum_of_prime_numbers(n)` takes an integer `n` as input, representing the upper limit of prime numbers to consider.
    It iterates through all numbers from 1 to `n-1`, inclusive, and checks if each number is prime using the `is_prime()` function imported from the `euler3` module.
    If a number is prime, it adds it to the running sum `result`.
    Finally, the function returns the total sum of all prime numbers below the given limit.

Note:
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    The `is_prime()` function used in this script checks whether a given number is prime.

Example:
    Calling the function `sum_of_prime_numbers(2000000)` will calculate the sum of all prime numbers below 2,000,000.
    The result is then printed to the console.
"""

from euler3 import is_prime


def sum_of_prime_numbers(n):  # returns sum of prime numbers
    result = 0
    for i in range(1, n):
        if is_prime(i):
            result += i
    return result


print(sum_of_prime_numbers(2000000))

# Expected output: 142913828922
