"""
This script calculates the sum of letters needed to write out all numbers from 1 to a given number.

Explanation:
    The script utilizes the `num2words` library to convert each number from 1 to the given number into words.
    It defines a function `sum_letters` that takes an integer `n` as input.
    Within the function, it iterates over the range from 1 to `n` (inclusive).
    For each number, it converts it to words using `num2words`, removes hyphens and spaces, and calculates the length.
    Finally, it sums up the lengths of all words and returns the total.

Args:
    n (int): The upper limit of numbers to consider.

Returns:
    int: The sum of the lengths of all words representing numbers from 1 to the given number.

Example:
    Calling the function with `n=1000` calculates the sum of letters needed to write out all numbers from 1 to 1000.
    The function converts each number to words using `num2words`, removes hyphens and spaces,
    calculates the length of each word, and sums up all lengths to obtain the final result.
"""

from num2words import num2words  # Importing the num2words library


def sum_letters(n: int) -> int:
    """Calculate the sum of letters needed to write out all numbers from 1 to n."""
    result = 0
    # Iterate over the range from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Convert each number to words, remove hyphens and spaces, and calculate the length
        word_length = len(num2words(i).replace('-', '').replace(' ', ''))
        result += word_length
    return result


print(sum_letters(1000))  # Print the sum of letters

# Expected output: 21124
