"""
This function calculates the sum of all natural numbers below a given number that are multiples of 3 or 5.

Args:
    n (int): The upper limit (exclusive) up to which to find the sum of multiples of 3 or 5.

Returns:
    int: The sum of all multiples of 3 or 5 below the given number.

Example:
    If we call f(10), the function will find all multiples of 3 or 5 below 10, which are 3, 5, 6, and 9.
    The sum of these multiples is 23, so the function will return 23.
"""


def f(n):
    result = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:  # check if divisible by 3 or 5 without remainder
            result += i
    return result


print(f(1000))  # Expected output: 233168
"""
This Python code defines a function `f(n)` that calculates the sum of all natural numbers below a given number `n` 
                                                                                    that are multiples of 3 or 5. 
It iterates through all numbers below `n` and checks if each number is divisible by 3 or 5 without remainder. 
If it is, the number is added to the `result`. Finally, it returns the sum of all such multiples. 
The example provided calls the function with an argument of 1000 and prints the result.
"""
