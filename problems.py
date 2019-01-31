'''

Euler problem sets

questions: https://projecteuler.net/archives
answers:   https://github.com/nayuki/Project-Euler-solutions/tree/master/python

'''

'''
PROBLEM 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''
#  need to find two numbers x, y such that x and y have 3 digits, xy = z such that z can be read the same way both ways


def is_pal(x):
    if type(x) != str:
        x = str(x)
    digits = list(x)
    limit = len(digits) // 2

    for inc in range(0, limit):
        if not digits[inc] == digits[-inc]:
            return False
    return True
