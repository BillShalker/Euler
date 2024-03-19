"""
This script finds the smallest positive number that is evenly divisible by all numbers from 1 to a given number.

Args:
    None

Returns:
    int: The smallest positive number that is evenly divisible by all numbers from 1 to the given number.

Example:
    Running the script will prompt the user to input a number, and then it will calculate and print the smallest positive number
    that is evenly divisible by all numbers from 1 to the input number.

Note:
    The script first imports the necessary functions from the euler3 module and the math library.
    It then defines two functions: list_of_prime_numbers and least_common_multiple.
    The list_of_prime_numbers function generates a list of prime numbers up to a given number.
    The least_common_multiple function calculates the least common multiple (LCM) of all prime numbers up to a given number.
    Finally, the script prints the calculated LCM.

"""

from euler3 import is_prime
import math


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


if __name__ == "__main__":
    number = int(input("Enter number (from 1 to n): "))
    print(least_common_multiple(number))

"""
Explanation of the Algorithm:

1) Input: Prompt the user to input a number (number) from 1 to n.

2) Define Function list_of_prime_numbers: This function generates a list of prime numbers up to the input number n. It 
    initializes an empty list result. Then, it iterates through numbers from 2 to n - 1. For each number i in this range, 
    it checks if i is prime using the is_prime function. If i is prime, it appends it to the result list. Finally, 
    it returns the list of prime numbers.

3) Define Function least_common_multiple: This function calculates the least common multiple (LCM) of a number n. 
It initializes a variable result to 1. Then, it iterates through each prime number (el) obtained from the 
list_of_prime_numbers function. For each prime number el, it multiplies result by el raised to the power of 
the floor of the logarithm base el of n. This effectively calculates the highest power of each prime number that is
less than or equal to n. The result is the LCM of all prime numbers up to n.

4) Print LCM: Print the least common multiple calculated by calling the least_common_multiple function with the input 
                                                                                                                number.

This algorithm computes the least common multiple of all prime numbers up to a given input number n.
"""
