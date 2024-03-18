"""
This script finds the largest prime factor of a given number.

Args:
    n (int): The number for which to find the largest prime factor.

Returns:
    int: The largest prime factor of the given number.

Example:
    If we call the script and enter the number 600851475143, it will find and print the largest prime factor.

Note:
    A prime factor is a prime number that divides another number without leaving a remainder.
    The script first finds all divisors of the number, then iterates through them in reverse order to find the largest prime factor.
    It checks each divisor to see if it is prime using the `is_prime` function.
"""


def is_prime(n):  # simple solution
    if n == 2 or n == 1:
        return True
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


if __name__ == "__main__":
    number = int(input("Enter number: "))  # 600851475143

    for el in all_dividers(number)[::-1]:
        if is_prime(el):
            print(el)  # Expected output: 6857
            break

"""
This function `all_dividers(n)` finds all the divisors of a given number.
To find divisors, it iterates through numbers from 1 up to the square root of the given number.
If a number divides the given number without leaving a remainder, it's considered a divisor.
The function returns a list containing all such divisors, including both the divisor itself and the result of dividing the given number by it.
It also ensures that if the given number is a perfect square, its square root is counted only once.

"""
