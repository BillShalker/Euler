"""
This script finds the largest product of 13 adjacent digits in a given number.

Args:
    None

Returns:
    int: The largest product of 13 adjacent digits in the given number.

Explanation:
    The script begins by defining a multi-line string `number` containing a large number represented as a string.
    It removes any whitespace and newline characters from the string using the `replace` method.
    Then, it converts each character in the string to an integer and stores them in a list `integers`.

    Next, it initializes an empty list `answers` to store the products of 13 adjacent digits.
    It iterates over the indices of the `integers` list using a for loop.
    For each index `i`, it calculates the product of 13 adjacent digits starting from that index.
    It then appends the result to the `answers` list.

    After iterating through all possible combinations, it finds the maximum value in the `answers` list,
    which represents the largest product of 13 adjacent digits in the given number.

Example:
    The script processes the given large number to find the largest product of 13 adjacent digits.
    Finally, it prints the largest product found.
"""

# Define the large number as a multi-line string
number = """
        73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450
    """
# Remove whitespace and newline characters, then convert to list of integers
number = number.replace(" ", "").replace("\n", "")
integers = [int(character) for character in number]

answers = []

# Iterate through the indices of the integers list
for i in range(len(integers)):
    result = 1
    # Check if there are 13 adjacent digits starting from index i
    if i + 13 < len(integers):
        # Calculate the product of 13 adjacent digits
        for j in range(i, i + 13):
            result *= integers[j]
        # Append the product to the answers list
        answers.append(result)

# Find the maximum product among all combinations
print(max(answers))
