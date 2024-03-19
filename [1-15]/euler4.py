"""
This function finds the largest palindrome product of two 3-digit numbers.

Args:
    None

Returns:
    tuple: A tuple containing the largest palindrome product and the pair of 3-digit numbers that produce it.

Example:
    Calling the function `largest_palindrome_product()` will find the largest palindrome product of two 3-digit numbers
    and return a tuple containing the product and the corresponding pair of numbers.

Note:
    A palindrome is a number that remains the same when its digits are reversed.
    The function iterates through all possible products of two 3-digit numbers (ranging from 100 to 999),
    checking if each product is a palindrome by converting it to a string and comparing it with its reverse.
    If a palindrome is found, it is stored in a dictionary along with the pair of numbers that produce it.
    Finally, the maximum palindrome product and the corresponding pair of numbers are returned.

"""


def largest_palindrome_product():
    products_of_3 = {}
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if str(product) == str(product)[::-1]:  # check if the product is a palindrome
                products_of_3[product] = (i, j)

    largest_palindrome = max(products_of_3)
    corresponding_pair = products_of_3[largest_palindrome]
    return largest_palindrome, corresponding_pair


# Example usage:
largest_palindrome, corresponding_pair = largest_palindrome_product()
print(largest_palindrome, corresponding_pair)  # Expected output: 906609 (924, 962)
