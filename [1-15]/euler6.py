"""
This function calculates the difference between the square of the sum and the sum of squares of the first n natural numbers.

Args:
    n (int): The upper limit of the range of natural numbers.

Returns:
    int: The difference between the square of the sum and the sum of squares of the first n natural numbers.

Example:
    If we call the function with an argument of 100, it will calculate the difference between the square of the sum
    and the sum of squares of the first 100 natural numbers and print the result.

Explanation:
    This Python function `difference(n)` calculates the difference between the square of the sum and the sum of squares
    of the first `n` natural numbers. It iterates through the range of numbers from 1 to `n`, accumulating the sum of squares
    and the sum of the numbers. Then, it calculates the square of the sum. Finally, it returns the difference between
    the square of the sum and the sum of squares.

"""


def difference(n):
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, n + 1):
        sum_of_squares += i ** 2  # calculate the sum of squares
        square_of_sum += i  # calculate the sum of numbers
    square_of_sum = square_of_sum ** 2  # calculate the square of the sum
    return square_of_sum - sum_of_squares  # return the difference


print(difference(100))  # Expected output: 25164150
"""
This function calculates the difference between the square of the sum and the sum of squares of the first `n` natural numbers.
It iterates through the range of numbers from 1 to `n`, accumulating the sum of squares and the sum of the numbers.
Then, it calculates the square of the sum.
Finally, it returns the difference between the square of the sum and the sum of squares.

"""
