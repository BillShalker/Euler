"""
This function finds a Pythagorean triplet whose sum equals a given number.

Args:
    n (int): The target sum of the Pythagorean triplet.

Returns:
    str or None: A string representing the Pythagorean triplet if found, or None if no such triplet exists.

Explanation:
    The function `pythagoras_triplet(n)` takes an integer n as input and iterates over values of m and n
    to find a Pythagorean triplet (a, b, c) such that a + b + c equals n.
    It uses nested loops to iterate over all possible values of m and n.
    For each pair of m and n, it calculates the three sides of a Pythagorean triplet using the formulas:
        a = m^2 - n^2
        b = 2 * m * n
        c = m^2 + n^2
    It then checks if the sum of the three sides equals n.
    If a triplet satisfying the condition is found, it constructs a string representing the sides of the triplet
    along with the values of m and n, and returns it.
    The function terminates after finding the first triplet that satisfies the condition.

Example:
    Calling the function with an argument of 1000 will find a Pythagorean triplet whose sum equals 1000.
    It then returns a string representing the sides of the triplet and the values of m and n.
    If no such triplet exists, it returns None.

"""


def pythagoras_triplet(n):
    for m in range(1, 100):
        for n in range(1, m):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            if a + b + c == n:
                result = f"{a} + {b} + {c} = {a + b + c} | m = {m} n = {n}"
                return result
