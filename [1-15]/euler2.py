"""
This script calculates the sum of even-valued terms in the Fibonacci sequence up to a certain limit.

Args:
    n (int): The upper limit (exclusive) up to which to consider the Fibonacci sequence terms.

Returns:
    int: The sum of even-valued terms in the Fibonacci sequence below the given limit.

Example:
    If we call the script with no arguments, it will consider Fibonacci sequence terms up to a limit of 4,000,000.
    It will then find and sum all even-valued terms in the sequence and print the result.

Note:
    The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones,
    usually starting with 0 and 1. In this script, the sequence starts with 1 and 2.
"""


def fibonacci(n):  # recursive function to calculate fibonacci sequence
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


i = 0
result = 0
while fibonacci(i) < 4000000:  # 4000000 is the limit of the Fibonacci sequence
    if fibonacci(i) % 2 == 0:  # check if the Fibonacci term is even
        result += fibonacci(i)
    i += 1

print(result)  # Expected output: 4613732

"""
This Python script defines a recursive function `fibonacci(n)` to calculate the Fibonacci sequence. 
Then, it iterates through the Fibonacci sequence terms, starting from 0, until reaching a term greater than or equal to 4,000,000.
During this iteration, it checks if each Fibonacci term is even and adds it to the result if it is.
Finally, it prints the sum of all even-valued terms.
"""
