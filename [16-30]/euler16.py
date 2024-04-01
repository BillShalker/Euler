"""
This script calculates the sum of digits of a number raised to a given power.

Explanation:
    The script defines a function `sum_of_digits` to compute the sum of digits of a number raised to a given power.
    It takes two arguments: `n` (the base number) and `power` (the exponent, with a default value of 1).
    Within the function, it first calculates the result of raising `n` to the power of `power`.
    Then, it iterates over each digit in the string representation of the result and adds them together.
    Finally, it returns the sum of digits as an integer.

Args:
    n (int): The base number.
    power (int, optional): The exponent (default is 1).

Returns:
    int: The sum of digits of the number raised to the given power.

Example:
    Calling the function with `n=2` and `power=1000` computes 2^1000 and returns the sum of its digits.
    The function calculates the result of 2^1000, iterates over each digit in the resulting number,
    and returns the sum of digits as the final result.
"""


def sum_of_digits(n: int, power: int = 1) -> int:
    """Compute the sum of digits of a number raised to a given power."""
    result = 0
    # Calculate the result of raising n to the power of power
    num = n ** power
    # Iterate over each digit in the string representation of
    for i in str(n ** power):
        result += int(i)
    return result


print(sum_of_digits(2, 1000))  # Expected output: 1366
