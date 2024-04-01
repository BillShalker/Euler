"""
This w.

Explanation:
    The script initializes an empty dictionary `results` to store the number of steps for each integer.
    It defines a function `is_double` to check if a number is even.
    Then, it iterates from 1 to 999,999, calculating the number of steps required to reach 1 in the Collatz sequence for each number.
    For each number `n`, it counts the steps until `n` becomes 1 using the rules of the Collatz sequence:
        - If `n` is even, it divides `n` by 2.
        - If `n` is odd, it multiplies `n` by 3 and adds 1.
    It stores the number of steps for each `n` in the `results` dictionary.
    After processing all numbers, it finds the number with the maximum steps and prints the result.

Note:
    - The Collatz sequence, also known as the hailstone sequence, is a sequence of numbers where each term is obtained from the previous term as follows:
        - If the previous term is even, the next term is half of it.
        - If the previous term is odd, the next term is 3 times it plus 1.
    - The script iterates over numbers up to one million, storing the number of steps for each integer to avoid recalculating steps for numbers that have already been processed.

Example:
    The script calculates the maximum number of steps in the Collatz sequence for numbers up to one million.
    Finally, it prints the number with the maximum steps and the corresponding number of steps.
"""

results = {}  # Dictionary to store the number of steps for each integer


def is_double(f):
    """Check if a number is even."""
    return True if f % 2 == 0 else False


# Iterate over numbers from 1 to 999,999
for i in range(1, 1000000):
    n = i
    step = 0
    # Calculate steps until reaching 1 in the Collatz sequence
    while n != 1:
        if n in results:
            step += results[n]
            n = 1
        elif is_double(n):
            n /= 2
            step += 1
        elif not is_double(n):
            n = 3 * n + 1
            step += 1
    results[i] = step

# Find the number with the maximum steps
max_steps = 0
max_number = ''
for el in results:
    if results[el] > max_steps:
        max_number = el
        max_steps = results[el]

# Print the result
print(f"The largest number in the Collatz sequence under one million is {max_number}, which has {max_steps} steps.")

# Expected output: 837799, which has 524 steps.
