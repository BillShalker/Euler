"""
This function generates the nth prime number.

Args:
    n (int): The ordinal number of the prime number to generate.

Returns:
    int: The nth prime number.

Explanation:
    This function iteratively generates prime numbers until it finds the nth prime number.
    It starts checking for prime numbers from 2 and keeps generating prime numbers until it has found n of them.
    For each number being checked, it verifies whether it is prime by ensuring it is not divisible by any prime number found so far.
    If the number is prime, it adds it to the list of primes.
    Finally, it returns the nth prime number.

Example:
    Calling the function with an argument of 10001 will generate and return the 10001st prime number (104743).
"""


def generate_primes(n):
    # Initialize an empty list to store prime numbers
    primes = []
    # Start checking for prime numbers from 2
    num = 2
    # Keep generating prime numbers until we have found n of them
    while len(primes) < n:
        # Check if the current number is prime
        # by verifying that it is not divisible by any prime number found so far
        if all(num % prime != 0 for prime in primes):
            # If the number is prime, add it to the list of primes
            primes.append(num)
        # Move to the next number
        num += 1
    # Return the nth prime number
    return primes[-1]


# Print the 10001st prime number
print(generate_primes(10001))  # 104743
