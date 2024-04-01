"""
This script calculates the number of possible paths in a grid of size 20x20, moving only right or down.

Explanation:
    The script defines a function `factorial` to compute the factorial of a given integer `n`.
    Then, it defines a function `steps` to calculate the number of possible paths in a grid of size 20x20.
    The number of possible paths from the top-left corner to the bottom-right corner in a grid of size n x n,
    moving only right or down, is calculated using combinatorial mathematics.
    It computes the binomial coefficient C(2n, n), which represents the number of combinations of choosing n items from 2n items.
    The formula for the binomial coefficient is C(n, k) = n! / (k! * (n - k)!).
    Therefore, the number of possible paths is C(2n, n) = (2n)! / (n! * (2n - n)!).
    Finally, it returns the result as an integer.

Note:
    - The script assumes that the grid is square (i.e., the number of rows equals the number of columns).
    - It uses the factorial function to calculate binomial coefficients efficiently.

Example:
    The script calculates the number of possible paths in a 20x20 grid, moving only right or down.
    It computes the binomial coefficient C(40, 20) using the formula mentioned above and returns the result.
"""


def factorial(n: int) -> int:
    """Compute the factorial of a given integer n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def steps(n: int) -> int:
    """Calculate the number of possible paths in a grid of size n x n."""
    return int(factorial(n * 2) / (factorial(n) * factorial(n * 2 - n)))


# Print the result for a 20x20 grid
print(steps(20))

# Expected output: 137846528820
