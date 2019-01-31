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
    x = str(x)
    middish_point = len(x) // 2
    if len(x) % 2 == 0:
        left_side = x[:middish_point]
        right_side = x[middish_point:][::-1]
    else:
        left_side = x[:middish_point]
        right_side = x[(middish_point+1):][::-1]
    return left_side == right_side

def get_largest():
    #  figures out largest palindrome of two three digit numbers.
    pals = []
    for x in range(100, 999):
        for y in range(100, 999):
            if is_pal(x * y):
                pals.append(x * y)
    return max(pals)

def non_idiot_answer():
    ans = max(i * j for i in range(100,1000) for j in range(100, 1000) if str(i * j) == str(i * j)[::-1])
    return str(ans)


'''
PROBLEM 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

def idiot_answer(n):
    #  first take product of everything up to n, then count down to see if it divides cleanly
    big_n = 1
    for x in range(1,n+1):
        big_n *=x
    for possible in range(1, big_n):
        if divides_clean(possible, n):
            break
    return possible


def divides_clean(x, n):
    for y in range(1,  n):
        if x % y != 0:
            return False
    return True

def non_idiot_answer():
    #  smallest number n thats evenly divided by {k1, k2,...km} is least common multiple of the numbers.
    #  LCM(x,y) = x * y / GCD(x, y) where GCD is greatest commont divisor





if __name__=='__main__':
    print(idiot_answer(10))
