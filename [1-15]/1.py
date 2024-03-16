"""If we list all the natural numbers below 10 that are multiples of 3 or 5 , we get 3 , 5 , 6 and 9.

The sum of these multiples is 23 . Find the sum of all the multiples of 3 or 5 below 1000 ."""


def f(n):
    result = 0
    for i in range(n + 1):  # +1 to include n
        if n % 3 == 0 or n % 5 == 0:  # check if divisible by 3 or 5 without remainder
            result += n


print(f(1000))
