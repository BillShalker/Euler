"""
This script finds the first triangle number to have over N divisors, where N is provided as an argument.

Args:
    n (int): The target number of divisors.

Returns:
    int: The first triangle number to have over N divisors.

Explanation:
    Triangle numbers are generated by summing the natural numbers sequentially.
    The script calculates triangle numbers incrementally and checks each one for the number of divisors.
    It iterates through the triangle numbers until finding the first one with over N divisors.
    This is achieved by calculating the divisors of each triangle number and comparing the count with the target N.
    Once a triangle number with over N divisors is found, it is returned as the result.

Example:
    To find the first triangle number with over 500 divisors, the script calculates triangle numbers incrementally,
    checks each one for the number of divisors, and returns the first one that exceeds 500 divisors.
"""

from euler3 import all_dividers  # Import function to calculate all dividers of a number


def triangle_number_with_n_divisors(n):
    result = 0  # Initialize the result
    add = 1  # Variable to add to the result to generate triangle numbers
    # Iterate until finding the first triangle number with over N divisors
    while len(all_dividers(result)) < n:
        result += add  # Calculate the next triangle number
        add += 1  # Increment the add variable for the next iteration
    return result  # Return the first triangle number with over N divisors


print(triangle_number_with_n_divisors(500))  # Print the result

# Expected output: 76576500
